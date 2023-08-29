import argparse

import database
import list as l
import add as a
import clear as c


database.initialize_database()

def main():
    parser = argparse.ArgumentParser(description="A simple to-do list manager.")

    parser.add_argument("-a", "--add", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List tasks")
    parser.add_argument("-c", "--clear", action="store_true", help="Clears new tasks")

    args = parser.parse_args()

    if args.add:
        task_name = args.add
        print(f"Adding task: {task_name}")
        a.add(task_name)

    if args.list:
        l.list()

    if args.clear:
        c.clear()
        print(f"New records cleared")

if __name__ == "__main__":
    main()