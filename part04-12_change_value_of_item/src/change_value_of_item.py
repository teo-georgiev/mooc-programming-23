# Write your solution here

newList = [1, 2, 3, 4, 5]
index = 0
value = 0

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    value = int(input("Value: "))
    newList[index] = value
    print(newList)