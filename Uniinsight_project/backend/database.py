from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Путь к файлу базы данных SQLite
# Файл unisiinsight.db создастся автоматически в папке backend
DATABASE_URL = "sqlite:///./uniinsight.db"

# check_same_thread=False нужно для SQLite чтобы работало с FastAPI
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# autoflush=False - не отправлять изменения автоматически
# autocommit=False - управлять транзакциями вручную через commit()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Базовый класс для всех таблиц
Base = declarative_base()

# Функция для получения сессии базы данных
# Используется в FastAPI через Depends(get_db)
def get_db():
    db = SessionLocal()  # открываем сессию
    try:
        yield db         # отдаём сессию в endpoint
    finally:
        db.close()       # закрываем сессию после завершения запроса
