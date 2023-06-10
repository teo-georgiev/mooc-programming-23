# Write your solution here
# If you use the classes made in the previous exercise, copy them here

# class OrderApplication
# Print out the help() method with the commands 
# method add order which initialised an Order object
    # the method adds the object to an OrderApplication list (maybe worth making an All Orders class?)
# method that returns a list of finished tasks 
# method that returns a list of unfinished tasks
    # both lists need to take advantage of the __str__ method in the class Order
# method to mark task as finished 
    # provide the ID of the task that needs to be marked
# method for programmers
    # provides a list of programmers who are working on tasks
# method for programmer's status 
    # name input
    # returns a summary for finished and unfinished tasks, sum of done hours, scheduled hours 

    # class Order, which has DESCRIPTION, PROGRAMMER AND WORKLOAD ESTIMATE
    # PROGRAMMER AND WORKLOAD ESTIMATE is a single input which has to be broken down into separate variables

class Task: 
    id = 0
    @classmethod
    def new_id(cls): 
        Task.id += 1
        return Task.id

    def __init__(self, description: str, programmer: str, workload: int):
        self.__description = description
        self.__programmer = programmer
        self.__workload = workload

        # # Splitting of the programmer's name and their workload
        # parts = programmer_workload.split(" ")
        # self.__programmer = parts[0]
        # self.__workload = int(parts[1])

        # Task completion 
        self.__finished = False 

        # Task id 
        self.__id = Task.new_id()
    
    def __str__(self) -> str:
        status = "NOT FINISHED" if not self.__finished else "FINISHED"
        return f"{self.__id}: {self.__description} ({self.__workload} hours), programmer {self.__programmer} {status}"
    
    def is_finished(self):
        return self.__finished

    def mark_finished(self):
        self.__finished = True

    def programmer_name(self):
        return self.__programmer

    def task_id(self): 
        return self.__id
    
    def workload(self):
        return self.__workload 

class OrdersList: 
    def __init__(self):
        self.__orders = []

    def add_task(self):
        description = input("description: ")
        programmer_workload = input("programmer and workload estimate: ")
        parts = programmer_workload.split(" ")

        if len(parts) != 2: 
            return "erroneous input" 
        try: 
            int(parts[1])
        except ValueError:
            return "erroneous input" 
        self.__orders.append(Task(description, parts[0], int(parts[1])))
        return "added!"

    def all_orders(self):
        for task in self.__orders: 
            print(task)

    def finished_tasks(self):
        return [task for task in self.__orders if task.is_finished()]

    def unfinished_tasks(self):
        return [task for task in self.__orders if not task.is_finished()]

    def mark_finished(self, task_id: str):
        try: 
            int(task_id)
        except ValueError:
            return "erroneous input" 
        task_id = int(task_id)
        if task_id > len(self.__orders) or task_id < 1: 
            return "erroneous input"
        
        for task in self.__orders: 
            if task.task_id() == task_id:
                task.mark_finished()
                return "marked as finished"
    
    def programmers(self): 
        return list(set([task.programmer_name() for task in self.__orders])) 

    def programmer_status(self, programmer: str): 
        if programmer not in self.programmers(): 
            return f"erroneous input"

        fin_tasks = [task for task in self.__orders if task.programmer_name() == programmer and task.is_finished()]
        unfin_tasks = [task for task in self.__orders if task.programmer_name() == programmer and not task.is_finished()]

        fin_hours = sum(task.workload() for task in fin_tasks)
        unfin_hours = sum(task.workload() for task in unfin_tasks)

        return f"tasks: finished {len(fin_tasks)} not finished {len(unfin_tasks)}, hours: done {fin_hours} scheduled {unfin_hours}"

class OrderApplication: 
    def __init__(self) -> None:
        self.__orders_list = OrdersList()

    def help(self): 
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.help()
        while True: 
            print()
            command = input("command: ")
            
            # Exit
            if command == "0": 
                break
            
            # Add task
            elif command == "1": 
                print(self.__orders_list.add_task())

            # Print finished tasks
            elif command == "2": 
                if self.__orders_list.finished_tasks() == []:
                    print("no finished tasks")
                else: 
                    for task in self.__orders_list.finished_tasks():
                        print(task)

            # Print unfinished tasks
            elif command == "3":
                if self.__orders_list.unfinished_tasks() == []:
                    print("no unfinished tasks")
                else: 
                    for task in self.__orders_list.unfinished_tasks():
                        print(task)

            # Mark task as finished
            elif command == "4": 
                task_id = input("id: ")
                print(self.__orders_list.mark_finished(task_id))

            # Print programmers
            elif command == "5": 
                if self.__orders_list.programmers() == []:
                    print("no programmers")
                else: 
                    for programmer in self.__orders_list.programmers(): 
                        print(programmer)

            # Print programmer's status
            elif command == "6": 
                programmer_name = input("programmer: ")
                print(self.__orders_list.programmer_status(programmer_name))


application = OrderApplication()
application.execute()
