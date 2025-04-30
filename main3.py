import json
import datetime

def add_task():
    name = input("Task name: ")
    while name == "" or name == " ":
        name = input (f"{name} is an invalid name. Try again: ")
    desc = input("Describe task: ")
    while desc == "" or desc == " ":
        desc = input (f"{desc} is an invalid description. Try again: ")
    status = input("Status: (todo, inprogress, done) ")
    while status not in ["todo","inprogress","done"]:
        status = input (f"{status} is an invalid status. Try again: ")

    new_task = {
        "name": f"{name}",
        "desc": f"{desc}",
        "status": f"{status}",
        "createdAt": f"{str(datetime.datetime.now())[:-10]}",
    }

    return new_task

def list_tasks():
    if len(data) == 0:
        print("You have no tasks")
    else:
        print("These are the tasks you input: ")
        for dicts in data:
            print(f"Name: {dicts['name']}, Description: {dicts['desc']}, Status: {dicts['status']}, Created At: {dicts['createdAt']}")

def remove_tasks(data):
    task_to_remove = input("Which task would you like to remove? ")
    while task_to_remove == "" or task_to_remove == " ":
        task_to_remove = input(f"{task_to_remove} is an invalid input. Try again: ")
    for dicts in data:
        if dicts["name"] == task_to_remove:
            data.remove(dicts)
            data = data
    else:
        print(f"There was no task by the name by {task_to_remove} ")

def list_finished_tasks():
    if len(data) == 0:
        print("You have no tasks")
    else:
        print("These are the finished tasks you have: ")
        for dicts in data:
            if dicts.get("status") == "done":
                print(f"Name: {dicts['name']}, Description: {dicts['desc']}, Status: {dicts['status']}, Created At: {dicts['createdAt']}")
        else:
            print("You have no tasks that are finished")    
def list_todo_tasks():
    if len(data) == 0:
        print("You have no tasks")
    else:
        print("These are the tasks you have to-do: ")
        for dicts in data:
            if dicts.get("status") == "todo":
                print(f"Name: {dicts['name']}, Description: {dicts['desc']}, Status: {dicts['status']}, Created At: {dicts['createdAt']}")
        else:
            print("You have no tasks to-do")             

def list_inprogress_tasks():
    if len(data) == 0:
        print("You have no tasks")
    else:
        print("These are the tasks you have inprogress: ")
        for dicts in data:
            if dicts.get("status") == "inprogress":
                print(f"Name: {dicts['name']}, Description: {dicts['desc']}, Status: {dicts['status']}, Created At: {dicts['createdAt']}")     
        else:
            print("You have no tasks in progress")     

def update_task_status(data):
    update_main = input("Would you like to update a task, description, or status: ")
    if update_main == "task":
        task_to_update = input("Which task's name would you like to update? ")
        while task_to_update in ["", " "]:
            task_to_update = input(f"{task_to_update} is not a valid task. Try again: ")
        name_to_give = input("What name would you like to give to this task? ")
        while name_to_give in [" ",""]:
            name_to_give = input(f"{name_to_give} is not a valid name. Try again: ")
        for dicts in data:
            if dicts["name"] == task_to_update:
                dicts["name"] = name_to_give
                return data
            else:
                print("That task was not found")
    if update_main == "description":
        task_to_update = input("Which task's description would you like to update? ")
        while task_to_update in ["", " "]:
            task_to_update = input(f"{task_to_update} is not a valid task. Try again: ")
        description_to_give = input("What description would you like to give to this task? ")
        while description_to_give in [" ",""]:
            description_to_give = input(f"{description_to_give} is not a valid description. Try again: ")
        for dicts in data:
            if dicts["name"] == task_to_update:
                dicts["desc"] = description_to_give
                return data
            else:
                print("That task was not found")
    if update_main == "status":
        task_to_update = input("Which task's status would you like to update? ")
        while task_to_update in ["", " "]:
            task_to_update = input(f"{task_to_update} is not a valid task. Try again: ")
        status_to_give = input("What status would you like to give to this task? (inprogress, done, todo) ")
        while status_to_give not in ["inprogress","done","todo"]:
            status_to_give = input(f"{status_to_give} is not a valid status. Try again: ")
        for dicts in data:
            if dicts["name"] == task_to_update:
                dicts["status"] = status_to_give
                return data
            else:
                print("That task was not found")
    

           

with open('data.json','r') as file:
    data = json.load(file)

while True:
    main = input("Welcome to Task Tracker CLI! How may I assist you with your tasks? (add, list, remove, update) ")
    if main == "list":
        list_type = input("What shall I list out (general, todo, done, inprogress) ")
        if list_type == "general":
            list_tasks()
        if list_type == "todo":
            list_todo_tasks()
        if list_type == "done":
            list_finished_tasks()
        if list_type == "inprogress":
            list_inprogress_tasks()
    if main == "add":
        data.append(add_task())
    if main == "remove":
        list_tasks()
        remove_tasks(data)
    if main == "update":
        list_tasks()
        update_task_status(data)


    with open('data.json','w') as file:
        json.dump(data,file,indent=2)