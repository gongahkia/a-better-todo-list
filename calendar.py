from datetime import date, datetime
from todo import *
import time

# DISPLAY FOR CURRENT DATE AND TIME

temp_date = date.today().strftime("%d.%m.%y").split(".")
temp_date[1] = abs(int(temp_date[1]))
current_day, current_month, current_year = int(temp_date[0]), int(temp_date[1]), int(temp_date[2])
current_date = f"{temp_date[0]}.{temp_date[1]}.{temp_date[2]}"
current_time = datetime.now().strftime("%H:%M:%S")


print(f"current date: {current_date}\ncurrent time: {current_time}")


################################

# actual program

print("\n\n\n\n\n|\t\t\tWelcome to Bullet Calendar V1.0\t\t\t|\n   ~For any feedback and pull requests, refer to @gongahkia on Github~\n\n\n\n\n")
time.sleep(2)
print("loading...")
time.sleep(2)

# LOAD DEADLINES FROM TODO LIST TO CALENDAR

try:
    Task_holder = read_tasks()
    print("\n\n\nSystem Notif: Previous save loaded.")

except:
    Task_holder = []
    print("\n\n\nSystem Notif: Previous save could not be found.")

######################

due_today, due_this_month_upcoming, overdue = [], [], []

for task in Task_holder:
    print(task)
    task_date = task[2].split(".")
    task_day, task_month, task_year = int(task_date[0]), int(task_date[1]), int(task_date[2])
    
    if task_year == current_year and task_month == current_month:
        if task_day == current_day:
            # DEADLINE DUE TODAY
            due_today.append(task)

        elif task_day > current_day:
            # UPCOMING DEADLINE
            due_this_month_upcoming.append(task)

        elif task_day < current_day:
            # TASK OVERDUE
            overdue.append(task)
    elif task_month < current_month or task_year < current_year:
        # TASK OVERDUE
        overdue.append(task)

print(due_today, due_this_month_upcoming, overdue)
