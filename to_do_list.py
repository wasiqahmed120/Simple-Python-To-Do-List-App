import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, index):
        try:
            removed = self.tasks.pop(index)
            print(f"Task removed: {removed}")
        except IndexError:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def save_tasks(self, filename="todo_list.txt"):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        print("Tasks saved.")

    def load_tasks(self, filename="todo_list.txt"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.tasks = [task.strip() for task in file.readlines()]
            print("Tasks loaded.")
        else:
            print("No saved tasks found.")

if __name__ == "__main__":
    todo = ToDoList()
    todo.load_tasks()

    while True:
        print("\nOptions: add, remove, list, save, exit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "add":
            task = input("Enter a task: ")
            todo.add_task(task)

        elif choice == "remove":
            try:
                index = int(input("Enter task number to remove: ")) - 1
                todo.remove_task(index)
            except ValueError:
                print("Invalid input. Enter a number.")

        elif choice == "list":
            todo.list_tasks()

        elif choice == "save":
            todo.save_tasks()

        elif choice == "exit":
            todo.save_tasks()
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")
