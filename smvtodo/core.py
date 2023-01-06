"""
Smvtodo is a project for managing productivity todo-lists in the
terminal using SQL and Python
Copyright (C) 2023-present Achyuth Jayadevan
Copyright (C) 2023-present Adharve N.A
"""
import sqlite3
import sys


def get_connection():
    """
    This function is used to return a connection object
    and then print a success message

    Returns:
        Connection: Connection object for the database
    """
    con = sqlite3.connect("todo-database.db")
    print("Connection has been created", end="\n\n")
    return con


def create_table_if_not_exists(cursor):
    """
    This is function is used to create the todo_table if it does
    not exist already, this is necessary if the program is running for the first time.
    """
    query = """CREATE TABLE IF NOT EXISTS todo_table
                (   id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    description UNIQUE
                );
            """
    cursor.execute(query)


def get_int_input(prompt):
    """
    This function is used to get a validated integer input from the user

    Args:
        prompt (str): a string prompt that should be displayed to the user

    Returns:
        int: integer output that was given by the user
    """
    while True:
        user_input = input(prompt)
        if not user_input.isnumeric():
            print("Please enter an valid integer")
        else:
            return int(user_input)


def get_confirmation(prompt):
    """
    Get confirmation from the user about a action
    this is done by asking the user yes or no question and then returning a
    corresponding boolean value, the inputs are validated

    Args:
        prompt (str): a string prompt that should be displayed to the user

    Returns:
        bool: True for yes, False for no
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in ["y", "yes"]:
            return True
        if user_input in ["n", "no"]:
            return False
        print("Please enter 'yes' or 'no', or abbreviate it as 'y' or 'n'")


def show_help_page(cursor=None):
    """
    Display help message for the user for an friendly interface
    providing cursor for this function is optional, process_choice may invoke
    this function with cursor as a positional argument
    """
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
    """
    Insert new records into the database
    """
    task = input("Enter the task that should be done >")
    cursor.execute("INSERT INTO todo_table (description) VALUES (?);", (task,))
    print("Task has been sucessfully inserted")


def delete_existing_record(cursor):
    """
    Delete an existing record in the database by referencing it's ID
    """
    record_id = get_int_input("Enter the record identity that should be deleted >")
    cursor.execute("DELETE FROM todo_table WHERE id = ?;", (record_id,))
    print("Task has been successfully deleted")


def modify_existing_record(cursor):
    """
    Modify an existing record in the database by referencing it's ID
    """
    record_id = get_int_input("Enter the record identity that should be deleted >")
    task = input("Enter the task that should be done >")
    query = """
    UPDATE todo_table
    SET description = ?
    WHERE id = ?;
    """
    cursor.execute(query, (task, record_id))


def display_all_todo_tasks(cursor):
    """
    Display all the todos that has been registered in the database
    """
    query = "SELECT id, description FROM todo_table;"
    records = cursor.execute(query).fetchall()
    print(records)


def clear_table(cursor):
    """
    Clear the database table and create a new tabe
    """
    prompt = "Are you sure you want to delete all the records? [yes / no] >"
    if get_confirmation(prompt):
        cursor.execute("DROP TABLE todo_table;")
        create_table_if_not_exists(cursor)
        print("All the values in the table have been reset")


def exit_app(cursor):
    """
    Exit the app and display credits
    """
    cursor.close()
    print("Thank you for using our app")
    print("Made by Achyuth Jayadevan and Adharve N.A")
    sys.exit()


def process_choice(choice, cursor):
    """
    Processes the choice the user has entered
    this is done by creating a mapping between the choices and the corresponding function
    and then calling the function with the cursor object

    Args:
        choice (int): the choice the user has made
        cursor (Cursor): the cursor object to execute queries
    """
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
    """
    Starts the application by creating tables and manual
    then proceeds to continously process commands

    Args:
        cursor (Cursor): Cursor object that has been initialized
    """
    create_table_if_not_exists(cursor)
    show_help_page(cursor)
    while True:
        choice = get_int_input("Enter your choice >")
        process_choice(choice, cursor)
        cursor.connection.commit()
        print()


def run_app():
    """
    Main entry point for the program, runs necessary prerequisites and
    starts the application
    """
    connection = get_connection()
    cursor = connection.cursor()
    start_application(cursor)


if __name__ == "__main__":
    run_app()
