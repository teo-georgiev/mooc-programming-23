class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here
def names_of_students(attempts: list): 
    students = map(lambda student: student.student_name, attempts)
    return students

def course_names(course_names: list): 
    # # MY SOLUTION
    courses_final = []
    courses = sorted(map(lambda course: course.course_name, attempts))
    [courses_final.append(course) for course in courses if course not in courses_final]
    return courses_final
    
    # # MODEL SOLUTION
    # names = map(lambda k: k.course_name, course_names)
    # # remove duplicates by using a set
    # return sorted(list(set(names)))

def main():        
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in course_names([s1, s2, s3]):
        print(name)

if __name__ == "__main__":
    main()
