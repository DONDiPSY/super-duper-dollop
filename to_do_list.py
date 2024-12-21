import os


# Function to load tasks from the file


def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    else:
        return []


# Function to save tasks to the file


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Function to display the menu


def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")


# Function to view tasks


def view_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks available.")


# Function to add a task


def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")


# Function to remove a task


def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main function


def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("\nChoose an option (1/2/3/4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# I don't understand this
if __name__ == "__main__":
    main()

# enumerate , with
