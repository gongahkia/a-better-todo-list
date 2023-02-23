Task_holder = []
# (1) figure out how to export Task_holder list from main.py to this file --> consider exporting all actual program running code to another file and importing main.py stuff into said file?

Event_storer = {}
# dictionary of key-value pairs (task name, task component), task components sorted into dictionary of key-value pairs (name: , description: , deadline: , urgency: )

for task in Task_holder:
    # implement a check to see if the given task_name overlaps with existing task name in dictionary, reject if thats the case
    Event_storer[Task_holder[0]] = {"name": Task_holder[0], "description": Task_holder[1], "deadline": Task_holder[2], "urgency": Task_holder[3]}

