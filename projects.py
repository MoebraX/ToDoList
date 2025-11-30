import tasks

class Project:
    _id_counter = 0
    def __init__(self, name: str = "default_name", description: str = "-"):
        self.id = Project._id_counter
        Project._id_counter += 1
        self.name = name
        self.description = description