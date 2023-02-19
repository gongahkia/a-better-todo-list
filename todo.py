class Task:
    
    # initialize tasks with instance variables using constructor method
    def __init__ (self, Task_name = "", Task_desc = "", Task_deadline = "", Task_urgency = "low"):
        self.name = Task_name
        self.descripton = Task_desc
        self.deadline = Task_deadline #in the format 20.10.20 (dd.mm.yy)
        self.urgency = Task_urgency #low, medium, high

    # check off completed tasks: to be handled by removing the task variable name from the dictionary of existing tasks

    # edit existing tasks:
    def change_name (self, newname):
        self.name = newname
    def change_description (self, newdescription):
        self.descripton = newdescription
    def change_deadline (self, newdeadline):
        self.deadline = newdeadline
    def change_urgency (self, newurgency):
        self.urgency = newurgency

    # deletion of tasks: to be handled by removing the task variable name from the dictionary of existing tasks 

    # used to save current task's instance attributes to a dictionary, which will then be added to the overall .json
    def at_a_glance (self):
        finallist = []
        finallist.extend((self.name, self.descripton, self.deadline, self.urgency))
        return finallist

Task_dict = {}

def completed_deleted_tasks (Task_dict, Task_name):
    if Task_name not in Task_dict:
        print(f"{Task_name} not found in list of tasks")
    else:
        Task_dict.remove(Task_name)

def add_task (Task_dict, Task_name, Task_desc, Task_deadline, Task_urgency):
    if Task_name in Task_dict:
        print(f"{Task_name} already exists, please choose another name")
    else:
        Task_dict[(Task_name.at_a_glance())[0]] = Task_name.at_a_glance()
        Task_name = Task(Task_name, Task_desc, Task_deadline, Task_urgency)


# create even spacing for each of the fields to allow for column dividers | to be evenly spread and aligned
def see_tasks (Task_dict):
    count = 1
    for Task in Task_dict:
        print (f"{count}. | {(Task_dict[Task])[0]} | {(Task_dict[Task])[1]} | {(Task_dict[Task])[2]} | {(Task_dict[Task])[3]}\n", end="")
        count += 1

add_task(Task_dict, "print out homework", "Immediately", "20.2.22", "High")
see_tasks(Task_dict)
add_task(Task_dict, "go work", "Later", "10.1.20", "low")
print(Task_dict)
Task_dict[1].change_name("ok")
see_tasks(Task_dict)
