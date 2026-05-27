# Pydantic - библиотека для проверки данных
# BaseModel - базовый класс, от которого наследуем наши схемы
from pydantic import BaseModel

# Схема - это описание того, какие данные ожидает FastAPI в теле запроса
# FastAPI автоматически проверяет что пришедшие данные соответствуют схеме


# Схема для POST /analyze
# Когда фронтенд отправляет запрос на анализ, он должен прислать вот это:
class AnalyzeRequest(BaseModel):
    query: str          # поле "query" строка текста 



# Схема для POST /favorites
# Когда фронтенд добавляет университет в избранное, он присылает вот это:
class FavoriteCreate(BaseModel):
    university_name: str          
    website: str = ""           
    country: str = ""           
    
