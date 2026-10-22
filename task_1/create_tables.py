from psycopg import Error, sql


sql_create_status_table = """
create table status (
    id serial primary key,
    name varchar(50) unique
)
"""

sql_create_users_table = """
create table users (
    id serial primary key,
    fullname varchar(100),
    email varchar(100) unique
)
"""

sql_create_tasks_table = """
create table tasks (
    id serial primary key,
    title varchar(100),
    description text,
    status_id int,
    user_id int,
    foreign key (status_id) references status (id) 
        on delete cascade
        on update cascade,
    foreign key (user_id) references users (id) 
        on delete cascade 
        on update cascade
)
"""

def drop_table(connection, table_name):
    try:
        cursor = connection.cursor()
        query = sql.SQL("drop table if exists {}").format(
            sql.Identifier(table_name)
        )
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(e)

def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
    except Error as e:
        print(e)


def intitialize_tables(connection):
    drop_table(connection, "tasks")
    drop_table(connection, "status")
    drop_table(connection, "users")
    print("Tables are droped")

    create_table(connection, sql_create_users_table)
    create_table(connection, sql_create_status_table)
    create_table(connection, sql_create_tasks_table)
    print("Tables are created")
