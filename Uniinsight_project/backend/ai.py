# requests - библиотека для отправки HTTP-запросов в ии
import requests

# json - встроенный модуль Python для работы с JSON 
import json

# os встроенный модуль Python 
# используем для чтения переменных окружения из .env файла
import os

# load_dotenv - функция которая читает файл .env и загружает переменные в os.getenv
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Читаем API-ключ от Groq из файла .env
# Если ключ не найден, GROQ_API_KEY будет пустой строкой 
#os.getenv - функция которая ищет переменную по имени
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")


def ai_analyze(query, universities):
    """
    Отправляет запрос пользователя и список университетов в Groq AI.
    ИИ выбирает 10 подходящих университетов и возвращает анализ по каждому.

    query - текст запроса пользователя
    universities - список словарей с университетами из Hipolabs API
    """

    # Если ключ не задан - возвращаем ошибку сразу, не делая запрос
    if not GROQ_API_KEY:
        return {"error": "Добавь GROQ_API_KEY в файл .env"}

    # Берём первые 20 университетов из списка
    top_20 = universities[:20]

    # Превращаем список университетов в текст для промпта
    uni_list = "\n".join(
        f"- {u['name']} | {u.get('website', '')}"
        for u in top_20
    )

    # Промпт
    prompt = f"""Ты консультант по поступлению в зарубежные университеты.

Верни ТОЛЬКО JSON массив - без пояснений, без markdown, только сырой JSON.

Формат каждого элемента:
{{
  "name": "Название университета",
  "website": "https://...",
  "tuition": "примерный диапазон стоимости в год - уточняй на официальном сайте",
  "requirements": "какие экзамены и документы нужны",
  "chance": "High, Medium или Low",
  "comment": "1-2 предложения почему этот университет подходит"
}}

Запрос пользователя: {query}

Список университетов:
{uni_list}

Выбери 10 наиболее подходящих. Ответ - только JSON массив."""

    # Отправляем POST-запрос в ии
    # POST  тип запроса для отправки данных на сервер
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",  # адрес Groq API
        headers={
            # headers- заголовки запроса (метаданные)
            "Authorization": f"Bearer {GROQ_API_KEY}",  # ключ для авторизации
            "Content-Type": "application/json",          # говорим что отправляем JSON
        },
        json={
            # тело запроса, что отправляем в ии
            "model": "llama-3.1-8b-instant",  # название ии модели
            "messages": [
                {
                    "role": "user",        # роль - пользователь 
                    "content": prompt      # сам промпт
                }
            ],
            #temperature - параметр который управляет "творчеством" ии
            "temperature": 0.3,           # температура: 0 = точный, 1 = творческий
        },
        timeout=30,  # ждём ответа не более 30 секунд
    )

    # Если Groq вернул ошибку 
    if response.status_code != 200:
        return {"error": "Ошибка запроса к Groq", "details": response.text}

    # Извлекаем текст ответа из JSON-ответа Groq
    # Путь до текста ответа ии
    text = response.json()["choices"][0]["message"]["content"].strip()

    #.strip() - Убирает лишние пробелы и переносы строк в начале и конце текста

    # Если ии оборачивает ответ в ```json ... ```, убираем это
    if "```" in text:
        # split("\n") - разбиваем текст на строки
        # отфильтровываем строки начинающиеся с ```
        lines = [line for line in text.split("\n") if not line.startswith("```")]
        #.startswith() - метод строки который проверяет начинается ли строка с указанного текста.
        text = "\n".join(lines).strip()  # собираем обратно в текст

    # Превращаем текст JSON в Python-список словарей
    try:
        return json.loads(text)   # json.loads - парсит JSON-текст в Python-объект
    except Exception:
        # Если ии вернул что-то не то, возвращаем ошибку с сырым текстом
        return {"error": "AI вернул не JSON", "raw": text}
