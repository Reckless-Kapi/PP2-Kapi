import psycopg2
from config import load_config

def get_paginated_users(limit, offset):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM phone_book
                    ORDER BY person_id
                    LIMIT %s OFFSET %s
                """, (limit, offset))
                results = cur.fetchall()
                for row in results:
                    print(row)
    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    limit = int(input("Сколько записей показать? (LIMIT): "))
    offset = int(input("Пропустить сколько записей? (OFFSET): "))
    get_paginated_users(limit, offset)
