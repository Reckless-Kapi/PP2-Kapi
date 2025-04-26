import psycopg2
from config import load_config

def search_pattern(pattern):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
                results = cur.fetchall()
                for row in results:
                    print(row)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    user_input = input("Введите шаблон для поиска (например: Ali, 877): ")
    search_pattern(user_input)
