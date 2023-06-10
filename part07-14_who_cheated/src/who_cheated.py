# Write your solution here
import datetime
from datetime import timedelta
import csv

# MODEL SOLUTION
# def cheaters(): 
#     with open("start_times.csv") as start, open("submissions.csv") as submission: 
        # start_times = {}
        # # First read students and start times to memory
        # for row in csv.reader(start, delimiter=";"):
        #     name = row[0]
        #     time = datetime.strptime(row[1], "%H:%M")
        #     start_times[name] = time

        # # Then read sumissions 
        # # For each student, last (i.e. greatest) is saved
        # submission_times = {}
        # for row in csv.reader(submission, delimiter=";"):
        #     name = row[0]
        #     time = datetime.strptime(row[3], "%H:%M")
        #     # If name does not exist in dictionary, add time directly to dictionary
        #     if name not in submission_times: 
        #         submission_times[name] = time
        #     # IF there already exists time for key, compare if currect time is greater
        #     elif time > submission_times[name]: 
        #         submission_times[name] = time
        
        # cheaters = []
        # # Iterate through students one by one 
        # for name in start_times: 
        #     if submission_times[name] - start_times[name] > timedelta(hours=3): 
        #         cheaters.append(time)
            
        # return cheaters

# MT SOLUTION
def cheaters(): 

    with open("start_times.csv") as startFile, open("submissions.csv") as submisFile: 
        startInfo = {}
        for line in startFile: 
            line = line.replace("\n", "")
            parts = line.split(";")
            startInfo[parts[0]] = parts[1]

        for key, value in startInfo.items(): 
            
            hours = int(value[0:2])
            mins = int(value[3:])
            startInfo[key] = datetime.datetime(1, 1, 1, hour=hours, minute=mins)

        cheaters = []
        for line in submisFile: 
            line = line.replace("\n", "")
            parts = line.split(";")
            
            hoursEnd = int(parts[3][0:2])
            minsEnd = int(parts[3][3:])
            parts[3] = datetime.datetime(1, 1, 1, hour=hoursEnd, minute=minsEnd)
            
            testTime = timedelta(hours=3)

            if parts[0] in startInfo and parts[0] not in cheaters: 
                if startInfo[parts[0]] + testTime < parts[3]:
                    cheaters.append(parts[0])

        return cheaters

if __name__ == "__main__":
    print(cheaters())

    # PSEUDO CODE
    # startInfo contains all the information about the name and the starting times
    # open the "submissions.csv" file as submissionsFile: 
    # go through each line with a loop 
    # split the line based on ";"
    # check for the [0] item inside the dictionary from startFile 
    # if it's in the startFile, grab the [3] item from the submissionsFile
    # split it along the ":" character
    # convert the two values into a datetime object
    # if hour from startFile time object + 3 > submissionsFile time object
        # add the name of the person to a cheater list
        # else: continue


# [
# 'justiina', 'esko', 'tiina', 'jyrki', 'teemu', 'johannes', 
# 'kjell', 'luukas', 'antti', 'virpi', 'kotivalo', 'matti', 
# 'arto', 'henrik', 'liisa'
# ]