# os - встроенный модуль Python для чтения переменных из .env
import os

# requests - библиотека для HTTP-запросов
import requests as req

# FastAPI инструменты:
from fastapi import APIRouter   # APIRouter группирует маршруты 
from fastapi import Depends     # Depends внедрение зависимостей
from fastapi import HTTPException  # HTTPException возвращает ошибку клиенту
from fastapi import Request     # Request объект входящего запроса (что то по типу cookies)
from fastapi.responses import RedirectResponse  # RedirectResponse перенаправляет браузер
from fastapi.responses import JSONResponse      # JSONResponse возвращает JSON-ответ

# SQLAlchemy сессия для работы с базой данных
from sqlalchemy.orm import Session  
# импортируем Session чтобы Python понимал что за тип данных приходит в db
# Сам объект Session создаётся не здесь
# он создаётся в database.py функцией get_db() и передаётся через Depends

# jose - библиотека для создания и проверки JWT токенов
# JWT (JSON Web Token) - зашифрованный токен для хранения данных о пользователе
from jose import jwt      # jwt.encode - создать токен, jwt.decode - прочитать токен
from jose import JWTError # JWTError - ошибка при неверном токене

# datetime для установки срока действия токена
from datetime import datetime, timedelta 
# timedelta представляет отрезок времени 

# load_dotenv читает .env файл и загружает переменные
from dotenv import load_dotenv

# Импортируем модули
from database import get_db  # функция для получения сессии базы данных
from models import User       # модель пользователя (таблица users)

# Загружаем переменные из файла .env
load_dotenv()

# Читаем настройки из .env файла
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")       # ID нашего приложения в Google
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")   # секретный ключ от Google
SECRET_KEY = os.getenv("SECRET_KEY", "secret")        # ключ для шифрования JWT токенов
REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:8000/auth/callback")  # куда Google вернёт пользователя
FRONTEND_URL = "http://localhost:3000"  # адрес нашего фронтенда
ALGORITHM = "HS256"  # алгоритм шифрования JWT токена

# роутер группа маршрутов с префиксом /auth
# Все маршруты ниже будут начинаться с /auth/
router = APIRouter(prefix="/auth", tags=["auth"])


def create_token(user_id):
    """
    Создаёт JWT токен для пользователя.
    JWT токен - это строка с зашифрованными данными о пользователе.
    Браузер хранит этот токен в cookie и отправляет с каждым запросом.
    """

    # Устанавливаем срок действия токена 7 дней от текущего момента
    expire = datetime.utcnow() + timedelta(days=7)

    # Создаём токен с данными: ID пользователя и время истечения
   #.encode() - метод библиотеки jose для создания JWT токена
    token = jwt.encode(
        {"sub": str(user_id), "exp": expire},  # данные внутри токена
        SECRET_KEY,    # ключ для шифрования
        algorithm=ALGORITHM  # алгоритм шифрования
    )

    return token  # возвращаем готовый токен


def get_current_user(request, db):
    """
    Читает JWT токен из cookie и возвращает текущего пользователя.
    Если токена нет или он неверный, возвращает None.
    Используется во всех защищённых маршрутах (избранное).
    """

    # Читаем токен из cookie запроса
    token = request.cookies.get("access_token")

    # Если токена нет, пользователь не авторизован
    if not token:
        return None

    try:
        # Расшифровываем токен и получаем данные из него
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Извлекаем ID пользователя из токена
        user_id = int(payload["sub"])

        # Ищем пользователя в базе данных по ID
        user = db.query(User).filter(User.id == user_id).first()

        return user  # возвращаем найденного пользователя

    except (JWTError, ValueError):
        # Если токен неверный или устарел, возвращаем None
        return None


# Маршрут. начало входа через Google 

@router.get("/login") #Когда кто-то открывает адрес /auth/login методом GET, вызови функцию login()
def login():
    """
    Перенаправляет пользователя на страницу входа Google.
    Браузер открывает Google, пользователь выбирает аккаунт.
    """

    # Если ключи Google не настроены, сообщаем об ошибке
    if not GOOGLE_CLIENT_ID:
        raise HTTPException(500, "GOOGLE_CLIENT_ID не задан в .env") #500 - код ошибки на стороне сервера.

    # Собираем параметры запроса к Google
    params = "&".join([                           #соединяет список строк через &
        f"client_id={GOOGLE_CLIENT_ID}",          # наш ID приложения
        f"redirect_uri={REDIRECT_URI}",           # куда вернуть после входа
        "response_type=code",                     # просим код авторизации
        "scope=openid%20email%20profile",         # просим доступ к email и профилю
    ])

    # Перенаправляем браузер на страницу входа Google
    return RedirectResponse(f"https://accounts.google.com/o/oauth2/v2/auth?{params}")


# Google возвращает пользователя обратно 

@router.get("/callback")
def callback(code: str, db: Session = Depends(get_db)):
    """
    Google перенаправляет сюда после того как пользователь выбрал аккаунт.
    code - одноразовый код от Google, обмениваем его на токен доступа.
    """

    # 1. Обмениваем code на access_token (ключ для получения данных пользователя)
    # отправляем данные на сервер Google чтобы обменять code на access_token
    token_response = req.post(
        "https://oauth2.googleapis.com/token",   # адрес Google для обмена кода
        data={
            "code":          code,                # код от Google
            "client_id":     GOOGLE_CLIENT_ID,    # наш ID приложения
            "client_secret": GOOGLE_CLIENT_SECRET, # наш секретный ключ
            "redirect_uri":  REDIRECT_URI,         # должен совпадать с тем что в Google Console
            "grant_type":    "authorization_code", # тип авторизации
        },
    )

    # Если Google вернул ошибку
    if token_response.status_code != 200:
        raise HTTPException(400, f"Ошибка Google: {token_response.text}")

    # Извлекаем access_token из ответа Google
    access_token = token_response.json().get("access_token")

    # 2. Используем access_token чтобы получить данные пользователя
    user_info = req.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",  # адрес API профиля Google
        headers={"Authorization": f"Bearer {access_token}"},  # передаём токен
    ).json()  # сразу превращаем ответ в словарь

    #3. Ищем пользователя в нашей базе данных
    # filter - ищем по google_id 
    # .first() - берём первый результат или None если не нашли
    user = db.query(User).filter(User.google_id == user_info["id"]).first()

    if not user:
        # Пользователь входит впервые - создаём новую запись в базе
        user = User(
            google_id = user_info["id"],              # ID от Google
            email     = user_info.get("email", ""),   # email
            name      = user_info.get("name", ""),    # имя
            picture   = user_info.get("picture", ""), # фото
        )
        db.add(user)     # добавляем в сессию
        db.commit()      # сохраняем в базу
        db.refresh(user) # обновляем объект 
    else:
        # обновляем данные пользователя
        user.name = user_info.get("name", user.name)
        user.picture = user_info.get("picture", user.picture)
        db.commit()

    # 4. Создаём JWT токен для нашего приложения
    jwt_token = create_token(user.id)

    # 5. Перенаправляем пользователя на фронтенд
    redirect = RedirectResponse(url=FRONTEND_URL)

    # Сохраняем JWT токен в cookie браузера
    # httponly=True - JavaScript не может читать этот cookie (защита от XSS атак)
    # атака когда злоумышленник внедряет вредоносный JavaScript код на сайт
    # max_age=604800 - время жизни cookie в секундах (604800 = 7 дней)
    # samesite="lax" - защита от CSRF атак
    redirect.set_cookie(
        key="access_token",
        value=jwt_token,
        httponly=True,
        max_age=604800,
        samesite="lax",
    )

    return redirect  # браузер переходит на localhost:3000 с установленным cookie


#   получить данные текущего пользователя 

@router.get("/me")
def me(request: Request, db: Session = Depends(get_db)):
    """
    Возвращает данные текущего авторизованного пользователя.
    Фронтенд вызывает этот маршрут при загрузке страницы чтобы узнать кто вошёл.
    """

    # Получаем текущего пользователя из токена в cookie
    user = get_current_user(request, db)

    # Если пользователь не авторизован - возвращаем null
    if not user:
        return {"user": None}

    # Возвращаем данные пользователя
    return {
        "user": {
            "id":      user.id,
            "email":   user.email,
            "name":    user.name,
            "picture": user.picture,
        }
    }

# выход из аккаунта 

@router.post("/logout")
def logout():
    """
    Выход из аккаунта удаляет JWT токен из cookie браузера.
    """

    # Создаём JSON-ответ с сообщением
    response = JSONResponse({"message": "Вышли из аккаунта"})

    # Удаляем cookie с токеном - пользователь становится неавторизованным
    response.delete_cookie("access_token")

    return response
