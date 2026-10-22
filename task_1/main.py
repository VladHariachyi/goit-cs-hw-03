from psycopg import Error

from connect import create_connection
from create_tables import intitialize_tables
from seed import insert_data_to_db


def task_1(connection, user_id):
    rows = None
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
        rows = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()

    return rows

def task_2(connection, status):
    rows = None
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT * FROM tasks WHERE status_id IN 
            (SELECT id FROM status WHERE name = %s)""", 
            (status,)
        )
        rows = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()

    return rows

def task_3(connection, task_id, status):
    cursor = connection.cursor()

    try:
        cursor.execute("""
            UPDATE tasks SET status_id = %s
            WHERE id = %s""", 
            (status, task_id, )
        )
        connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()


def task_4(connection):
    rows = None
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT * FROM users WHERE id NOT IN 
            (SELECT user_id FROM tasks)""", 
        )
        rows = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()

    return rows  


def task_5(connection, task):
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO tasks (title, description, status_id, user_id)
            VALUES (%s, %s, %s, %s)
            """, 
            task
        )
        connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()


def task_6(connection):
    rows = None
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT * FROM tasks WHERE status_id !=
            (SELECT id FROM status WHERE name = 'completed')""", 
        )
        rows = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()

    return rows

def task_7(connection, task_id):
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()

def task_8(connection, domain):
    rows = None
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE email LIKE %s", (f"%.{domain}",))
        rows = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()

    return rows

def task_9(connection, user_id, user_name):
    cursor = connection.cursor()

    try:
        cursor.execute("""
            UPDATE users SET fullname = %s
            WHERE id = %s""", 
            (user_name, user_id, )
        )
        connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()

def task_10(connection):
    rows = None
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT COUNT(t.id) as total_tasks, s.name AS status
            FROM tasks AS t 
            LEFT JOIN status AS s ON s.id = t.status_id 
            GROUP BY s.name 
        """)
        rows = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()

    return rows


def task_11(connection, domain):
    rows = None
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT t.title AS title, t.description AS description, u.fullname AS user_name, u.email AS email
            FROM tasks AS t 
            LEFT JOIN users AS u ON u.id = t.user_id 
            WHERE email LIKE %s
        """, (f"%.{domain}",) )
        rows = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()

    return rows

def task_12(connection):
    rows = None
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM tasks WHERE description = '' OR description IS NULL")
        rows = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()

    return rows

def task_13(connection):
    rows = None
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT t.title, t.description, t.status_id, u.fullname, u.email FROM tasks as t 
            INNER JOIN users AS u ON u.id = t.user_id 
            WHERE t.status_id =
            (SELECT id FROM status WHERE name = 'in progress')
        """,)
        rows = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()

    return rows

def task_14(connection):
    rows = None
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT COUNT(t.id) as total_tasks, u.fullname AS user_name
            FROM tasks AS t 
            LEFT JOIN users AS u ON u.id = t.user_id 
            GROUP BY u.fullname 
        """)
        rows = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()

    return rows

if __name__ == "__main__":
    with create_connection() as connection:
        if connection is not None:
            # Re-creates tables, re-fill data (Call one time) 
            intitialize_tables(connection)
            insert_data_to_db(connection)

            # Tasks
            print(f"Task 1")
            print(f"{task_1(connection, 5)}\n")

            print(f"Task 2")
            print(f"{task_2(connection, "in progress")}\n")

            task_3(connection, 1, 3)

            print(f"Task 4")
            print(f"{task_4(connection)}\n")

            print(f"Task 5")
            task_5(connection, ("Some task", "Some description", 2, 1))

            print(f"Task 6")
            print(f"{task_6(connection)}\n")

            task_7(connection, 2)

            print(f"Task 8")
            print(f"{task_8(connection, "com")}\n")

            task_9(connection, 1, "John Doe")

            print(f"Task 10")
            print(f"{task_10(connection)}\n")

            print(f"Task 11")
            print(f"{task_11(connection, "net")}\n")

            print(f"Task 12")
            print(f"{task_12(connection)}\n")

            print(f"Task 13")
            print(f"{task_13(connection)}\n")

            print(f"Task 14")
            print(f"{task_14(connection)}\n")
        else:
            print("Error - Cannot connect to database")