import psycopg2
from config import load_config

def create_table():
    config = load_config(filename='lab 10/phonebook/database.ini')
    command = """CREATE TABLE phone_book(
                    person_id SERIAL PRIMARY KEY,
                    name VARCHAR(30) NOT NULL,
                    second_name VARCHAR(30) NOT NULL,
                    last_name VARCHAR(30) NOT NULL,
                    phone_number VARCHAR(30) NOT NULL
                )"""
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    create_table()