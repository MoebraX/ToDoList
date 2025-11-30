from datetime import datetime, timedelta
from typing import Literal

class Task:
    _id_counter = 0
    def __init__(self, name: str = "default_name", description: str = "-", status: Literal["todo", "doing", "done"] = "todo", deadline: datetime = None):
        if len(name) > 30 :
            raise ValueError("Task name can't be longer than 30 characters.")
        if len(description) > 150 :
            raise ValueError("Task description can't be longer than 150 characters.")
        self.id = Task._id_counter
        Task._id_counter += 1
        self.name = name
        self.description = description
        self.status = status
        self.deadline = deadline or (datetime.now() + timedelta(days=10))