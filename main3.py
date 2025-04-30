import json
import datetime

def add_task():
    name = input("Task name: ")
    while name == "" or name == " ":
        name = input (f"{name} is an invalid status. Try again: ")
    desc = input("Describe task: ")
    while desc == "" or desc == " ":
        desc = input (f"{desc} is an invalid status. Try again: ")
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
    for dicts in data:
        if dicts["name"] == task_to_remove:
            data.remove(dicts)
            data = data

def list_finished_tasks():
    if len(data) == 0:
        print("You have no tasks")
    else:
        print("These are the finished tasks you have: ")
        for dicts in data:
            if dicts.get("status") == "done":
                print(f"Name: {dicts['name']}, Description: {dicts['desc']}, Status: {dicts['status']}, Created At: {dicts['createdAt']}")

def list_todo_tasks():
    if len(data) == 0:
        print("You have no tasks")
    else:
        print("These are the tasks you have to-do: ")
        for dicts in data:
            if dicts.get("status") == "todo":
                print(f"Name: {dicts['name']}, Description: {dicts['desc']}, Status: {dicts['status']}, Created At: {dicts['createdAt']}")

def list_inprogress_tasks():
    if len(data) == 0:
        print("You have no tasks")
    else:
        print("These are the tasks you have inprogress: ")
        for dicts in data:
            if dicts.get("status") == "inprogress":
                print(f"Name: {dicts['name']}, Description: {dicts['desc']}, Status: {dicts['status']}, Created At: {dicts['createdAt']}")            
        

with open('data.json','r') as file:
    data = json.load(file)

while True:
    main = input("Welcome to Task Tracker CLI! How may I assist you with your tasks? (add, list, remove) ")
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

    with open('data.json','w') as file:
        json.dump(data,file,indent=2)