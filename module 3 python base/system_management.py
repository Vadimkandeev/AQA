class DataError(Exception):
    pass

class Project:
    def __init__(self, name_project):
        self.tasks = []
        self.name_project = name_project


    def get_progress(self):
        status_list = ["New", "In progress", "Done"]
        tasks_not_done = 0
        tasks_done = 0
        for task in self.tasks:
            if task.status not in status_list:
                raise DataError("Ошибка статуса")
            elif task.status == "Done":
                tasks_done += 1
            else:
                tasks_not_done += 1
        return self.name_project, self.tasks, tasks_not_done, tasks_done


    def add_task(self, task):
        self.tasks.append(task)

#--------------------------------------------------------------------

class Task:
    def __init__(self):
        self.status = "New"
        self.assigned_to = None

    def task_start(self):
        if self.status != "New":
            raise DataError(f"Задача уже в статусе {self.status}")
        self.status = "In progress"


    def task_complete(self):
        if self.status != "In progress":
            raise DataError(f"Задача в статусе {self.status}")
        self.status = "Done"


    def assign_to(self, developer):
        if self.assigned_to is not None:
            raise DataError(f"Задача уже назначена на {self.assigned_to.name}")
        self.assigned_to = developer

#-------------------------------------------------------------------------------


class Developer:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.complete_tasks = []

    def take_task(self, task):
        task.assign_to(self)
        task.task_start()
        self.tasks.append(task)


    def complete_task(self, task):
        if task not in self.tasks:
            raise DataError("Ошибка назначения задачи")
        task.task_complete()
        self.tasks.remove(task)
        self.complete_tasks.append(task)


    def get_workload(self):
        return self.tasks, self.complete_tasks





project = Project("My_notepad")

desktop_task = Task()

project.add_task(desktop_task)

project.get_progress()


