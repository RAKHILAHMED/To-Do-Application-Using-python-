class ToDoApp:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Incomplete"
                print(f'{i + 1}. {task["description"]} - {status}')

    def add_task(self, task_description):
        self.tasks.append({"description": task_description, "completed": False})
        print(f'Task "{task_description}" added.')

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f'Task "{self.tasks[task_index]["description"]}" marked as completed.')
        else:
            print("Invalid task number.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f'Task "{removed_task["description"]}" removed.')
        else:
            print("Invalid task number.")

def main():
    todo_app = ToDoApp()

    while True:
        print("\nTo-Do Application Menu:")
        print("1. Display To-Do List")
        print("2. Add a new task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_app.display_tasks()
        elif choice == "2":
            task_description = input("Enter task description: ")
            todo_app.add_task(task_description)
        elif choice == "3":
            todo_app.display_tasks()
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_app.complete_task(task_index)
        elif choice == "4":
            todo_app.display_tasks()
            task_index = int(input("Enter the task number to remove: ")) - 1
            todo_app.remove_task(task_index)
        elif choice == "5":
            print("Exiting To-Do Application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
