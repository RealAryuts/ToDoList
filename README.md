# ToDoList

I made a simple to-do list program in Python that runs in the terminal. Instead of just listing tasks, it lets you put an expected finish time for each task and tells you if you finished it on time or late when you check it off. I also packed it into a Windows `.exe` so you can run it without installing Python.

## What it can do

- Add a task with an expected date and time
- View all your pending and finished tasks
- Mark tasks as done (it checks the current time and tells you if you were on time or late)
- Delete tasks you dont need anymore
- Uses colored text in the terminal so pending, done, and late tasks stand out
- Saves your tasks automatically to a `tasks.json` file so nothing gets lost when you close it

## How to use it

You can either run the `.exe` directly or run the Python file.

### Using the .exe (Windows)
1. Download `todo.exe` from this repo (or from the Releases page).
2. Double click it to open in the terminal.
3. Type a number from 1 to 5 to pick what you want to do.

### Using Python
If you have Python 3 installed, just run:

```bash
python todo.py
```

When adding a task, type the expected time like `YYYY-MM-DD HH:MM` (for example `2026-11-24 18:30`). If you mess up the format it just asks you again.

## What it looks like

```text
--- Your To-Do List ---
1. [Done] Finish math homework
   Expected:  2026-11-24 23:59
   Completed: 2026-11-24 19:10 (On time)
2. [Pending] Clean desk
   Expected:  2026-11-25 18:00
```

## Notes

- Doesnt need any external libraries, only built-in Python stuff (`json`, `os`, `sys`, `datetime`).
- `todo.exe` was made with PyInstaller, and `tasks.json` gets created in the same folder automatically.
