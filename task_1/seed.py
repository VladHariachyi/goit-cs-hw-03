from psycopg import Error
import faker
from random import randint


NUMBER_USERS = 30
NUMBER_TASKS = 60
STATUSSES = [('new',), ('in progress',), ('completed',)]


def insert_satuses_to_db(connection):
    sql_to_statuses = """
        INSERT INTO status(name)
        VALUES (%s)
    """
    cursor = connection.cursor()

    try:
        for status in STATUSSES:
            cursor.execute(sql_to_statuses, status)
            connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()

def insert_users_to_db(connection):
    users = []
    fake_data = faker.Faker()

    for _ in range(NUMBER_USERS):
        users.append((
            fake_data.name(),
            fake_data.email(),
        ))

    sql_to_users = """
        INSERT INTO users(fullname, email)
        VALUES (%s, %s)
    """
    cursor = connection.cursor()

    try:
        for user in users:
            cursor.execute(sql_to_users, user)
            connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()

def insert_tasks_to_db(connection):
    tasks = []
    fake_data = faker.Faker()

    for _ in range(NUMBER_TASKS):
        tasks.append((
            fake_data.sentence(nb_words=5),
            fake_data.paragraph(nb_sentences=1),
            randint(1, len(STATUSSES)),
            randint(1, NUMBER_USERS),
        ))


    sql_to_taks = """
        INSERT INTO tasks(title, description, status_id, user_id)
        VALUES (%s, %s, %s, %s)
    """
    cursor = connection.cursor()

    try:
        for task in tasks:
            cursor.execute(sql_to_taks, task)
            connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()


def insert_data_to_db(connection):
    insert_satuses_to_db(connection)
    insert_users_to_db(connection)
    insert_tasks_to_db(connection)