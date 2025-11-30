from projects import *


while(True):
    print("\nHi. What can I do for you?")
    print("""\t Create new project-> 1
         See list of all existing projects-> 2
         Edit details of a project-> 3
         Delete a project-> 4
         Create a new task-> 5
         List all tasks of a project-> 6
         Change status of a task-> 7""")
    command = input()
    match command:
        case "1":
            new_project = create_project()
        case "2":
            list_projects()
        case "3":
            edit_project()
        case "4":
            pass
        case "5":
            add_task()
        case "6":
            list_tasks()
        case "7":
            change_task_status()
        case _:
            pass