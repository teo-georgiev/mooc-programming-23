# Write your solution here
from datetime import timedelta, datetime
import csv

# If the name is not in the dictionary 
    # We add the name as a new nested dictionary 
    # the nexted dictionary contains: 
        # start time : start_time value
        # task num: points, end_time 
            # check if task already exists. If it exists in the cirectory, we compare the points and add the higher one 
            # check if the end_time is longer than 3 hours after the start time. If it is, task receives 0 points. 
        # total points : tot_pts we add all the points towards that 

# MODEL SOLUTION
# def final_points():
#     with open("start_times.csv") as start, open("submissions.csv") as submission: 
#         start_times = {}
#         # First read students and start times to memory 
#         for row in csv.reader(start, delimiter=";"):
#             name = row[0]
#             time = datetime.strptime(row[1], "%H:%M")
#             start_times[name] = time

#         # Then read submissions
#         # From each student time and points is saved to a dictionary 
#         # Time and points is saved as tuple. 
        
#         points = {}
#         for row in csv.reader(submission, delimiter = ";"): 
#             name = row[0]
#             tno = int(row[1])
#             p = int(row[2])
#             time = datetime.strptime(row[3], "%H:%M")

#             # If cheating has happened, submission is not handled
#             if time - start_times[name] > timedelta(hours=3): 
#                 continue

#             # If student isj not hadled yet, add student directly to the dictionary 
#             if name not in points: 
#                 default_time = datetime(1900, 1, 1)
#                 points[name] = {}
#                 for i in range(1, 8+1): 
#                     points[name][i] = 0
#                 points[name][tno] = p

#             # If student already exists, more points than earlier is required 
#             elif p > points[name][tno]:
#                 points[name][tno] = p

#         final_points = {}
#         # Iterate through students one by one 
#         for student in points: 
#             p = 0
#             for exercise in points[student]: 
#                 p += points[student][exercise]
#             final_points[student] = p

#         return final_points

# MY SOLUTION
def final_points(): 
    start_times = {}
    student_submissions = {}

    with open("start_times.csv") as newFile: 
        for line in csv.reader(newFile, delimiter=";"):
            name = line[0]
            startTime = datetime.strptime(line[1], "%H:%M")
            start_times[name] = startTime

    with open("submissions.csv") as newFile: 
        for line in csv.reader(newFile, delimiter=";"):
            name = line[0]
            task = line[1]
            points = int(line[2])
            endTime = datetime.strptime(line[3], "%H:%M")

            if name not in student_submissions: 
                student_submissions[name] = {}

            student_submissions[name]["start time"] = start_times[name]
            
            if endTime - start_times[name] <= timedelta(hours=3): 
                if task not in student_submissions[name]: 
                    student_submissions[name][task] = [points, endTime]
                else: 
                    if student_submissions[name][task][0] < points: 
                        student_submissions[name][task][0] = points
        
        finalPoints = {}

        for key, value in student_submissions.items():
            totPts = 0
            print(key)
            for key1, value1 in student_submissions[key].items():
                if key1 != "start time": 
                    totPts += student_submissions[key][key1][0]
                print(f"{key1} : {value1}")
            finalPoints[key] = totPts
            print(f"FINAL POINTS : {finalPoints[key]}")
            print("------")

    return finalPoints

if __name__ == "__main__":
    
    studentsAll = final_points()