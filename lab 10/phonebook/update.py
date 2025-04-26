import psycopg2
from config import load_config


def update_person(person_id, change, text):
    
    updated_row_count = 0

    sql = f""" UPDATE phone_book
                SET {change} = '{text}'
                WHERE person_id = {person_id}"""
    
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

if __name__ == '__main__':
    update_person(1, "name", "Kassymkhan")