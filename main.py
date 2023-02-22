from todo import *

Task_holder = []

while True:

    #EXIT CALL
    task_exit = input("[(E)xit?]: ")
    if task_exit.lower() == "e" or task_exit.lower() == "exit":
        break

    #####################

    #ADD_TASK

    task_name = input("Task name: ")
    if len(task_name) > 25:
        print("Please shorten task name.")
        task_name = task_name[:22] + "..."
    # (1) possible tweaks: save full task name input in list and only SHOW truncated "..." name for the visualisation
    task_description = input("Task description: ")
    if len(task_description) > 25:
        print("Please shorten task description. ")
        task_description = task_description[:22] + "..."
    # (2) possible tweaks: save full task description input in list and only SHOW truncated "..." description for the visualisation

    task_deadline = input("Task deadline [DD.MM.YY]: ")
    date_components = task_deadline.split(".")
    if len(date_components) == 3:
        date_components[0], date_components[1], date_components[2] = int(date_components[0]), int(date_components[1]), int(date_components[2])
        if date_components[0] < 32 and date_components[0] > 0 and date_components[1] < 13 and date_components[1] > 0 and date_components[2] < 100 and date_components[2] > 22:
            pass
        else:
            print("Invalid date entered. Please enter a deadline in the future.")
            task_deadline = "22.2.23"
            # (3) to update this task_deadline variable with the value of the current day + 1, when updating the calender
    else:
        print("Please enter a deadline according to the specified date format [DD.MM.YY].")
        task_deadline = "22.2.23"
        # (4) to update this task_deadline variable with the value of the current day + 1, when updating the calender
            
    task_urgency = input("Task urgency [(L)ow / (M)edium / (H)igh]: ")
    if task_urgency.lower() == "l":
        task_urgency = "Low"
    elif task_urgency.lower() == "m":
        task_urgency = "Medium"
    elif task_urgency.lower() == "h":
        task_urgency = "High"
    else:
        task_urgency = "Low"

    add_task(task_name, task_description, task_deadline, task_urgency, Task_holder) # this function is tested to be working

    #####################

    #SEE_TASKS
    print(see_tasks(Task_holder)) # this function is tested to be working

