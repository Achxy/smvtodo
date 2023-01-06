# [`Smvtodo`](https://github.com/Achxy/smvtodo)
An TODO app made for school project - SMV

# Summary
Smvtodo is an application for managing productivity tasks in the terminal using python and SQL.
We use `sqlite3` from the standard library of python to establish a connection between python and the local database created in the file system.

For the first launch of the application we ensure that the `todo_table` relation is created by the python integration using the `create_table_if_not_exists` function, for every subsequent launch afterwards the aforementioned function does not perform any additional operation. Furthermore, we want the ID of each record to be the `PRIMARY KEY`, and be automatically incremented, as such, the following query is used to create the table structure:

```js
CREATE TABLE IF NOT EXISTS todo_table
    (   id          INTEGER PRIMARY KEY AUTOINCREMENT,
        description UNIQUE
    );
```

Proceeding, we ask the end-user for the actions that they want to perform, such as
- Adding new task
- Deleting an existing task
- Modifying an task
- Displaying all the tasks that need to be completed
- Clearing / Dropping the table of tasks
- Accessing the manual / help page
- Gracefully exiting the application


After receving the user's choice made through the terminal using the python's builtin `input` function we then advance towards registering the changes in the database by executing the relevant and corresponding queries from the cursor.

