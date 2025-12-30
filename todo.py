tasks = []
def add_task(task):
    tasks.append({"task": task, "done": False})
    print("Task added successfully")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i+1}. {task['task']} [{status}]")

def main():
    print("Welcome to To-Do List Manager")
    
if __name__ == "__main__":
    main()
