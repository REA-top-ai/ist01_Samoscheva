# FastAPI - программная платформа для создания веб-API на Python
from fastapi import FastAPI
from fastapi import Depends        # Depends - внедрение зависимостей (например get_db)
from fastapi import HTTPException  # HTTPException - возвращает ошибку с кодом клиенту
from fastapi import Request        # Request - объект входящего HTTP-запроса

# CORSMiddleware - разрешает фронтенду (localhost:3000) обращаться к бэкенду (localhost:8000)
# Без этого браузер блокирует запросы между разными портами
from fastapi.middleware.cors import CORSMiddleware

# Session - тип объекта сессии базы данных (нужен для type hints)
from sqlalchemy.orm import Session

# Counter - считает сколько раз встречается каждый элемент в списке
from collections import Counter

# Наши модули:
from database import Base, engine, get_db  # Base - базовый класс таблиц, engine - подключение к БД, get_db - сессия
import models                              # импортируем все модели чтобы SQLAlchemy их увидел
from services import get_universities, extract_country, save_query  # функции работы с университетами
from ai import ai_analyze                  # функция AI-анализа через Groq
from auth import router as auth_router     # роутер авторизации (/auth/login, /auth/callback и т.д.)
from auth import get_current_user          # функция получения текущего пользователя из cookie
from schemas import AnalyzeRequest, FavoriteCreate  # схемы данных для запросов
from models import Favorite, Query         # модели таблиц 

# Создаём все таблицы в базе данных если их ещё нет
# Base.metadata.create_all - проходит по всем моделям и создаёт таблицы
Base.metadata.create_all(bind=engine)

# Создаём приложение FastAPI
app = FastAPI(title="UniInsight API")

# Подключаем CORS - разрешаем фронтенду делать запросы к бэкенду
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # разрешаем запросы только с фронтенда
    allow_credentials=True,                   # разрешаем передавать cookies
    allow_methods=["*"],                      # разрешаем все HTTP-методы
    allow_headers=["*"],                      # разрешаем все заголовки
)

# Подключаем роутер авторизации
# Все маршруты из auth.py 
app.include_router(auth_router)


# Главная страница 

@app.get("/")
def root():
    # маршрут для проверки что сервер работает
    return {"message": "UniInsight API работает", "docs": "/docs"}


# ии анализ
@app.post("/analyze")
def analyze(data: AnalyzeRequest, db: Session = Depends(get_db)):
    """
    Главный маршрут приложения.
    1. Принимает текстовый запрос пользователя
    2. Определяет страну из текста
    3. Получает университеты этой страны из Hipolabs API
    4. Отправляет всё в Groq AI
    5. Возвращает AI-анализ с рекомендациями
    """

    # data.query - текст запроса
    # .strip() - убирает пробелы в начале и конце строки
    query = data.query.strip()

    # Если запрос пустой - возвращаем ошибку 400 
    if not query:
        raise HTTPException(status_code=400, detail="Запрос не может быть пустым")

    # Определяем страну из текста запроса
    country = extract_country(query)

    # Сохраняем запрос в историю 
    save_query(db, query, country)

    # Получаем список университетов этой страны из Hipolabs API
    unis = get_universities(country)

    # Если университеты не найдены, возвращаем ошибку 404 
    if not unis:
        raise HTTPException(status_code=404, detail=f"Университеты для '{country}' не найдены")

    # Отправляем запрос и список университетов в Groq AI
    # AI выбирает 10 подходящих и добавляет анализ по каждому
    ai_result = ai_analyze(query, unis)

    # Возвращаем результат фронтенду
    return {
        "country":            country,       # определённая страна
        "universities_found": len(unis),     # сколько всего университетов нашли
        "result":             ai_result,     # список с ии-анализом
    }


# статистика

@app.get("/trends")
def trends(db: Session = Depends(get_db)):
    """
    Возвращает статистику: какие страны чаще всего ищут пользователи.
    Берёт данные из таблицы queries где хранится история запросов.
    """

    # Получаем все записи из таблицы queries
    all_queries = db.query(Query).all()

    # Собираем список стран из всех запросов
    # q.country for q in all_queries - берём поле country из каждой записи
    # if q.country - пропускаем записи где country пустой
    countries = [q.country for q in all_queries if q.country]

    # Counter считает сколько раз встречается каждая страна
    # Например, {"Germany": 5, "France": 3, "Italy": 1}
    counts = Counter(countries)

    # Возвращаем статистику
    return {
        "total_queries": len(all_queries),  # всего запросов
        "popular_countries": [
            {"country": name, "count": num}
            for name, num in counts.most_common(10)  # топ-10 стран
        ],
    }


# --- Избранное: добавить ---

@app.post("/favorites")
def add_favorite(fav: FavoriteCreate, request: Request, db: Session = Depends(get_db)):
    """
    Добавляет университет в избранное текущего пользователя.
    Требует авторизации - проверяет JWT токен из cookie.
    """

    # Получаем текущего пользователя из cookie
    user = get_current_user(request, db)

    # Если пользователь не авторизован - ошибка 401 
    if not user:
        raise HTTPException(status_code=401, detail="Необходима авторизация")

    # Проверяем не добавлен ли уже этот университет
    # .filter() - условие поиска, .first() - первый результат или None
    already_exists = db.query(Favorite).filter(
        Favorite.user_id == user.id,                        # принадлежит этому пользователю
        Favorite.university_name == fav.university_name,    # с таким же названием
    ).first()

    # Если уже есть - ошибка 400 
    if already_exists:
        raise HTTPException(status_code=400, detail="Уже в избранном")

    # Создаём новую запись в избранном
    new_fav = Favorite(
        user_id         = user.id,              # ID текущего пользователя
        university_name = fav.university_name,  # название университета
        website         = fav.website,          # сайт
        country         = fav.country,          # страна
    )

    db.add(new_fav)   # добавляем в сессию
    db.commit()       # сохраняем в базу

    return {"message": "Добавлено в избранное"}


#  Избранное,сп исок 

@app.get("/favorites")
def get_favorites(request: Request, db: Session = Depends(get_db)):
    """
    Возвращает список избранных университетов текущего пользователя.
    """

    # Получаем текущего пользователя из cookie
    user = get_current_user(request, db)

    # Если не авторизован - ошибка 401
    if not user:
        raise HTTPException(status_code=401, detail="Необходима авторизация")

    # Получаем все избранные записи этого пользователя из базы
    favs = db.query(Favorite).filter(Favorite.user_id == user.id).all()

    # Превращаем список объектов базы данных в список обычных словарей
    # Фронтенд работает со словарями, а не с объектами SQLAlchemy
    return [
        {
            "id":               f.id,
            "university_name":  f.university_name,
            "website":          f.website,
            "country":          f.country,
        }
        for f in favs  # проходим по каждой записи
    ]


# удалить из избранного

@app.delete("/favorites/{fav_id}")
def delete_favorite(fav_id: int, request: Request, db: Session = Depends(get_db)):
    """
    Удаляет университет из избранного.
    fav_id - ID записи в таблице favorites (приходит из URL)
    """

    # Получаем текущего пользователя из cookie
    user = get_current_user(request, db)

    # Если не авторизован - ошибка 401
    if not user:
        raise HTTPException(status_code=401, detail="Необходима авторизация")

    # Ищем запись в базе по ID и проверяем что она принадлежит этому пользователю
    fav = db.query(Favorite).filter(
        Favorite.id == fav_id,           # нужная запись по ID
        Favorite.user_id == user.id,     # принадлежит этому пользователю (защита)
    ).first()

    # Если не нашли - ошибка 404 
    if not fav:
        raise HTTPException(status_code=404, detail="Не найдено в избранном")

    db.delete(fav)   # удаляем запись из сессии
    db.commit()      # применяем изменения в базе

    return {"message": "Удалено из избранного"}
