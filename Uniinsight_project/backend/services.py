# requests - библиотека для отправки HTTP-запросов 
import requests

# Словарь. ключевое слово из текста -> официальное название страны для API
# Поддерживает русские и английские слова
COUNTRY_MAP = {
    "germany":        "Germany",
    "finland":        "Finland",
    "france":         "France",
    "italy":          "Italy",
    "canada":         "Canada",
    "usa":            "United States",
    "united states":  "United States",
    "america":        "United States",
    "japan":          "Japan",
    "china":          "China",
    "spain":          "Spain",
    "uk":             "United Kingdom",
    "england":        "United Kingdom",
    "australia":      "Australia",
    "netherlands":    "Netherlands",
    "sweden":         "Sweden",
    "norway":         "Norway",
    "denmark":        "Denmark",
    "switzerland":    "Switzerland",
    "austria":        "Austria",
    "poland":         "Poland",
    "portugal":       "Portugal",
    "belgium":        "Belgium",
    "turkey":         "Turkey",
    "south korea":    "South Korea",
    "singapore":      "Singapore",
    
    "германи":   "Germany",
    "герман":    "Germany",
    "финлянд":   "Finland",
    "франц":     "France",
    "итали":     "Italy",
    "канад":     "Canada",
    "сша":       "United States",
    "америк":    "United States",
    "япони":     "Japan",
    "кита":      "China",
    "испани":    "Spain",
    "британи":   "United Kingdom",
    "велик":     "United Kingdom",
    "австрали":  "Australia",
    "нидерланд": "Netherlands",
    "голланд":   "Netherlands",
    "швеци":     "Sweden",
    "норвеги":   "Norway",
    "дани":      "Denmark",
    "швейцари":  "Switzerland",
    "австри":    "Austria",
    "польш":     "Poland",
    "португали": "Portugal",
    "бельги":    "Belgium",
    "турци":     "Turkey",
    "корее":     "South Korea",
    "корея":     "South Korea",
    "сингапур":  "Singapore",
}


def get_universities(country):
    """
    Получает список университетов из открытого API Hipolabs.
    Hipolabs - бесплатный API с базой университетов всего мира.
    Возвращает список словарей: [{name, website, country}, ...]
    """

    # Формируем адрес запроса к API
    url = f"http://universities.hipolabs.com/search?country={country}"

    try:
        # Отправляем GET-запрос к API, ждём не более 10 секунд
        #метод протокола HTTP, предназначенный для получения данных с сервера
        response = requests.get(url, timeout=10)

        # Превращаем ответ из JSON-текста в список Python-словарей
        data = response.json()
    except Exception:
        # Если API не ответил или произошла ошибка - возвращаем пустой список
        return []

    # Пустой список для результатов
    result = []

    # Проходим по каждому университету из ответа API
    for uni in data:
        # Добавляем только нужные поля (name, website, country)
        result.append({
            "name":    uni["name"],                                           # название университета
            "website": uni["web_pages"][0] if uni.get("web_pages") else "",  # первый сайт из списка
            "country": uni.get("country", country),                          # страна
        })

    # Возвращаем готовый список университетов
    return result


def extract_country(query):
    """
    Определяет страну из текста запроса пользователя.
    Ищет ключевые слова из COUNTRY_MAP в тексте.
    Если ничего не нашли - по умолчанию возвращает Германию.
    """

    # Переводим запрос в нижний регистр чтобы сравнение было нечувствительно к регистру
    query_lower = query.lower()

    # Перебираем все ключевые слова из словаря
    for keyword, country in COUNTRY_MAP.items():

        # Если ключевое слово встречается в тексте запроса
        if keyword in query_lower:
            return country  # возвращаем название страны

    # Если не нашли ни одного совпадения - возвращаем Германию по умолчанию
    return "Germany"


def save_query(db, query_text, country):
    """
    Сохраняет запрос пользователя в таблицу queries.
    Это нужно для статистики - эндпоинт /trends считает популярные страны.
    """

    # Импортируем модель Query (импорт здесь чтобы не было циклических зависимостей)
    from models import Query
    from datetime import datetime

    # Создаём новую запись в таблице queries
    new_query = Query(
        query_text=query_text,       # текст запроса
        country=country,             # определённая страна
        created_at=datetime.utcnow() # текущее время
    )

    # Добавляем запись в сессию (ещё не сохранено в базу)
    db.add(new_query)

    # Сохраняем в базу данных
    db.commit()
