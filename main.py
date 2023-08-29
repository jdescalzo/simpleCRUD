import argparse

import database
import queries as q


database.initialize_database()

def main():
    parser = argparse.ArgumentParser(description="A simple to-do list manager.")

    parser.add_argument("-a", "--add", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List tasks")
    parser.add_argument("-c", "--clear", action="store_true", help="Clears new tasks")

    args = parser.parse_args()

    if args.add:
        task_name = args.add
        q.add(task_name)

    if args.list:
        q.list()

    if args.clear:
        q.clear()

if __name__ == "__main__":
    main()