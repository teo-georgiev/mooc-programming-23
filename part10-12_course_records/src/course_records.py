# tee ratkaisusi tänne
class Course:
    # course name 
    def __init__(self, course_name: str) -> None:
        self.__course_name = course_name
        self.__grade = 0
        self.__credits = 0    

        self._course_data = [self.__grade, self.__credits]
    
    def __str__(self) -> str:
        return f"{self.__course_name} ({self.__credits} cr) grade {self.__grade}"
        
    def course_name(self): 
        return self.__course_name

    def course_grade(self): 
        return self.__grade

    def course_credits(self): 
        return self.__credits

    def add_course_data(self, grade: int, credits: int): 
        self.__grade = grade
        self.__credits = credits

        self._course_data.append(self.__grade)
        self._course_data.append(self.__credits)

class CourseList: 
    def __init__(self) -> None:
        self.__courses = {} 

    def add_course(self, course_name: str, grade: int, credits: int): 
        if course_name not in self.__courses:
            self.__courses[course_name] = Course(course_name)

        if self.__courses[course_name].course_grade() == 0 or grade > self.__courses[course_name].course_grade():
            self.__courses[course_name].add_course_data(grade, credits) 
        else: 
            return
            
    def get_course(self, course_name: str):
        if course_name not in self.__courses: 
            return "no entry for this course"
        return self.__courses[course_name]
    
    def all_courses(self):
        return self.__courses

class CourseApplication: 
    def __init__(self) -> None:
        self.__course_list = CourseList()

    def help(self): 
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
    
    def statistics(self):
        completed_courses = 0
        total_credits = 0
        total_grade = 0
        all_courses = self.__course_list.all_courses()
        grades_distribution = {}

        for course, data in all_courses.items():
            completed_courses += 1
            data = self.__course_list.get_course(course)
            total_credits += data.course_credits()
            total_grade += data.course_grade()
            
            if data.course_grade() not in grades_distribution: 
                grades_distribution[data.course_grade()] = 0
            grades_distribution[data.course_grade()] += 1
        
        if completed_courses == 0:
            print("no completed courses")
        else:
            mean = total_grade / completed_courses
            mean = round(mean, 1)
            print(f"{completed_courses} completed courses, a total of {total_credits} credits")
            print(f"mean {mean}")
            
        print("grade distribution")

        for i in range(5, 0, -1): 
            if i not in grades_distribution: 
                print(f"{i}: {0 * 'x'}")
            else: 
                print(f"{i}: {int(grades_distribution[i]) * 'x'}")
                
    def execute(self): 
        self.help()
        while True: 
            print("")
            command = input("command: ")
            if command == "1": 
                course_name = input("course: ")
                grade = int(input("grade: "))
                credits = int(input("credits: "))
                self.__course_list.add_course(course_name, grade, credits)
            elif command == "2": 
                course_name = input("course: ")
                print(self.__course_list.get_course(course_name))
            elif command == "3": 
                self.statistics()
            elif command == "0": 
                break
            else: 
                print("Invalid command")
                self.help()
                continue


application = CourseApplication()
application.execute()
