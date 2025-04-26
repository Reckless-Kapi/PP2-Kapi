import psycopg2
from config import load_config

def insert_player_result(name, level, score, speed):
    sql = f"""INSERT INTO snake(user_name, user_level, user_score, user_speed) VALUES('{name}', {level}, {score}, {speed}) RETURNING user_id;"""
    config = load_config()
    user_id = None
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)

                rows = cursor.fetchone()
                if rows:
                    user_id = rows[0]

                connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return user_id
    

if __name__ == "__main__":
    insert_player_result("mkhmtcore", 45, 1000, 5)

