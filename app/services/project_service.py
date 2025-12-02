from task_service import *
from dotenv import load_dotenv
import os

load_dotenv()

projects_db: list[Project] = []
project_repository = ProjectRepository()

def pass_projects_from_db() -> list[Project] :
    return projects_db

def add_project_to_db(project: Project) -> None:
    projects_db.append(project)
    

def input_project() -> list[str]:
    while True:
        name = str(input("Enter a name: "))
        if name == "" or name.isspace():
             print("The name field can't be empty. Try another name.")
             continue
        if len(name) > 30:
            print("Name can't be longer than 30 characters. Try a shorter name.")
            continue
        for project in pass_projects_from_db():
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


def search_project_by_id() -> Project:
    if project_repository.get_all() == []:
        print("<There's no existing project.>")
        return
    list_projects()
    flag = False
    while flag == False:
        print("Enter project's id: ")
        target_id = int(input())
        project = project_repository.get(target_id)
        if project == None :
            print("The entered id was not found. Try again.")
        else:
            flag = True


def edit_project() -> None:
    project = search_project_by_id()
    inputs = input_project()
    project.name = inputs["name"]
    project.description = inputs["description"]    

    
def add_task() -> None:
    if project_repository.get_all() == []:
        print("<There's no existing project.>")
        return
    project = search_project_by_id()
    if len(project.tasks) > int(os.getenv("MAX_NUMBER_OF_TASK")) :
        print("<The max number of tasks for this project is reached.>")
        return
    inputs = input_task()
    inputs.project_id = project.id
    task_repository.add(inputs)
    print("<New task created successfully.>")


def list_tasks(project: Project) -> None:
    if len(project.tasks) == 0 :
        print("No task exists.")
        return
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("\tID\t|\tName\t|\tDescription\t|\tStatus\t|\tDeadline")
    for task in project.tasks:
        print(f"\t{task.id}\t|\t{task.name}\t|\t{task.description}\t|\t{task.status}\t|\t{task.deadline}")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^")


def search_task_by_project(project: Project) -> Task | None:
    if project == None:
        return
    if len(project.tasks) == 0 :
        print("No task exists.")
        return
    while True :
        target_id = int(input("Enter task id: "))
        for task in project.tasks:
            if target_id == task.id :
                return task
        print("Task not found")  
    
def change_task_status() -> None:
    task = search_task_by_project(search_project_by_id())
    status = ""
    while True:
        status = str(input("Enter new status (todo/doing/done): "))
        if status in ("todo", "doing", "done"):
            break
    task.status = status
    print("<Status changed successfully.>")


def edit_task() -> None :
    project = search_project_by_id()
    list_tasks(project)
    task = search_task_by_project(project)
    if task == None:
        return
    inputs = input_task()
    inputs.project_id = task.project_id
    task_repository.update(task.id, inputs)
    print("<Task's details were edited successfully.>")


def delete_task() -> None:
    project = search_project_by_id()
    list_tasks(project)
    task = search_task_by_project(project)
    if task == None:
        return
    task_repository.delete(task.id)
    print("<Task deleted successfully.>")


def delete_project() -> None:
    project = search_project_by_id()
    project_repository.delete(project.id)
    print("<Project deleted successfully.>")