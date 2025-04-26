import psycopg2
from config import load_config

def delete_user(identifier):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM phone_book
                    WHERE name = %s OR phone_number = %s
                """, (identifier, identifier))
                
                if cur.rowcount > 0:
                    print("Пользователь удалён.")
                else:
                    print("Пользователь не найден.")
    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    identifier = input("Введите имя или номер телефона для удаления: ")
    delete_user(identifier)
