import json
import datetime

def add_task():
    name = input("Task name: ")
    desc = input("Describe task: ")
    status = input("Status: ")

    new_task = {
        "name": f"{name}",
        "desc": f"{desc}",
        "status": f"{status}",
        "createdAt": f"{str(datetime.datetime.now())[:-10]}",
    }

    return new_task

with open('data.json','r') as file:
    data = json.load(file)


data.append(add_task())



with open('data.json','w') as file:
    json.dump(data,file,indent=2)

