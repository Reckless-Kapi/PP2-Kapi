import psycopg2
from config import load_config

def get_player_data(name):
    config = load_config()

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM snake WHERE user_name = '{name}'")


                row = cursor.fetchone()

                print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return row


if __name__ == "__main__":
    get_player_data("Batyrlan")