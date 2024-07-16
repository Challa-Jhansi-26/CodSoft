# Simple To-Do List Application

# Initialize an empty to-do list
to_do_list = []

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_list():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    to_do_list.append(task)
    print("Task added.")

def update_task():
    view_list()
    task_num = int(input("Enter the task number to update: "))
    if 1 <= task_num <= len(to_do_list):
        new_task = input("Enter the new task: ")
        to_do_list[task_num - 1] = new_task
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task():
    view_list()
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(to_do_list):
        to_do_list.pop(task_num - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
