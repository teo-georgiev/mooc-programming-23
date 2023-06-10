# Write your solution here:

# MY SOLUTION
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person("name")
        self.__persons[name].add_number(number)
    
    def add_address(self, name: str, address: str):
        if not name in self.__persons: 
            self.__persons[name] = Person("name")
        self.__persons[name].add_address(address) 

    def get_entry(self, name: str):
        if name not in self.__persons:
            return f"number unknown\naddress unknown"
        return self.__persons[name]

    def all_entries(self):
        return self.__persons
    
class Person(): 
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = ""

        self.__person = {
            self.__name : [self.__numbers, self.__address]
        }
    
    def __str__(self) -> str:
        if self.__numbers == [] and self.__address == "":
            return None
        elif self.__numbers == [] and self.__address != "":
            return f"number unknown\n{self.__address}"
        elif self.__numbers != [] and self.__address == "":
            return f"{self.__numbers}\naddress unknown"
        else: 
            return f"{self.__numbers}\n{self.__address}"

    def name(self):
        return self.__name

    def numbers(self):
        if self.numbers == []: 
            return "number unknown"
        return self.__person[self.__name][0]
        
    def address(self): 
        if self.__address == "":
            return None
        return self.__person[self.__name][1]

    def add_number(self, number: str): 
        self.__person[self.__name][0].append(number)

    def add_address(self, address: str): 
        self.__address = address
        self.__person[self.__name][1] = self.__address    

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self): 
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        person_info = self.__phonebook.get_entry(name)
        print(person_info)
        # print(person_info[1])

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3": 
                self.add_address()
            else:
                self.help()

#  MODEL SOLUTION 
# class Person: 
#     def __init__(self, name: str) -> None:
#         self.__name = name 
#         self.__numbers = []
#         self.__address = None

#     def name(self): 
#         return self.__name
    
#     def number(self): 
#         return self.__numbers
    
#     def add_number(self, number: str): 
#         self.__numbers.append(number)

#     def add_address(self, address: str):
#         self.__address = address

# class PhoneBook: 
#     def __init__(self) -> None:
#         self.__persons = {}
    
#     def add_number(self, name: str, number: str): 
#         if not name in self.__persons:
#             self.__persons[name] = Person(name)
#         self.__persons[name].add_number(number)

#     def add_address(self, name: str, address: str):
#         if not name in self.__persons: 
#             self.__persons[name] = Person(name)
#         self.__persons[name].add_address(address)
    
#     def get_entry(self, name: str): 
#         if not name in self.__persons: 
#             return None
#         return self.__persons[name]
    
#     def all_entries(self):
#         return self.__persons
    
# class PhoneBookApplication:
#     def __init__(self) -> None:
#         self.__phonebook = PhoneBook()
    
#     def help(self):
#         print("commands: ")
#         print("0 exit")
#         print("1 add number")
#         print("2 search")
#         print("3 add address")

#     def add_address(self):
#         name = input("name: ")
#         address = input("address: ")
#         self.__phonebook.add_address(name, address)
    
#     def add_number(self):
#         name = input("name: ")
#         number = input("number: ")
#         self.__phonebook.add_number(name, number)

#     def search(self): 
#         name = input("name: ")
#         data = self.__phonebook.get_entry(name)
#         if data == None:
#             print("number unknown")
#             print("address unknown")
        
#         numbers = data.numbers()
#         if len(numbers) == 0: 
#             print("number unknown")
#         else: 
#             for number in numbers: 
#                 print(number)
#         address = data.address()
#         if address != None: 
#             print(address)
#         else: 
#             print("address unknown")
    
#     def execute(self):
#         self.help()
#         while True: 
#             print("")
#             command = input("command: ")
#             if command == "0":
#                 break
#             elif command == "1":
#                 self.add_number()
#             elif command == "2":
#                 self.search()
#             elif command == "3":
#                 self.add_address()
#             else:
#                 self.help()

# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()