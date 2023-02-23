from todo import *
from datetime import date 

current_date = date.today()
temp_date = (current_date.strftime("%d.%m.%y")).split(".")
temp_date[1] = abs(int(temp_date[1]))
formatted_current_date = f"{temp_date[0]}.{temp_date[1]}.{temp_date[2]}"
print(formatted_current_date)

try:

    # RELOAD PAST SAVE

    Task_holder = read_tasks()
    print("Previous save loaded.")

except:
    print("Previous save could not be found.")
    Task_holder = []

while True:

    #EXIT CALL

    task_exit = input("[(E)xit?]: ")
    if task_exit.lower() == "e" or task_exit.lower() == "exit": 

        # SAVE TASKS TO LOCAL FILE

        save_input = input("[S]ave?: ")
        if save_input.lower() == "s":
            write_tasks(Task_holder)
            print("Tasks saved")
            break

    #####################

    #ADD_TASK

    task_name = input("Task name: ")
    if len(task_name) > 25:
        print("Please shorten task name.")
        task_name = task_name[:22] + "..."

    task_description = input("Task description: ")
    if len(task_description) > 25:
        print("Please shorten task description. ")
        task_description = task_description[:22] + "..."

    task_deadline = input("Task deadline [DD.MM.YY]: ")
    date_components = task_deadline.split(".")
    if len(date_components) == 3:
        date_components[0], date_components[1], date_components[2] = int(date_components[0]), int(date_components[1]), int(date_components[2])
        if date_components[0] < 32 and date_components[0] > 0 and date_components[1] < 13 and date_components[1] > 0 and date_components[2] < 100 and date_components[2] > 22:
            pass
        else:
            print("Invalid date entered. Please enter a deadline in the future.")
            task_deadline = formatted_current_date
    else:
        print("Please enter a deadline according to the specified date format [DD.MM.YY].")
        task_deadline = formatted_current_date
            
    task_urgency = input("Task urgency [(L)ow / (M)edium / (H)igh]: ")
    if task_urgency.lower() == "l":
        task_urgency = "Low"
    elif task_urgency.lower() == "m":
        task_urgency = "Medium"
    elif task_urgency.lower() == "h":
        task_urgency = "High"
    else:
        task_urgency = "Low"

    add_task(task_name, task_description, task_deadline, task_urgency, Task_holder)

    #####################

    #SEE_TASKS

    print(see_tasks(Task_holder))

    #####################

    #COMPLETE_TASKS

    completed_task = input("Enter name of completed task: ")

    # (5) when working on UI with main page and shifting arrow, change this input to allow for auto-checking of which task is being pointed at.
    # (6) ensure point 5 is up and running so that multiple tasks with same task name can be created without conflict
    
    complete_task(completed_task, Task_holder)

    #####################

    #DELETE_TASKS

    deleted_task = input("Enter name of task to be deleted: ")

    # (7) follow up on points 5 and 6 for this operation as well

    complete_task(deleted_task, Task_holder)

    #####################

    #EDIT_TASK_NAME
    old_task_name = input("Enter old task name: ")
    new_task_name = input("Enter new task name: ")
    if len(new_task_name) > 25:
        print("Please shorten task name.")
        new_task_name = new_task_name[:22] + "..."

    # (8) possible tweaks: save full task name input in list and only SHOW truncated "..." name for the visualisation

    edit_task_name(old_task_name, new_task_name, Task_holder)

    # (9) once the main menu is up, allow for selection of existing task name to be done via shifting arrow, and only typing done should be for new task name

    #####################

    #EDIT_TASK_DESCRIPTION
    old_task_description = input("Enter old task description: ")
    new_task_description = input("Enter new task description: ")
    if len(new_task_description) > 25:
        print("Please shorten task description. ")
        new_task_description = new_task_description[:22] + "..."

    # (10) possible tweaks: save full task description input in list and only SHOW truncated "..." description for the visualisation

    edit_task_description(old_task_description, new_task_description, Task_holder)

    # (11) once the main menu is up, allow for selection of existing task description to be done via shifting arrow, and only typing done should be for new task description

    #####################

    #EDIT_TASK_DEADLINE
    old_task_deadline = input("Enter old task deadline [DD.MM.YY]: ")    
    new_task_deadline = input("Enter new task deadline [DD.MM.YY]: ")
    new_date_components = new_task_deadline.split(".")
    if len(new_date_components) == 3:
        new_date_components[0], new_date_components[1], new_date_components[2] = int(new_date_components[0]), int(new_date_components[1]), int(new_date_components[2])
        if new_date_components[0] < 32 and new_date_components[0] > 0 and new_date_components[1] < 13 and new_date_components[1] > 0 and new_date_components[2] < 100 and new_date_components[2] > 22:
            pass
        else:
            print("Invalid date entered. Please enter a deadline in the future.")
            new_task_deadline = formatted_current_date
    else:
        print("Please enter a deadline according to the specified date format [DD.MM.YY].")
        new_task_deadline = formatted_current_date
    edit_task_deadline(old_task_deadline, new_task_deadline, Task_holder)

    # (14) once the main menu is up, allow for selection of existing task deadline to be done via shifting arrow, and only typing done should be for new task deadline

    #####################

    #EDIT_TASK_URGENCY
    old_task_urgency = input("Enter old task urgency level [(L)ow / (M)edium / (H)igh]: ")
    new_task_urgency = input("Enter new task urgency level [(L)ow / (M)edium / (H)igh]: ")
    if new_task_urgency.lower() == "l":
        new_task_urgency = "Low"
    elif new_task_urgency.lower() == "m":
        new_task_urgency = "Medium"
    elif new_task_urgency.lower() == "h":
        new_task_urgency = "High"
    else:
        new_task_urgency = "Low"
    edit_task_urgency(old_task_urgency, new_task_urgency, Task_holder)

    # (15) once the main menu is up, allow for selection of existing task urgency to be done via shifting arrow, and only typing done should be for new task urgency

    #####################
