from fastapi import FastAPI , status, HTTPException
from pydantic import BaseModel
from typing import Optional

from services import *


class ProjectData(BaseModel):
    name: str
    description: Optional[str] = None


app = FastAPI()


@app.post("/projects/create", status_code = status.HTTP_201_CREATED)
def api_create_project(inputs: ProjectData):
    try:
        project = create_project(inputs.name, inputs.description)
        response = {"id: " : project.id,
                    "name: " : project.name,
                    "description: " : project.description}
        return response
    except:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get("/projects/all",status_code = status.HTTP_200_OK)
def api_list_projects():
    try:
        projects = {}
        for project in list_projects():
            projects[project.id] = {
                "name" : project.name,
                "description" : project.description
            }
        return projects
    except:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@app.patch("/projects/{target_id}/edit")
def api_edit_project(target_id: int, inputs: ProjectData):
    try:
        project = edit_project(target_id = target_id, name = inputs.name,
            description = inputs.description)
        response = {"id: " : project.id,
                    "name: " : project.name,
                    "description: " : project.description}
        return response
    except ProjectNotFound:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)


@app.delete("/projects/delete/{target_id}")
def api_delete_project(target_id: int):
    try:
        delete_project(target_id)
        return {"message: " : "Project deleted successfully"}
    except ProjectNotFound:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)