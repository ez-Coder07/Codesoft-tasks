def show_tasks():
    print("Your list of tasks:")
    print("-----------------------------")
    with open("sav.txt", "r") as f:
        tasks = f.readlines()
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
    print("-----------------------------\n")


def add_task():
    task = input("Enter the task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    with open("sav.txt", "a") as f:
        f.write(task + "\n")
    print(f"Task '{task}' added.")


def remove_task():
    try:
        task_number = int(input("Enter the task number to remove (0 to remove all): "))
    except ValueError:
        print("Please enter a valid number.")
        return
    with open("sav.txt", "r") as f:
        tasks = f.readlines()
    if task_number == 0:
        with open("sav.txt", "w") as f:
            f.write("")
    elif 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        with open("sav.txt", "w") as f:
            f.writelines(tasks)
        print(f"Task '{removed_task.strip()}' removed.")
    else:
        print("Invalid task number.")

show_tasks()

while True:
    print("\nOptions:")
    print("0. Show tasks")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "0":
        show_tasks()
    elif choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
