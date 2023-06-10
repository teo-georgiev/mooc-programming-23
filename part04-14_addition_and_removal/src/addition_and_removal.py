# Write your solution here
myList = []
optionList = ""
index = 0

while True: 
    print(f"The list is now {myList}")
    option = input("a(d)d, (r)emove or e(x)it: ")
    if option == "d": 
        myList.append(index + 1)
        index += 1
    elif option == "r": 
        myList.pop(index - 1)
        index -= 1
    elif option == "x":
        print("Bye!")
        break
    else: 
        continue