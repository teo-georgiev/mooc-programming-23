# write your solution here
studentInfo = input("Student information: ")
exercisesInfo = input("Exercises completed: ")

names = {}
with open(studentInfo) as newFile: 
    for line in newFile:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id": 
            continue
        names[parts[0]] = f"{parts[1]} {parts[2]}"

exercises = {}

with open(exercisesInfo) as newFile: 
    
    for line in newFile:
        sum = 0
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id": 
            continue
        for i in range(1, len(parts[1:]) + 1):
            sum += int(parts[i])
        exercises[parts[0]] = sum

for id, name in names.items():
    if id in exercises: 
        exerciseSum = exercises[id]
        print(name, exerciseSum)
    else: 
        print("WRONG")
    