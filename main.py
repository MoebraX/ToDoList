from projects import *


while(True):
    print("\nHi. What can I do for you?")
    print("""\t Create new project-> 1""")
    command = input()
    match command:
        case "1":
            new_project = create_project()
            projects_db.append(new_project)
            print("<Project created successfully!>")
        case _:
            pass