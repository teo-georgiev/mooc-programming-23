# wwite your solution here
if True:  
    studentInfo = input("Student information: ")
    exercisesInfo = input("Exercises completed: ")
    examInfo = input("Exam points: ")
else: 
    studentInfo = "students1.csv"
    exercisesInfo = "exercises1.csv"
    examInfo = "exam_points1.csv"

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
        if sum >= 0 and sum != 40: 
            exercisePoints = int((sum * 10 // 4) // 10)
        elif sum == 40: 
            exercisePoints = 10
        exercises[parts[0]] = exercisePoints

examPoints = {}
with open(examInfo) as newFile: 
    for line in newFile: 
        sum = 0
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        for i in range(1, len(parts[1:]) + 1): 
            sum += int(parts[i])
        examPoints[parts[0]] = sum

for id, name in names.items():
    if id in exercises: 
        exerciseSum = exercises[id]
        examSum = examPoints[id]
        allPointsSum = exerciseSum + examSum
        if allPointsSum > 0 and allPointsSum <= 14: 
            grade = 0
        elif allPointsSum > 14 and allPointsSum <=17: 
            grade = 1
        elif allPointsSum > 17 and allPointsSum <= 20:
            grade = 2 
        elif allPointsSum > 20 and allPointsSum <= 23: 
            grade = 3 
        elif allPointsSum > 23 and allPointsSum <= 27: 
            grade = 4 
        else:
            grade = 5

        print(name, grade)
    