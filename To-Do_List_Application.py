class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def complete_task(self, task_index):
        if task_index < 1 or task_index > len(self.tasks):
            print("Invalid task index>")
        else:
            completed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{completed_task}' marked as completed.")

#ToDoList Class
todo_list = ToDoList()

#Loop Created
while True:
    print("\n===== To-Do List Application =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice =="1":
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == "2":
        todo_list.add_task()
    elif choice == "3":
        task_index = int(input("Enter the task index: "))
        todo_list.complete_task(task_index)
    elif choice == "4":
        print("Thank you for using the to-do list application. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
