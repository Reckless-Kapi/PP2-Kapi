import psycopg2
from config import load_config


def create_table():
    config = load_config()

    sql = """CREATE TABLE snake(
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(30),
                user_level SMALLINT,
                user_score SMALLINT,
                user_speed SMALLINT
            )"""
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    create_table()
