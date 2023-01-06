"""
Smvtodo is a project for managing productivity todo-lists in the
terminal using SQL and Python
Copyright (C) 2023-present Achyuth Jayadevan
Copyright (C) 2023-present Adharve N.A
"""
import sqlite3
import sys


def get_connection():
    con = sqlite3.connect("todo-database.db")
    print("Connection has been created", end="\n\n")
    return con


def create_table_if_not_exists(cursor: sqlite3.Cursor):
    query = """CREATE TABLE IF NOT EXISTS todo_table
                (   id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    description UNIQUE
                );
            """
    cursor.execute(query)


def get_int_input(prompt):
    while True:
        user_input = input(prompt)
        if not user_input.isnumeric():
            print("Please enter an valid integer")
        return int(user_input)


def get_confirmation(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ["y", "yes"]:
            return True
        elif user_input in ["n", "no"]:
            return False
        else:
            print("Please enter 'yes' or 'no', or abbreviate it as 'y' or 'n'")


def show_help_page(cursor=None):
    info = """
    1 - INSERT NEW RECORD
    2 - DELETE RECORD
    3 - MODIFY EXISTING RECORD
    4 - DISPLAY ALL TODO TASKS
    5 - CLEAR TABLE
    6 - SHOW HELP PAGE
    7 - EXIT
    """
    print(info)


def insert_new_record(cursor):
    task = input("Enter the task that should be done >")
    cursor.execute("INSERT INTO todo_table (description) VALUES (?);", (task,))
    print("Task has been sucessfully inserted")


def delete_existing_record(cursor):
    record_id = get_int_input("Enter the record identity that should be deleted >")
    cursor.execute("DELETE FROM todo_table WHERE id = ?;", (record_id,))
    print("Task has been successfully deleted")


def modify_existing_record(cursor):
    record_id = get_int_input("Enter the record identity that should be deleted >")
    task = input("Enter the task that should be done >")
    query = """
    UPDATE todo_table
    SET description = ?
    WHERE id = ?;
    """
    cursor.execute(query, (task, record_id))


def display_all_todo_tasks(cursor):
    query = "SELECT id, description FROM todo_table;"
    records = cursor.execute(query).fetchall()
    print(records)


def clear_table(cursor):
    prompt = "Are you sure you want to delete all the records? [yes / no] >"
    if get_confirmation(prompt):
        cursor.execute("DROP TABLE todo_table;")
        create_table_if_not_exists(cursor)
        print("All the values in the table have been reset")


def exit_app(cursor):
    cursor.close()
    print("Thank you for using our app")
    print("Made by Achyuth Jayadevan and Adharve N.A")
    sys.exit()


def process_choice(choice, cursor):
    if choice not in range(1, 8):
        print("choice must be within ranges of 1 to 7 inclusive")
    choices = {
        1: insert_new_record,
        2: delete_existing_record,
        3: modify_existing_record,
        4: display_all_todo_tasks,
        5: clear_table,
        6: show_help_page,
        7: exit_app,
    }
    function = choices[choice]
    function(cursor)


def start_application(cursor):
    create_table_if_not_exists(cursor)
    show_help_page(cursor)
    while True:
        choice = get_int_input("Enter your choice >")
        process_choice(choice, cursor)
        cursor.connection.commit()
        print()


def run_app():
    connection = get_connection()
    cursor = connection.cursor()
    start_application(cursor)


if __name__ == "__main__":
    run_app()
