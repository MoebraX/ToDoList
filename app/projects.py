from tasks import *
from dotenv import load_dotenv
import os

load_dotenv()

class Project:
    _id_counter = 0
    def __init__(self, name: str = "default_name", description: str = "-"):
        if len(name) > 30 :
            raise ValueError("Project name can't be longer than 30 characters.")
        if len(description) > 150 :
            raise ValueError("Project description can't be longer than 150 characters.")
        self.id = Project._id_counter
        Project._id_counter += 1
        self.name = name
        self.description = description
        self.tasks: list[Task] = []

projects_db: list[Project] = []

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
        if description == " " or description.isspace():
            description = "-"
        break
    inputs = [name,description]
    return inputs


def create_project() -> Project:
    inputs = input_project()
    new_project = Project(inputs[0], inputs[1])
    add_project_to_db(new_project)
    print("<Project created successfully!>")
    return new_project
    

def list_projects() -> None:
    if pass_projects_from_db() == []:
        print("<There's no existing project.>")
        return
    print("__________________________")
    print("\tID\t|\tName\t|\tDescription")
    for project in pass_projects_from_db():
        print(f"\t{project.id}\t|\t{project.name}\t|\t{project.description}")
    print("__________________________")


def search_project_by_id() -> Project:
    if pass_projects_from_db() == []:
        print("<There's no existing project.>")
        return
    list_projects()
    flag = False
    while flag == False:
        print("Enter project's id: ")
        target_id = int(input())
        for project in pass_projects_from_db():
            if project.id == target_id:
                return project
        if flag == False :
            print("The entered id was not found. Try again.")


def edit_project() -> None:
    project = search_project_by_id()
    inputs = input_project()
    project.name = inputs["name"]
    project.description = inputs["description"]    

    
def add_task() -> None:
    if pass_projects_from_db() == []:
        print("<There's no existing project.>")
        return
    project = search_project_by_id()
    if len(project.tasks) > int(os.getenv("MAX_NUMBER_OF_TASK")) :
        print("<The max number of tasks for this project is reached.>")
        return
    new_task = create_task()
    project.tasks.append(new_task)
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
    return project


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
    task.name = inputs["name"]
    task.description = inputs["description"]
    task.status = inputs["status"]
    task.deadline = inputs["deadline"]
    print("<Task's details were edited successfully.>")


def delete_task() -> None:
    project = search_project_by_id()
    list_tasks(project)
    task = search_task_by_project(project)
    if task == None:
        return
    project.tasks.remove(task)
    del task
    print("<Task deleted successfully.>")


def delete_project() -> None:
    project = search_project_by_id()
    for task in project.tasks:
        project.tasks.remove(task)
        del task
    pass_projects_from_db().remove(project)
    del project
    print("<Project deleted successfully.>")