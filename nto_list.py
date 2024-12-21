import os

# define a load function
def load_task():
    if os.path.exists("rate.txt") :
        with open("rate.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    else:
        return []


def save_task(tasks):
    with open("rate.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def display():
    print("\n To-do-list")
    print("1. to view")
    print("2. to Add")
    print("3. to Remove")
    print("4. to exit")


def view_task(tasks):
    if tasks:
        print("\n Your task:")
        for i,task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\n No task Available")


def add_task(tasks):
    task = input("Add a task:  ")
    tasks.append(task)
    save_task(tasks)
    print(f"\n You added '{task}'")


def remove_task(tasks):
    try:
        task_number = int(input("Enter the number you want to remove: "))
        if 1 <= task_number <= len(tasks):
            remove_task = tasks.pop(task_number - 1)
            save_task(tasks)
            print(f"Your task {remove_task} as been removed")
        else:
            print("The number is not in the range of removed list")
    except ValueError:
        print("this not a number")


def main():
    task = load_task()
    while True:
        display()
        choice = input("Enter number btw 1-4: ")

        if choice == "1":
            view_task(task)
        elif choice == "2":
            add_task(task)
        elif choice == "3":
            remove_task(task)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("invalid number")



if __name__ == "__main__":
    main()

