# Write your solution here
# ADD STUDENTS
def add_student(students: dict, name: str): 
    students[name] = ""
    return students

# ADD COURSES
def add_course(students: dict, name: str, course: tuple):
    if students[name] == "": 
        coursesList = []
        students[name] = coursesList
    else: 
        coursesList = students[name]

    marker = 0
    if course[1] > 0: 
        for index in range(len(coursesList)): 
            if course[0] in coursesList[index]:
                prevGrade = coursesList[index]
                if prevGrade[1] < course[1]: 
                    coursesList[index] = course
                marker = 1
                break
        if marker != 1: 
            coursesList.append(course)
        students[name] = coursesList

    return students[name]

# PRINT STUDENTS
def print_student(students: dict, name: str): 
    avgGrade = 0
    if name in students: 
        counter = len(students[name])

    if name in students and counter >= 0:
        courseSum = 0
        for course in students[name]: 
            courseSum += course[1]
        if counter > 0: 
            avgGrade = courseSum / counter

    if name not in students: 
        print(f"{name}: no such person in the database")
    else: 
        print(f"{name}:")
        if students[name] == "" or counter == 0:
            print(f" no completed courses")
        else:
            print(f" {counter} completed courses:")
            for course in students[name]: 
                print(f"  {course[0]} {course[1]}")
            print(f" average grade {avgGrade}")

# SUMMARY
def summary(students: dict):
    # NUMBER OF STUDENTS
    counter = len(students)
    print(f"students {counter}")

    # MOST COURSES
    mostCourses = 0
    name = ""
    for key, value in students.items():
        if len(value) > mostCourses: 
            mostCourses = len(value)
            name = key 
    print(f"most courses completed {mostCourses} {name}")

    # BEST AVERAGE
    bestAvg = 0
    name = ""
    for key, value in students.items():
        avg = 0
        sum = 0
        for course in value: 
            sum = sum + course[1]
        avg = sum / len(value)
        if avg > bestAvg:
            bestAvg = avg
            name = key
    print(f"best average grade {bestAvg} {name}")      

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Emily")
    print_student(students, "Peter")
    print_student(students, "Emily")
    print_student(students, "Andy")

    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    add_course(students, "Emily", ("Introduction to Programming", 5))
    print_student(students, "Peter")
    summary(students)