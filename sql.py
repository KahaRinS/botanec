from locale import currency
from multiprocessing import connection
from types import NoneType
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from ConfigSQL import host, user, password, db_name


# подключение к таблице
connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
connection.autocommit = True

# Создание таблицы
# with connection.cursor() as cursor:
#    cursor.execute(
#        """CREATE TABLE users(
#            id serial PRIMARY KEY,
#            first_name varchar(50) NOT NULL,
#            nick_name varchar(50) NOT NULL);"""
#    )

# Вставка данных в таблицу


def Insert(first_name, second_name, user_id):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO users(
                            user_id, first_name, second_name) VALUES
                            ({user_id}, '{first_name}', '{second_name}');"""
            )
            print("Данные добавлены в таблицу")
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

# Получение данных из БД


def Search(user_id):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT second_name FROM users WHERE user_id = '{user_id}';""",
            )

            return cursor.fetchone()
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
