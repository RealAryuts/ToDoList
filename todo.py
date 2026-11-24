import json
import os
import sys
from datetime import datetime

os.system("")

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE = os.path.join(BASE_DIR, "tasks.json")
FMT = "%Y-%m-%d %H:%M"


def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print(YELLOW + "\nNo tasks yet." + RESET)
        return

    print(CYAN + "\n--- Your To-Do List ---" + RESET)
    for i, t in enumerate(tasks, 1):
        if t["done"]:
            status = GREEN + "[Done]" + RESET
        else:
            status = YELLOW + "[Pending]" + RESET

        print(f"{i}. {status} {t['name']}")
        print(f"   Expected:  {t['expected']}")

        if t["done"]:
            col = GREEN if t["result"] == "On time" else RED
            print(f"   Completed: {t['completed']} ({col}{t['result']}{RESET})")
    print()


def add_task(tasks):
    name = input("Task: ").strip()
    if not name:
        print(RED + "Task can't be empty." + RESET)
        return

    # get expected finish date/time
    while True:
        exp = input("Expected finish (YYYY-MM-DD HH:MM): ").strip()
        try:
            datetime.strptime(exp, FMT)
            break
        except ValueError:
            print(RED + "Wrong format, try like 2026-11-24 18:30" + RESET)

    tasks.append({
        "name": name,
        "expected": exp,
        "done": False,
        "completed": None,
        "result": None
    })
    save_tasks(tasks)
    print(GREEN + "Task added!" + RESET)


def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    num = input("Enter task num to mark done: ").strip()
    if not num.isdigit():
        print(RED + "Enter a valid number." + RESET)
        return

    idx = int(num) - 1
    if idx < 0 or idx >= len(tasks):
        print(RED + "Task not found." + RESET)
        return

    if tasks[idx]["done"]:
        print(YELLOW + "Already marked done." + RESET)
        return

    now = datetime.now()
    exp = datetime.strptime(tasks[idx]["expected"], FMT)

    # chk if on time or late
    if now <= exp:
        res = "On time"
        col = GREEN
    else:
        res = "Late"
        col = RED

    tasks[idx]["done"] = True
    tasks[idx]["completed"] = now.strftime(FMT)
    tasks[idx]["result"] = res
    save_tasks(tasks)
    print(f"Marked done! ({col}{res}{RESET})")


def del_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    num = input("Enter task num to delete: ").strip()
    if not num.isdigit():
        print(RED + "Enter a valid number." + RESET)
        return

    idx = int(num) - 1
    if idx < 0 or idx >= len(tasks):
        print(RED + "Task not found." + RESET)
        return

    removed = tasks.pop(idx)
    save_tasks(tasks)
    print(YELLOW + f"Deleted: {removed['name']}" + RESET)


tasks = load_tasks()

while True:
    print(CYAN + "\n1. View tasks")
    print("2. Add task")
    print("3. Mark task done")
    print("4. Delete task")
    print("5. Exit" + RESET)

    ch = input("Choose (1-5): ").strip()

    if ch == "1":
        show_tasks(tasks)
    elif ch == "2":
        add_task(tasks)
    elif ch == "3":
        mark_done(tasks)
    elif ch == "4":
        del_task(tasks)
    elif ch == "5":
        print(CYAN + "Bye!" + RESET)
        break
    else:
        print(RED + "Invalid option." + RESET)
