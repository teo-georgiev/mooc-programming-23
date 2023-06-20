class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list): 
    return list(filter(lambda course : course.grade >= 1, attempts))

def attempts_with_grade(attempts: list, grade: int): 
    return list(filter(lambda course: course.grade == grade, attempts))

def passed_students(attempts: list, course: str): 
    # MODEL SOLUTION
    course_attempts = filter(lambda s: s.course_name == course and s.grade > 0, attempts)
    course_students = map(lambda s: s.student_name, course_attempts)
    return sorted(course_students)
    
    # # MY SOLUTION
    # students_passed = []
    # course_attempts = list(map(students_passed.append, accepted(attempts)))
    # students_names = sorted(list(map(lambda s: s.student_name, filter(lambda course_attempt: course_attempt.course_name == course, students_passed))))
    # return students_names

def main():
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)

        
if __name__ == "__main__": 
    main()