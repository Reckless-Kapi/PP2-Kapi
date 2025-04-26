import psycopg2
from config import load_config

def delete_by_name(name):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phone_book WHERE name = %s;", (name,))
                print(f"{cur.rowcount} record(s) deleted.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    user_input = input()
    delete_by_name(user_input)
