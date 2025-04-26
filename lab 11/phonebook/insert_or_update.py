import psycopg2
from config import load_config

def insert_or_update_user(name, second_name, last_name, phone_number):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Проверка, есть ли пользователь
                cur.execute("""
                    SELECT * FROM phone_book
                    WHERE name = %s AND second_name = %s AND last_name = %s
                """, (name, second_name, last_name))
                
                user = cur.fetchone()
                
                if user:
                    # Если пользователь есть, обновляем телефон
                    cur.execute("""
                        UPDATE phone_book
                        SET phone_number = %s
                        WHERE name = %s AND second_name = %s AND last_name = %s
                    """, (phone_number, name, second_name, last_name))
                    print("Телефон обновлён.")
                else:
                    # Иначе вставляем нового
                    cur.execute("""
                        INSERT INTO phone_book (name, second_name, last_name, phone_number)
                        VALUES (%s, %s, %s, %s)
                    """, (name, second_name, last_name, phone_number))
                    print("Пользователь добавлен.")
    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    name = input("Введите имя: ")
    second_name = input("Введите отчество: ")
    last_name = input("Введите фамилию: ")
    phone_number = input("Введите номер телефона: ")
    insert_or_update_user(name, second_name, last_name, phone_number)
