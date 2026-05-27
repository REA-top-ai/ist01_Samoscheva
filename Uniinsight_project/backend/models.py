# Импортируем типы колонок из SQLAlchemy
from sqlalchemy import Column      # Column - обозначает колонку в таблице
from sqlalchemy import Integer     # Integer - целое число
from sqlalchemy import String      # String - строка текста
from sqlalchemy import Text        # Text - длинный текст (без ограничения длины)
from sqlalchemy import DateTime    # DateTime - дата и время
from sqlalchemy import ForeignKey  # ForeignKey - внешний ключ, связь между таблицами
from sqlalchemy import Boolean     # Boolean - логическое значение (True/False)

from sqlalchemy.orm import relationship  # relationship - описывает связь между объектами

from database import Base          # Base - базовый класс, от него наследуем все таблицы
from datetime import datetime      # datetime - для записи текущего времени


#  Таблица пользователей 
# Здесь хранятся все пользователи, которые вошли через Google

class User(Base):
    __tablename__ = "users"        # название таблицы в базе данных

    # Колонки таблицы:
    id         = Column(Integer, primary_key=True, index=True)           # уникальный номер пользователя (автоматически увеличивается)
    google_id  = Column(String(100), unique=True, nullable=False)        # ID пользователя в Google (уникальный, обязательный)
    email      = Column(String(100), unique=True, nullable=False)        # email пользователя (уникальный, обязательный)
    name       = Column(String(100), nullable=False)                     # имя пользователя (обязательное)
    picture    = Column(String(300))                                     # ссылка на фото профиля (необязательное)
    created_at = Column(DateTime, default=datetime.utcnow)              # дата и время регистрации

    # Связь с таблицей Favorite:
    # cascade="all, delete-orphan" - если удалить пользователя, его избранное тоже удалится
    favorites = relationship("Favorite", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        # __repr__ - метод, который показывает объект в понятном виде при выводе в консоль
        # Например: <User id=1 email=test@gmail.com>
        return f"<User id={self.id} email={self.email}>"


# Таблица избранных университетов 
# Каждая строка = один университет в избранном у одного пользователя

class Favorite(Base):
    __tablename__ = "favorites"    # название таблицы в базе данных

    # Колонки таблицы:
    id               = Column(Integer, primary_key=True, index=True)          # уникальный номер записи
    user_id          = Column(Integer, ForeignKey("users.id"), nullable=False) # ID пользователя (обязательный)
    university_name  = Column(String(200), nullable=False)                    # название университета (обязательное)
    website          = Column(String(300))                                    # сайт университета (необязательный)
    country          = Column(String(100))                                    # страна университета (необязательная)
    created_at       = Column(DateTime, default=datetime.utcnow)              # дата добавления в избранное

    # Связь с таблицей User - из избранного можно получить данные пользователя
    user = relationship("User", back_populates="favorites")

    def __repr__(self):
        # Показывает объект Favorite в понятном виде при выводе в консоль
        return f"<Favorite id={self.id} university={self.university_name}>"


#  Таблица истории запросов 
# Сохраняем каждый запрос пользователя - нужно для статистики (/trends)

class Query(Base):
    __tablename__ = "queries"      # название таблицы в базе данных

    # Колонки таблицы:
    id         = Column(Integer, primary_key=True, index=True)    # уникальный номер запроса
    query_text = Column(Text, nullable=False)                     # текст запроса пользователя (обязательный)
    country    = Column(String(100))                              # определённая страна (необязательная)
    created_at = Column(DateTime, default=datetime.utcnow)        # дата и время запроса

    def __repr__(self):
        # Показывает объект Query в понятном виде при выводе в консоль
        return f"<Query id={self.id} country={self.country}>"


# Этот блок выполняется только если запустить models.py напрямую (python models.py)
# При импорте из других файлов этот блок НЕ выполняется
if __name__ == "__main__":
    from database import engine
    # Создаём все таблицы в базе данных
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы!")
