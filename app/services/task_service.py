from datetime import datetime, timedelta
from typing import Literal, TypedDict

#from repositories.repositories import *
from services.project_service import *


task_repository = TaskRepository()

class TaskDict(TypedDict):
    name: str
    description: str = "-"
    status: Literal["todo", "doing", "done"] = "todo"
    deadline: datetime = None
    project_id: int


def add_task(inputs: TaskDict) -> None:
    id = inputs["project_id"]
    if validate_project_id(id) == None:
        return None
    length = len(project_repository.get(id).tasks)
    if length >= int(os.getenv("MAX_NUMBER_OF_TASK")) :
        return None
    return task_repository.add(inputs)


def list_tasks_by_project(id: int) -> List[Task]:
    if validate_project_id(id) == None :
        return None
    return project_repository.get(id).tasks


def validate_task_id(target_id: int) -> int | None:
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