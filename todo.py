# To-Do List Manager (Command Line Application)

tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})
    print("✅ Task added successfully")

def view_tasks():
    if not tasks:
        print("📭 No tasks available")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i + 1}. {task['task']} [{status}]")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"🗑️ Task deleted: {removed['task']}")
    else:
        print("❌ Invalid task number")

def show_menu():
    print("\n==== To-Do List Manager ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(task)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)

        elif choice == "4":
            print("👋 Exiting To-Do List Manager")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
