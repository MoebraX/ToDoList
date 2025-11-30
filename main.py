from projects import *


while(True):
    print("\nHi. What can I do for you?")
    print("""\t Create new project-> 1
         See list of all existing projects-> 2""")
    command = input()
    match command:
        case "1":
            new_project = create_project()
        case "2":
            list_projects()
        case _:
            pass