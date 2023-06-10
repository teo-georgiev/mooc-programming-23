# Write your solution here
itemsNum = int(input("How many items: "))
myList = []
number = 0
index = 0

while index < itemsNum:
    num = int( input(f"Item {index + 1}: ") )
    myList.append(num)
    index += 1 

print(myList)
