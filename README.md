# To-do List and project manager

![](https://i.kym-cdn.com/entries/icons/mobile/000/026/489/crying.jpg)

This is my attempt to decompress from learning so many languages by distracting myself with a small project- a to-do list that runs on the **CLI (terminal)**.    

> **Edit on 19.2.2023**: I have since given up on writing this monster in C, and will instead be doing the ultimate funny by writing this in *Python* first, and then translating it to ***Nim***

![](https://img.devrant.com/devrant/rant/r_714509_DhE7P.jpg)

----------

Here is what I hope to accomplish with this terminal application:

### General

- [ ] stylized *home page* 
- [ ] stylized *notifications bar* to print out any new notifications
- [ ] clear, easy to navigate commands and GUI (multiple pages to navigate between, each with their own defined purpose)
- [x] terminal that ***clears the screen*** whenever a command is inputted, to give the impression of [constant refresh](https://www.geeksforgeeks.org/clear-screen-python/) on the application *(import os, os.system('cls'))*


### To-do List

- [x] create new tasks in a numbered list, with **task name**, **description**, **date/deadline** *(date and time)* and **urgency level** *(low, medium, high)*
- [x] check off completed tasks
- [x] edit existing tasks (task name, description, date/deadline)
- [x] delete tasks
- [x] save current session's tasks to a local `pickle` file that is updated whenever the terminal session is closed
- [x] boot up using previous saved tasks from the local `pickle` file


### Event tracker 

- [x] Events and additional deadlines to be taken from the `To-do List`
- [x] calendar that shows the **current date and time** on the default application *home page*
- [x] reminders for **deadlines on the current day** for the default application *home page*
- [x] notification prompts for *upcoming deadlines* in upcoming weeks in the month
- [ ] calendar view (weekly) that shows all the deadlines and their respective times for the current week
- [ ] calendar view (monthly) that shows all the deadline and their respective times for the current month

### Project manager

- [ ] Option on `To-do List` to create a ***Project***, which you can then bunch a group of To-do items under *(each item retains its properties as previously described under `To-do List`)*
- [ ] create new projects in a numbered list, with **Project name** and **Project description**
- [ ] **Visualizer** option, which prints out a bar diagram of the extent of completion for each of the To-do items under the project head 
- [ ] completed projects will be checked off
- [ ] edit existing projects (project name, description)
- [ ] delete projects

----------

### Possible approaches

> **Edit on 19.2.2023**: I have since learned that object-oriented might not be the best approach for completing this project.

* Create a global *Task_holder* dictionary that will then store the *Tasks*, which are also dictionaries ***(storing the name, description, deadline and urgency level of each task)***

----------

### To be implemented in the future

- sort tasks by **date** *(ascending/descending)*, **task name** *(alphabetical)*
> This would probably be easier achieved if I used a dictionary instead of a list to store all my tasks.

----------

Let's see how far I get with this one 💀  
~Gong
