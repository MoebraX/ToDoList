from projects import *


while(True):
    print("\nHi. What can I do for you?")
    print("""\t Create new project-> 1
          \t See list of all existing projects-> 2""")
    command = input()
    match command:
        case "1":
            new_project = create_project()
            add_project_to_db(new_project)
            print("<Project created successfully!>")
        case "2":
            pass
        case _:
            pass