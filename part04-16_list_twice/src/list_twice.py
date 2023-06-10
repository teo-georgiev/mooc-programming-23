# Write your solution here
numList = []

while True: 
    num = int(input("New item: "))
    if num == 0: 
        print("Bye!")
        break
    else: 
        numList.append(num)
        print(f"The list now: {numList}")
        print(f"The list in order: {sorted(numList)}")
        continue