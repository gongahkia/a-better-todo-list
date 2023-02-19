class Task:
    
    # initialize tasks with instance variables using constructor method
    def __init__ (self):
        self.name = ""
        self.descripton = ""
        self.deadline = "" #in the format 20.10.20 (dd.mm.yy)
        self.urgency = "" #low, medium, high

    # check off completed tasks: to be handled by removing the task variable name from the list of existing tasks

    # edit existing tasks:
    def change_name (self, newname):
        self.name = newname
    def change_description (self, newdescription):
        self.descripton = newdescription
    def change_deadline (self, newdeadline):
        self.deadline = newdeadline
    def change_urgency (self, newurgency):
        self.urgency = newurgency

    # deletion of tasks: to be handled by removing the task variable name from the list of existing tasks 

    # used to save current task's instance attributes to a dictionary, which will then be added to the overall .json
    def at_a_glance (self):
        finaldict = {}
        finaldict["name"] = self.name
        finaldict["description"] = self.descripton
        finaldict["deadline"] = self.deadline
        finaldict["urgency"] = self.urgency
        return finaldict

