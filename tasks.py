from datetime import datetime, timedelta
from typing import Literal

class Task:
    _id_counter = 0
    def __init__(self, name: str, description: str = "-", status: Literal["todo", "doing", "done"] = "todo", deadline: datetime = None):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.name = name
        self.description = description
        self.status = status
        self.deadline = deadline or (datetime.now() + timedelta(days=10))