# Write your solution here
import urllib.request
import json

def retrieve_all(): 
    myRequest = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = myRequest.read()

    courses = json.loads(data)
    infoList = []
    for course in courses: 
        if course["enabled"] == True: 
            fullName = course['fullName']
            name = course['name']
            year = course['year']
            exercises = sum(course['exercises'])
            infoList.append((fullName, name, year, exercises))

    return infoList

def retrieve_course(course_name: str):
    myRequest = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = myRequest.read()

    courseInfo = json.loads(data)
    # print("--------")
    # for key,value in courseInfo.items(): 
    #     print(key)
    #     print(value)
    #     print()
    # print("--------")
    weeks = len(courseInfo)
    
    students = 0
    studentsAll = 0
    hours = 0 
    exercises = 0
    courseDict = {}

    for key, value in courseInfo.items():
        if value['students'] > students: 
            students = value['students']
        studentsAll += value['students']
        hours += value['hour_total']
        exercises += value['exercise_total']

    hoursAvg = hours // students 
    exercisesAvg = exercises // students

    courseDict['weeks'] = weeks
    courseDict['students'] = students
    courseDict['hours'] = hours
    courseDict['hours_average'] = hoursAvg
    courseDict['exercises'] = exercises
    courseDict['exercises_average'] = exercisesAvg

    return courseDict
        
if __name__ == "__main__":
    retrieve_all()
    print()
    print(retrieve_course("docker2019"))