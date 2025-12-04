from services.task_service import *
from dotenv import load_dotenv
import os

load_dotenv()

project_repository = ProjectRepository()
    

def create_project(name: str, description: str) -> Project | None:
    projects = project_repository.get_all()
    if len(projects) >= int(os.getenv("MAX_NUMBER_OF_PROJECT")):
        return None
    return project_repository.add(name, description)
    

def list_projects() -> List[Project] :
    return project_repository.get_all()


def validate_project_id(target_id: int) -> int | None:
    project = project_repository.get(target_id)
    if project != None :
        return target_id
    else:
        return None


def edit_project(target_id: int, name: str = None, description: str = None) -> Project:
    if validate_project_id(target_id) == None:
        return None
    return project_repository.update(target_id, name, description)   

    
def add_task(inputs: TaskDict) -> None:
    id = inputs["project_id"]
    if validate_project_id(id) == None:
        return None
    length = len(project_repository.get(id).tasks)
    if length >= int(os.getenv("MAX_NUMBER_OF_TASK")) :
        return None
    return task_repository.add(inputs)


def list_tasks(id: int) -> List[Task]:
    if len(project_repository.get(id).tasks) == 0 :
        return None
    return project_repository.get(id).tasks:


def validate_task_id(target_id: int) -> int | None:
    #if id == None:
     #   return None
    task = task_repository.get(target_id)
    if task != None :
        return target_id 
    else:
        return None
    
def change_task_status(target_id: int, new_status: str) -> Task | None:
    if validate_task_id(target_id) == None :
        return None
    if new_status in ("todo", "doing", "done"):
        task = task_repository.get(target_id)
        inputs : TaskDict = {
            "name" : task.name
            ,"description" : task.description
            ,"status" : new_status
            ,"deadline" : task.deadline
            ,"project_id" : task.project_id
        }
        return task_repository.update(id, inputs)
    else:
        return None


def edit_task(target_id: int, inputs: TaskDict) -> Task :
    if validate_task_id(target_id) == None :
        return None
    inputs["project_id"] = task_repository.get(target_id).project_id
    return task_repository.update(target_id, inputs)


def delete_task(target_id: int) -> None:
    if validate_task_id(target_id) == None :
        return
    task_repository.delete(target_id)


def delete_project(target_id: int) -> None:
    if validate_project_id(target_id) == None :
        return
    project_repository.delete(target_id)