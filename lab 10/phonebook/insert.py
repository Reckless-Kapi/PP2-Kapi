import psycopg2
from csv import DictReader
from config import load_config

def insert_data(name, second_name, last_name, phone_number):
    config = load_config()
    sql = f"""INSERT INTO phone_book(name, second_name, last_name, phone_number) VALUES('{name}', '{second_name}', '{last_name}', {phone_number}) RETURNING person_id;"""
    
    person_id = None

    try:
        with psycopg2.connect(**config) as connection:
            print("Connected")
            with connection.cursor() as cursor:
                cursor.execute(sql)

                rows = cursor.fetchone()
                if rows:
                    person_id = rows[0]


                connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return person_id
    

if __name__ == "__main__":
    if input("Вы хотите ввести данные вручну? y/n \n").lower() == "y":
        insert_data(input("Введите свое имя: "), input("Введите свое отчество: "), input("Введите фамилию: "), input("Номер телефона: "))
    else:
        print("В таком случае данные будут братся из csv файла.")
        with open("lab_10/phonebook/contacts.csv", mode="r", newline="") as data:
            contacts = DictReader(data)
        
            for contact in contacts:
                insert_data(contact["name"], contact["second_name"], contact["last_name"], contact["phone_number"])