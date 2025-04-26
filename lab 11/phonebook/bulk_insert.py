import psycopg2
from config import load_config

def is_valid_phone(phone):
    return phone.isdigit()

def bulk_insert_users(users):
    config = load_config()
    invalid_users = []
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for user in users:
                    name, second_name, last_name, phone_number = user
                    if is_valid_phone(phone_number):
                        cur.execute("""
                            INSERT INTO phone_book (name, second_name, last_name, phone_number)
                            VALUES (%s, %s, %s, %s)
                        """, (name, second_name, last_name, phone_number))
                    else:
                        invalid_users.append(user)
    except Exception as e:
        print("Ошибка:", e)

    return invalid_users

if __name__ == "__main__":
    users = [
        ("Almas", "Askaruly", "Amanov", "87578072322"),
        ("Test", "Testovich", "Tester", "invalid_phone"),  # Неправильный
        ("Aliya", "Karimovna", "Seidakhmet", "87475674567")
    ]

    bad_users = bulk_insert_users(users)
    if bad_users:
        print("Некорректные пользователи:")
        for u in bad_users:
            print(u)
    else:
        print("Все пользователи успешно добавлены.")
