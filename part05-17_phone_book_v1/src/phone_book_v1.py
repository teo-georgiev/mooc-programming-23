# Write your solution here
phoneBook = {}

while True: 
    command = int(input("command (1 search, 2 add, 3 quit): "))
    
    if command == 1: 
        #search 
        name = input("name: ")
        if name not in phoneBook: 
            print("no number")
        else: 
            print(phoneBook[name])
    elif command == 2: 
        name = input("name: ")
        number = input("number: ")
        phoneBook[name] = number
        print("ok!")
    else: 
        print("quitting...")
        break