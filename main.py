import argparse
import database
import queries as q


database.initialize_database()

def main():
    parser = argparse.ArgumentParser(description="A simple to-do list manager.")

    parser.add_argument("-a", "--add", nargs=3, help="Add a new task: ID, Task Name, Due Date")
    parser.add_argument("-l", "--list", action="store_true", help="List tasks")
    parser.add_argument("-k", "--clear", action="store_true", help="Clears new tasks")
    parser.add_argument("-c", "--complete", help="Completes specified task")

    args = parser.parse_args()

    if args.add:
        task = args.add
        q.add(task)

    if args.list:
        q.list()

    if args.clear:
        q.clear()

    if args.complete:
        task = args.complete
        q.complete(task)

if __name__ == "__main__":
    main()