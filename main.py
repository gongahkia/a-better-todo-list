from todo import *

Task_holder = []

while True:

    #EXIT CALL
    task_exit = input("Exit? [(Y)es / (N)o]: ")
    if task_exit.lower() == "y":
        break

    #ADD_TASK

    task_name = input("Task name: ")
    # (1) check input does not exceed 26 characters, otherwise reject entire input

    task_description = input("Task description: ")
    # (2) check input does not exceed 26 characters, otherwise reject entire input

    task_deadline = input("Task deadline: ")
    # (3) check input that it follows the appropriate dd.mm.yy format, otherwise reject entire input

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

    #SEE_TASKS
    print(see_tasks(Task_holder)) # this function is tested to be working

