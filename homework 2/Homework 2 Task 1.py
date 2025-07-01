# Homework 2
# @Author  : Haixiang Yu

# List to store tasks
todo_list = []

def d_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour to-do list:")
        for index, task in enumerate(todo_list, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{index}. [{status}] {task['task']}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added.")

def mark_completed():
    d_tasks()
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task():
    d_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task '{removed['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Quit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            d_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Wrong. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
