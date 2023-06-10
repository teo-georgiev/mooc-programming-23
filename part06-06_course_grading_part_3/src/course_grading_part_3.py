# write your solution here
studentInfo = input("Student information: ")
exercisesInfo = input("Exercises completed: ")
examInfo = input("Exam points: ")

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
        execData = []
        execNum = 0
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id": 
            continue

        for i in range(1, len(parts[1:]) + 1):
            execNum += int(parts[i]) # Exercise number
        execData.append(execNum)

        if execNum >= 0 and execNum != 40: 
            execPts = int((execNum * 10 // 4) // 10)
        elif execNum == 40: 
            execPts = 10
        execData.append(execPts)  # Exercise points

        exercises[parts[0]] = execData  # Exercise num + points

examPoints = {}
with open(examInfo) as newFile: 
    for line in newFile: 
        examPts = 0
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue

        for i in range(1, len(parts[1:]) + 1): 
            examPts += int(parts[i])

        examPoints[parts[0]] = examPts

print(f"{'name': <30}{'exec_nbr': <10}{'exec_pts.': <10}{'exm_pts.': <10}{'tot_pts.': <10}{'grade': <10}")

for id, name in names.items():
    if id in exercises: 

        execPts = exercises[id] # Exercises points
        
        examPts = examPoints[id] # Exam points

        totPts = execPts[1] + examPts # Total points
        
        # Grade
        if totPts > 0 and totPts <= 14: 
            grade = 0
        elif totPts > 14 and totPts <=17: 
            grade = 1
        elif totPts > 17 and totPts <= 20:
            grade = 2 
        elif totPts > 20 and totPts <= 23: 
            grade = 3 
        elif totPts > 23 and totPts <= 27: 
            grade = 4 
        else:
            grade = 5

        print(f"{name: <30}{execPts[0]: <10}{execPts[1]: <10}{examPts: <10}{totPts: <10}{grade: <10}")
    