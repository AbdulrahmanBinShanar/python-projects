from datetime import datetime, timedelta

class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date

def add_task(tasks, task):
    tasks.append(task)

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. Title: {task.title}, Priority: {task.priority}, Due Date: {task.due_date}")

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

tasks_list = []
task1 = Task("Complete project", "High", datetime.now() + timedelta(days=7))
task2 = Task("Prepare presentation", "Medium", datetime.now() + timedelta(days=3))

add_task(tasks_list, task1)
add_task(tasks_list, task2)

display_tasks(tasks_list)

new_task = Task("Review documentation", "Low", datetime.now() + timedelta(days=5))
add_task(tasks_list, new_task)

print("\nTasks after adding a new one:")
display_tasks(tasks_list)

task_to_remove = int(input("\nEnter the index of the task to remove: "))
remove_task(tasks_list, task_to_remove)

print("\nTasks after removing a task:")
display_tasks(tasks_list)