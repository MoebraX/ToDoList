from services.task_service import *
from dotenv import load_dotenv
import os

load_dotenv()

project_repository = ProjectRepository()
    

def input_project() -> list[str]:
    while True:
        name = str(input("Enter a name: "))
        if name == "" or name.isspace():
             print("The name field can't be empty. Try another name.")
             continue
        if len(name) > 30:
            print("Name can't be longer than 30 characters. Try a shorter name.")
            continue
        for project in project_repository.get_all():
            if name == project.name:
                print("This name already exists. Try another name.")
                continue
        break
    while True:
        description = str(input("Enter a description: "))
        if len(description) > 150:
            print("Description can't be longer than 150 characters. Try again.")
            continue
        if description == "" or description.isspace():
            description = "-"
        break
    inputs = [name,description]
    return inputs


def create_project() -> Project:
    inputs = input_project()
    new_project = project_repository.add(inputs[0], inputs[1])
    print("<Project created successfully!>")
    return new_project
    

def list_projects() -> None:
    if project_repository.get_all() == []:
        print("<There's no existing project.>")
        return
    print("__________________________")
    print("\tID\t|\tName\t|\tDescription")
    for project in project_repository.get_all():
        print(f"\t{project.id}\t|\t{project.name}\t|\t{project.description}")
    print("__________________________")


def search_project_by_id() -> int | None:
    if project_repository.get_all() == []:
        print("<There's no existing project.>")
        return
    list_projects()
    while True:
        print("Enter project's id: ")
        target_id = int(input())
        project = project_repository.get(target_id)
        if project == None :
            print("The entered id was not found. Try again.")
        else:
            return target_id


def edit_project() -> None:
    id = search_project_by_id()
    if id == None:
        return
    inputs = input_project()
    project_repository.update(id, inputs[0], inputs[1])   

    
def add_task() -> None:
    if project_repository.get_all() == []:
        print("<There's no existing project.>")
        return
    id = search_project_by_id()
    if id == None:
        return
    length = len(project_repository.get(id).tasks)
    if length > int(os.getenv("MAX_NUMBER_OF_TASK")) :
        print("<The max number of tasks for this project is reached.>")
        return
    inputs = input_task()
    inputs["project_id"] = id
    task_repository.add(inputs)
    print("<New task created successfully.>")


def list_tasks(id: int) -> None:
    if len(project_repository.get(id).tasks) == 0 :
        print("No task exists.")
        return
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("\tID\t|\tName\t|\tDescription\t|\tStatus\t|\tDeadline")
    for task in project_repository.get(id).tasks:
        print(f"\t{task.id}\t|\t{task.name}\t|\t{task.description}\t|\t{task.status}\t|\t{task.deadline}")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^")


def search_task_by_project_id(id: int) -> int | None:
    if id == None:
        return
    if len(project_repository.get(id).tasks) == 0 :
        print("No task exists.")
        return
    while True :
        target_id = int(input("Enter task id: "))
        tasks = project_repository.get(id).tasks
        for task in tasks:
            if target_id == task.id :
                return target_id
        print("Task not found")  
    
def change_task_status() -> None:
    id = search_task_by_project_id(search_project_by_id())
    status = ""
    while True:
        status = str(input("Enter new status (todo/doing/done): "))
        if status in ("todo", "doing", "done"):
            break
    task = task_repository.get(id)
    inputs : TaskDict = {
        "name" : task.name
        ,"description" : task.description
        ,"status" : status
        ,"deadline" : task.deadline
        ,"project_id" : task.project_id
    }
    task_repository.update(id, inputs)
    print("<Status changed successfully.>")


def edit_task() -> None :
    id = search_project_by_id()
    list_tasks(id)
    task_id = search_task_by_project_id(id)
    if task_repository.get(task_id) == None:
        return
    inputs = input_task()
    inputs["project_id"] = task_repository.get(task_id).project_id
    task_repository.update(task_id, inputs)
    print("<Task's details were edited successfully.>")


def delete_task() -> None:
    id = search_project_by_id()
    list_tasks(id)
    task_id = search_task_by_project_id(id)
    if task_id == None:
        return
    task_repository.delete(task_id)
    print("<Task deleted successfully.>")


def delete_project() -> None:
    id = search_project_by_id()
    project_repository.delete(id)
    print("<Project deleted successfully.>")