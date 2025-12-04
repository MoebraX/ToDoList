from dotenv import load_dotenv
import os

#from services.task_service import *
from exceptions.service_exceptions import *
from repositories.repositories import *

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


def edit_project(target_id: int, name: str = None, description: str = None) -> Project | None:
    if validate_project_id(target_id) == None:
        return None
    return project_repository.update(target_id, name, description)   


def delete_project(target_id: int) -> None:
    if validate_project_id(target_id) == None :
        return
    project_repository.delete(target_id)