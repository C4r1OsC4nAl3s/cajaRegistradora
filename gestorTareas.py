class Task:
    def __init__(self, title, due_date, priority):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔️" if self.completed else "❌"
        return f"[{status}] {self.title} (Due: {self.due_date}, Priority: {self.priority})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date, priority):
        new_task = Task(title, due_date, priority)
        self.tasks.append(new_task)
        print(f'Task "{title}" added.')

    def update_task(self, task_index, title=None, due_date=None, priority=None):
        try:
            task = self.tasks[task_index]
            if title:
                task.title = title
            if due_date:
                task.due_date = due_date
            if priority:
                task.priority = priority
            print(f'Task "{task.title}" updated.')
        except IndexError:
            print("Task not found.")

    def delete_task(self, task_index):
        try:
            removed_task = self.tasks.pop(task_index)
            print(f'Task "{removed_task.title}" deleted.')
        except IndexError:
            print("Task not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High/Medium/Low): ")
            task_manager.add_task(title, due_date, priority)

        elif choice == '2':
            task_index = int(input("Enter task index to update: "))
            title = input("Enter new task title (leave blank to keep current): ")
            due_date = input("Enter new due date (leave blank to keep current): ")
            priority = input("Enter new priority (leave blank to keep current): ")
            task_manager.update_task(task_index, title or None, due_date or None, priority or None)

        elif choice == '3':
            task_index = int(input("Enter task index to delete: "))
            task_manager.delete_task(task_index)

        elif choice == '4':
            task_manager.list_tasks()

        elif choice == '5':
            task_index = int(input("Enter task index to mark as completed: "))
            try:
                task_manager.tasks[task_index].mark_completed()
                print("Task marked as completed.")
            except IndexError:
                print("Task not found.")

        elif choice == '6':
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
