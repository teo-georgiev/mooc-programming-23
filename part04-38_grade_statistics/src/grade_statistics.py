# Write your solution here

def studentInfo():
    inputStudent = []
    while True: 
        allInfo = input("Exam points and exercises completed: ")
        if allInfo == "" or allInfo == " ": 
            break
        inputStudent.append(allInfo)

    return inputStudent

# Split of the EXAM POINTS

def splitPoints(inputStudent: list):
    stPoints = []
    for item in inputStudent: 
        x = item.split()
        stPoints.append(int(x[0]))
    
    return stPoints

def failExam(examPoints: list):
    failExam = 0

    for item in examPoints: 
        if item < 10: 
            failExam += 1
    
    return failExam

# Split of the EXERCISES COMPLETED 
# and conversion to EXERCISE POINTS

def splitExercises(inputStudent: list):
    stExercises = []

    for item in inputStudent: 
        y = item.split() # Number of completed exercises 
        z = int(y[1]) // 10 # Conversion of exercises to exercise points 
        stExercises.append(z)

    return stExercises

# All POINTS calculation

def allPoints(examPoints: list, exercisePoints): 
    studentPoints = []
    for i in range(0, len(examPoints), 1): 
        allPoints = examPoints[i] + exercisePoints[i]
        studentPoints.append(allPoints)
    
    return studentPoints

# GRADE calculation

def gradeStudents(allPoints: list):
    grade = []

    for i in range(0, len(allPoints), 1): 
        if allPoints[i] > 0 and allPoints[i] <= 14: 
            x = 0 
        elif allPoints[i] >= 15 and allPoints[i] <= 17:
            x = 1
        elif allPoints[i] >= 18 and allPoints[i] <= 20:
            x = 2
        elif allPoints[i] >= 21 and allPoints[i] <= 23:
            x = 3
        elif allPoints[i] >= 24 and allPoints[i] <= 27:
            x = 4
        elif allPoints[i] >= 28 and allPoints[i] <= 30:
            x = 5
        
        grade.append(x)
    
    return grade

# STATISTICS
def stats(allPoints: list, pointsSt: int, gradeSt: list): 
    print("Statistics:")
    
    # Points Average
    pointsSum = sum(allPoints) 
    ptAverage = pointsSum / len(allPoints)
    print(f"Points average: {ptAverage}")

    # Pass Percentage
    pointsFail = 0
    for i in range(0, len(gradeSt), 1):
        if gradeSt[i] == 0 or pointsSt[i] < 10:
            pointsFail += 1
    passPersentage = ((len(gradeSt) - pointsFail) / len(gradeSt)) * 100 
    print(f"Pass percentage: {passPersentage:.1f}")

    # Grade Distribution 
    x5 = x4 = x3 = x2 = x1 = x0 = 0 
    
    for i in range(0, len(gradeSt), 1): 
        if gradeSt[i] == 5 and pointsSt[i] >= 10: 
            x5 += 1
        elif gradeSt[i] == 4 and pointsSt[i] >= 10:
            x4 += 1
        elif gradeSt[i] == 3 and pointsSt[i] >= 10: 
            x3 += 1
        elif gradeSt[i] == 2 and pointsSt[i] >= 10: 
            x2 += 1
        elif gradeSt[i] == 1 and pointsSt[i] >= 10: 
            x1 += 1
        elif gradeSt[i] == 0 or pointsSt[i] < 10:
            x0 += 1
    
    print("Grade distribution:")
    print("  5: " + x5 * "*")
    print("  4: " + x4 * "*")
    print("  3: " + x3 * "*")
    print("  2: " + x2 * "*")
    print("  1: " + x1 * "*")
    print("  0: " + x0 * "*")  
    
# MAIN FUNCTION

def main(): 
    inputSt = studentInfo()
    pointsSt = splitPoints(inputSt)
    pointsFail = failExam(pointsSt)

    exercisesSt = splitExercises(inputSt)
    allPointsStudent = allPoints(pointsSt, exercisesSt)
    gradeSt = gradeStudents(allPointsStudent)

    stats(allPointsStudent, pointsSt, gradeSt)

# BODY 
main()