import uuid
import json
from datetime import datetime

# A list to store the tasks
task_list = []

# Function to generate a unique ID for each task
def generate_task_id():
    return str(uuid.uuid4())

# Function to add a task
def add_task(description, priority='Medium', category=None, due_date=None):
    task = {
        'id': generate_task_id(),
        'description': description,
        'status': 'Pending',
        'priority': priority,
        'category': category,
        'due_date': due_date
    }
    task_list.append(task)
    print(f"Task '{description}' added successfully!")

# Function to remove a task by its ID
def remove_task(task_id):
    global task_list
    task_list = [task for task in task_list if task['id'] != task_id]
    print(f"Task with ID '{task_id}' removed successfully!")

# Function to mark a task as complete
def mark_complete(task_id):
    for task in task_list:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            print(f"Task '{task['description']}' marked as completed!")
            return
    print(f"Task with ID '{task_id}' not found!")

# Function to edit a task's description
def edit_task(task_id, new_description):
    for task in task_list:
        if task['id'] == task_id:
            task['description'] = new_description
            print(f"Task with ID '{task_id}' updated to: '{new_description}'")
            return
    print(f"Task with ID '{task_id}' not found!")

# Function to set due date for a task
def set_due_date(task_id, due_date):
    for task in task_list:
        if task['id'] == task_id:
            task['due_date'] = due_date
            print(f"Due date for task '{task['description']}' set to {due_date}")
            return
    print(f"Task with ID '{task_id}' not found!")

# Function to prioritize a task
def prioritize_task(task_id, priority):
    for task in task_list:
        if task['id'] == task_id:
            task['priority'] = priority
            print(f"Priority of task '{task['description']}' set to {priority}")
            return
    print(f"Task with ID '{task_id}' not found!")

# Function to categorize a task
def categorize_task(task_id, category):
    for task in task_list:
        if task['id'] == task_id:
            task['category'] = category
            print(f"Task '{task['description']}' categorized as {category}")
            return
    print(f"Task with ID '{task_id}' not found!")

# Function to search tasks based on a keyword
def search_task(keyword):
    found_tasks = [task for task in task_list if keyword.lower() in task['description'].lower()]
    if found_tasks:
        for task in found_tasks:
            print(f"Found task: {task['description']} - Status: {task['status']}")
    else:
        print(f"No tasks found for keyword '{keyword}'")

# Function to sort tasks by priority
def sort_tasks_by_priority():
    sorted_tasks = sorted(task_list, key=lambda x: x['priority'])
    for task in sorted_tasks:
        print(f"Task: {task['description']} - Priority: {task['priority']}")

# Function to filter tasks by status
def filter_tasks_by_status(status):
    filtered_tasks = [task for task in task_list if task['status'].lower() == status.lower()]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"Task: {task['description']} - Status: {task['status']}")
    else:
        print(f"No tasks with status '{status}'")

# Function to display statistics on tasks
def task_statistics():
    total_tasks = len(task_list)
    completed_tasks = len([task for task in task_list if task['status'] == 'Completed'])
    pending_tasks = total_tasks - completed_tasks
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")

# Function to import tasks from a JSON file
def import_tasks_from_file(filename):
    global task_list
    try:
        with open(filename, 'r') as file:
            task_list = json.load(file)
        print(f"Tasks imported from {filename} successfully!")
    except FileNotFoundError:
        print(f"File {filename} not found!")

# Function to export tasks to a JSON file
def export_tasks_to_file(filename):
    with open(filename, 'w') as file:
        json.dump(task_list, file, indent=4)
    print(f"Tasks exported to {filename} successfully!")

# Function to display all tasks
def view_tasks():
    if task_list:
        for task in task_list:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Priority: {task['priority']}, Category: {task['category']}, Due Date: {task['due_date']}")
    else:
        print("No tasks available!")

# Main loop to interact with the user
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. Edit Task")
        print("5. Set Due Date")
        print("6. Prioritize Task")
        print("7. Categorize Task")
        print("8. View Tasks")
        print("9. Search Task")
        print("10. Sort Tasks by Priority")
        print("11. Filter Tasks by Status")
        print("12. View Statistics")
        print("13. Import Tasks from File")
        print("14. Export Tasks to File")
        print("15. Exit")

        choice = input("Choose an option (1-15): ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter priority (Low, Medium, High): ")
            category = input("Enter category (optional): ") or None
            due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ") or None
            add_task(description, priority, category, due_date)
        elif choice == '2':
            task_id = input("Enter task ID to remove: ")
            remove_task(task_id)
        elif choice == '3':
            task_id = input("Enter task ID to mark as complete: ")
            mark_complete(task_id)
        elif choice == '4':
            task_id = input("Enter task ID to edit: ")
            new_description = input("Enter new task description: ")
            edit_task(task_id, new_description)
        elif choice == '5':
            task_id = input("Enter task ID to set due date: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            set_due_date(task_id, due_date)
        elif choice == '6':
            task_id = input("Enter task ID to prioritize: ")
            priority = input("Enter priority (Low, Medium, High): ")
            prioritize_task(task_id, priority)
        elif choice == '7':
            task_id = input("Enter task ID to categorize: ")
            category = input("Enter category: ")
            categorize_task(task_id, category)
        elif choice == '8':
            view_tasks()
        elif choice == '9':
            keyword = input("Enter keyword to search: ")
            search_task(keyword)
        elif choice == '10':
            sort_tasks_by_priority()
        elif choice == '11':
            status = input("Enter status to filter (Completed/Pending): ")
            filter_tasks_by_status(status)
        elif choice == '12':
            task_statistics()
        elif choice == '13':
            filename = input("Enter filename to import tasks from: ")
            import_tasks_from_file(filename)
        elif choice == '14':
            filename = input("Enter filename to export tasks to: ")
            export_tasks_to_file(filename)
        elif choice == '15':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
