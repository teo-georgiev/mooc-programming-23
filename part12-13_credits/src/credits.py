from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

from functools import reduce

def sum_of_all_credits(attempts: list):
    return reduce(lambda course_credits, course: course_credits + course.credits, attempts, 0)

def sum_of_passed_credits(attempts: list): 
    courses_passed = list(filter(lambda course: course.grade > 0, attempts))
    all_courses = reduce(lambda course_credits, course: course_credits + course.credits, courses_passed, 0)
    return all_courses

def average(attempts: list): 
    courses_passed = list(filter(lambda course: course.grade > 0, attempts))
    avg_grade = (reduce(lambda course_grade, course: course_grade + course.grade, courses_passed, 0)) / len(courses_passed)
    return avg_grade

def main():
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)

if __name__ == "__main__":
    main()