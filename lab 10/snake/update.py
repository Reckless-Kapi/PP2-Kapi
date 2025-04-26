import psycopg2
from config import load_config


def update_person(name ,level, score, speed):
    
    updated_row_count = 0

    sql = f""" UPDATE snake
                SET user_level = {level}, user_score = {score}, user_speed = {speed}
                WHERE user_name = '{name}';"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql)
                updated_row_count = cur.rowcount

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

