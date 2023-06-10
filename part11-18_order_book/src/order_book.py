# Write your solution here:

# # MODEL SOLUTION
# class Task: 
#     id = 0
#     @classmethod
#     def new_ide(cls):
#         Task.id += 1
#         return Task.id
    
#     def __init__(self, description, programmer, workload):
#         self.programmer = programmer
#         self.description = description
#         self.workload = workload
#         self.id = Task.new_id()
#         self.finished = False
    
#     def is_finished(self):
#         return self.finished
    
#     def mark_finished(self): 
#         self.finished = True

#     def __str__(self) -> str:
#         status = "NOT FINISHED" if not self.finished else "FINISHED"
#         return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

# class OrderBook: 
#     def __init__(self) -> None:
#         self.__tasks = []
    
#     def add_order(self, description, programmer, workload):
#         self.__tasks.append(Task(description, programmer, workload))

#     def all_orders(self):
#         return self.__tasks
    
#     def programmers(self):
#         return list(set([t.programmer for t in self.__tasks]))
    
    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id: 
                task.mark_finished()
                return 
        
#         # not correct
#         raise ValueError("wrong id")
    
#     def unfinished_orders(self): 
#         return [t for t in self.__tasks if not t.is_finished()]
    
#     def finished_orders(self):
#         return [t for t in self.__tasks if t.is_finished()]

#     def status_of_programmer(self, programmer: str):
#         if programmer not in self.programmers(): 
#             raise ValueError("Programmer does not exist")
        
#         finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished()]
#         not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished()]

#         finished_hours = sum(t.workload for t in finished_tasks)
#         not_finished_hours = sum(t.workload for t in not_finished_tasks)

#         return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)

# MY SOLUTION
class Task: 
    id = 0
    def __init__(self, description: str, programmer: str, workload: int, status: bool = False):
        self.description = description
        self.programmer = programmer
        self.workload = workload

        self.status = status
        self.status_text = "NOT FINISHED"

        Task.id = Task.id + 1
        self.id = Task.id 
    
    def __str__(self) -> str:
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status_text}"

    def is_finished(self): 
        return self.status
    
    def mark_finished(self): 
        self.status = True
        self.status_text = "FINISHED"

    def programmer_name(self):
        return self.programmer
    
    def id_num(self):
        return self.id 
    
    def workload_hours(self): 
        return self.workload

class OrderBook: 
    def __init__(self):
        self.orders = []

    # def __str__(self) -> str:
    #     return super().__str__()
    
    def add_order(self, description: str, programmer: str, workload: int):
        self.order = Task(description, programmer, workload)
        self.orders.append(self.order)

    def all_orders(self):
        return self.orders

    def programmers(self):
        programmers_list = []
        [programmers_list.append(self.order.programmer_name()) for self.order in self.orders if self.order.programmer_name() not in programmers_list]
        return programmers_list
        # return [*set([self.order.programmer_name() for self.order in self.orders])]

    def mark_finished(self, id: int): 
        for self.order in self.orders: 
            if self.order.id_num() == id:
                return self.order.mark_finished()
            else: continue
        
        raise ValueError("No task with the given id")
    
    def finished_orders(self):
        return [order for order in self.orders if order.is_finished() == True]

    def unfinished_orders(self):
        return [self.order for self.order in self.orders if self.order.is_finished() == False]
    
    def status_of_programmer(self, programmer: str):
        fin = 0
        unfin = 0
        sum_fin_h = 0
        sum_unfin_h = 0

        for self.order in self.orders: 
            if self.order.programmer_name() != programmer: 
                continue
            else: 
                if self.order.is_finished() == True: 
                    fin += 1
                    sum_fin_h += self.order.workload_hours()
                else: 
                    unfin += 1
                    sum_unfin_h += self.order.workload_hours()
        
        if fin == 0 and unfin == 0 and sum_fin_h == 0 and sum_unfin_h == 0: 
            raise ValueError("No such programmer")
        else: 
            return fin,unfin,sum_fin_h,sum_unfin_h

def main():

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)

if __name__ == "__main__": 
    main()