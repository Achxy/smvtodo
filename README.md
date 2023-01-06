# [`Smvtodo`](https://github.com/Achxy/smvtodo)
An TODO app made for school project - SMV

# Summary
Smvtodo is an application for managing productivity tasks in the terminal using python and SQL.
We use `sqlite3` from the standard library of python to establish a connection between python and the local database created in the file system.

For the first launch of the application we ensure that the `todo_table` relation is created by the python integration using the `create_table_if_not_exists` function, for every subsequent launch afterwards the aforementioned function does not perform any additional operation

Proceeding, we ask the end-user for the actions that they want to perform, such as
- Adding new task
- Deleting an existing task
- Modifying an task
- Displaying all the tasks that need to be completed
- Clearing / Dropping the table of tasks
- Accessing the manual / help page
- Gracefully exiting the application

