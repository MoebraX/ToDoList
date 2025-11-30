import tasks

class Project:
    _id_counter = 0
    def __init__(self, name: str = "default_name", description: str = "-"):
        self.id = Project._id_counter
        Project._id_counter += 1
        self.name = name
        self.description = description

projects_db: list[Project] = []

def create_project () -> Project:
    while True:
        name = str(input("Enter a name: "))
        if name == "" or name.isspace():
             print("The name field can't be empty. Try another name.")
             continue
        if len(name) > 30:
            print("Name can't be longer than 30 characters. Try a shorter name.")
            continue
        for project in projects_db:
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
    new_project = Project(name, description)
    return new_project
    
       