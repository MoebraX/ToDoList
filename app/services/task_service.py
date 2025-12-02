from datetime import datetime, timedelta
from typing import Literal, TypedDict
from repositories.repositories import *


task_repository = TaskRepository()

class TaskDict(TypedDict):
    name: str
    description: str = "-"
    status: Literal["todo", "doing", "done"] = "todo"
    deadline: datetime = None
    project_id: int


def input_task() -> TaskDict:
    while True:
        name = str(input("Enter a name: "))
        if name == "" or name.isspace():
             print("The name field can't be empty. Try another name.")
             continue
        if len(name) > 30:
            print("Name can't be longer than 30 characters. Try a shorter name.")
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
    while True:
        status = str(input("Enter status: "))
        if status == "":
            status = "todo"
        if status in ("todo", "doing", "done"):
            break
        else :
            print("Status should be either one of todo|doing|done. Try again.")
    while True:
        user_input = input("Enter deadline (YYYY-MM-DD HH:MM:SS): ")
        if user_input == "":
            dt = datetime.now() + timedelta(days=10)
            break
        try:
            dt = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid format! Please use YYYY-MM-DD HH:MM:SS")
            continue
        if dt < datetime.now():
            print("The entered date/time is in the past.")
            continue
        break
    inputs = TaskDict(name = name, description = description, status = status, deadline = dt)
    return inputs


def create_task() -> Task:
    inputs = input_task()
    new_task = Task(inputs)
    return new_task


