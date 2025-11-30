import tasks

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

projects_db: list[Project] = []

def pass_projects_from_db() -> list[Project] :
    return projects_db

def add_project_to_db( project: Project) -> None:
    projects_db.append(project)

def create_project() -> Project:
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
    new_project = Project(name, description)
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
