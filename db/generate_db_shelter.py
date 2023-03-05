import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from faker import Faker
from faker_vehicle import VehicleProvider
from random import randint, choice, sample
import string
from animals import Animals

animal_name_m = []
with open('name_m.txt') as f:
    animal_name_m = f.read()
animal_name_m = animal_name_m.split('\n')
animal_name_m = animal_name_m[:-1]


animal_name_w = []
with open('name_w.txt') as f:
    animal_name_w = f.read()
animal_name_w = animal_name_w.split('\n')
animal_name_w = animal_name_w[:-1]


breed_dog = []
with open('breed_dog.txt') as f:
    breed_dog = f.read()
breed_dog = breed_dog.split('\n')
breed_dog = breed_dog[:-1]


breed_cat = []
with open('breed_cat.txt') as f:
    breed_cat = f.read()
breed_cat = breed_cat.split('\n')
breed_cat = breed_cat[:-1]


vaccination = []
with open('vaccination.txt') as f:
    vaccination = f.read()
vaccination = vaccination.split('\n')
vaccination = vaccination[:-1]


PRIVILEGE = ['admin', 'operator', 'content-menegere']

BREED_DOG = len(breed_dog)
BREED_CAT = len(breed_cat)
ANIMALS = len(animal_name_m) + len(animal_name_w)
VACCINATIONS = len(vaccination)
ANIMAL_X_VACCINETION = 2000
MESSAGE = 1000
USER = 100

DOG_VAC = 12
CAT_VAC = 8

def generate_animals(connection, cursor):
    fake = Faker()#['ru_RU'])
    f = Faker()
    id = 0
    for i in range(200): #len(animal_name_m) 
        print(i)
        id += 1
        name = animal_name_m[i]
        sex = "м"
        age = randint(1, 20)
        history = "history"
        if (id % 2 == 0):
            breed = breed_dog[randint(0, BREED_DOG - 1)]
            animal = Animals('dog')
            type = 'dog'
            img = animal.image()
        else:
            breed = breed_cat[randint(0, BREED_CAT - 1)]
            animal = Animals('cat')
            type = 'cat'
            img = animal.image()
        flag = 0
        sql_insert = f"""INSERT INTO animal (animal_id, animal_type, animal_name, animal_sex, animal_age, animal_history, animal_breed, animal_img, delete_flag) 
                         VALUES ({id}, \'{type}\', \'{name}\', \'{sex}\', {age}, \'{history}\', \'{breed}\', \'{img}\',  \'{flag}\');"""
        cursor.execute(sql_insert)
        connection.commit()


    for i in range(200): #len(animal_name_w)
        print(i)
        id += 1
        name = animal_name_w[i]
        sex = "ж"
        age = randint(1, 20)
        history = "history"
        if (id % 2 == 0):
            breed = breed_dog[randint(0, BREED_DOG - 1)]
            animal = Animals('dog')
            type = 'dog'
            img = animal.image()
        else:
            breed = breed_cat[randint(0, BREED_CAT - 1)]
            animal = Animals('cat')
            type = 'cat'
            img = animal.image()
        flag = 0
        sql_insert = f"""INSERT INTO animal (animal_id, animal_type, animal_name, animal_sex, animal_age, animal_history, animal_breed, animal_img, delete_flag) 
                         VALUES ({id}, \'{type}\', \'{name}\', \'{sex}\', {age}, \'{history}\', \'{breed}\', \'{img}\',  \'{flag}\');"""
        cursor.execute(sql_insert)
        connection.commit()


def generate_vaccination(connection, cursor):
    for i in range(VACCINATIONS):
        name = vaccination[i]
        sql_insert = f"""INSERT INTO vaccination (vaccinatiоn_id, vaccinatiоn_name) 
                         VALUES ({i+1}, \'{name}\');"""
        cursor.execute(sql_insert)
        connection.commit()


def generate_animal_x_vaccination(connection, cursor):
    fake = Faker(['ru_RU'])
    for i in range(ANIMAL_X_VACCINETION):
        animal_id = randint(1, 400) #ANIMALS
        if (animal_id % 2 == 0):
            vac_id = randint(1, DOG_VAC)
        else:
            vac_id = randint(CAT_VAC, VACCINATIONS)
        date = str(fake.date_this_decade())
        sql_insert = f"""INSERT INTO animal_x_vaccination (an_x_vac_id, animal_id, vaccination_id, vaccination_date) 
                         VALUES ({i+1}, {animal_id}, {vac_id}, \'{date}\');"""
        cursor.execute(sql_insert)
        connection.commit()


def generate_message(connection, cursor):
    fake = Faker(['ru_RU'])
    for i in range(MESSAGE):
        name = fake.name()
        phone = '+7'
        for j in range(10):
            phone += str(randint(0, 9))
        email = fake.email()
        text = "text"
        pre = choice(['телефон', 'email'])
        flag = 0
        sql_insert = f"""INSERT INTO message (message_id, message_name, phone, email, message_text, preferred_contact_method, answer_flag) 
                         VALUES ({i+1}, \'{name}\', \'{phone}\', \'{email}\', \'{text}\', \'{pre}\', \'{flag}\');"""
        cursor.execute(sql_insert)
        connection.commit()


def generate_info_shelter(connection, cursor):
    fake = Faker(['ru_RU'])
    address = "Любовь, улица Надежды, доп Доброты"
    phone = "+7-895-923-25-54"
    email = "iva@iva.shelter.com"
    sql_insert = f"""INSERT INTO info_shelter (shelter_address, shelter_phone, shelter_email) 
                        VALUES (\'{address}\', \'{phone}\', \'{email}\');"""
    cursor.execute(sql_insert)
    connection.commit()


def generate_dict_privilege(connection, cursor):
    fake = Faker(['ru_RU'])
    for i in range(len(PRIVILEGE)):
        sql_insert = f"""INSERT INTO dict_privilege (priv_id, priv_name) 
                         VALUES (\'{i + 1}\', \'{PRIVILEGE[i]}\');"""
        cursor.execute(sql_insert)
        connection.commit()


def generate_user_shelter(connection, cursor):
    chars=string.ascii_uppercase + string.digits
    fake = Faker(['ru_RU'])
    for i in range(USER):
        name = fake.name()
        login = fake.email()
        login = login.partition('@')[0] + "@iva.shelter.com"
        check = ''.join(choice(chars) for _ in range(10))
        priv = choice([i + 1 for i in range(len(PRIVILEGE))])
        sql_insert = f"""INSERT INTO user_shelter (user_id, user_fio, user_login, user_check, user_privilege) 
                         VALUES ({i + 1}, \'{name}\', \'{login}\', \'{check}\', {priv});"""
        cursor.execute(sql_insert)
        connection.commit()

def main_fun():
    # try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(database="shelter_db",
                                    user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="1234",
                                    host="127.0.0.1",
                                    port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()

    generate_animals(connection, cursor)
    print('1')
    generate_vaccination(connection, cursor)
    print('2')
    generate_animal_x_vaccination(connection, cursor)
    print('3')
    generate_message(connection, cursor)
    print('4')
    generate_info_shelter(connection, cursor)
    print('5')
    generate_dict_privilege(connection, cursor)
    print('6')
    generate_user_shelter(connection, cursor)
    print('7')




    # except (Exception, Error) as error:
    #     print("Ошибка при работе с PostgreSQL", error)



main_fun()


