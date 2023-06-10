# Write your solution here
from datetime import datetime, timedelta

# MY SOLUTION
while True:
    fileName = input("File name: ")
    startDate = input("Starting date: ")
    daysNum = int(input("How many days: "))

    # Splitting the user input date in order to 
    # get the values for the datetime formatting 
    startDate = startDate.split(".")
    daySplit = int(startDate[0])
    monthSplit = int(startDate[1])
    yearSplit = int(startDate[2])

    # Checking if the input date is valid
    try: 
        startDate = datetime(yearSplit, monthSplit, daySplit)
        break
    except ValueError: 
        continue

scrTimeDates = startDate

print("Please type in screen time in minutes on each day (TV computer mobile):")
dailyTime = []


# for i in range(0, daysNum, 1):
i = 0
while i < daysNum:
    while True: 
        scrTime = f"{scrTimeDates.strftime('%d.%m.%Y')}"
        x = input(f"Screen time {scrTime}: ")
        check = x.split(" ")
        if len(check) != 3: 
            continue
        else: 
            dailyTime.append(x)
            scrTimeDates += timedelta(days=1)
            i += 1
            break

with open(fileName, "w") as newFile: 

    scrTimeDates -= timedelta(days=1)
    scrTime = f"{scrTimeDates.strftime('%d.%m.%Y')}"
    newFile.write(f"Time period: {startDate.strftime('%d.%m.%Y')}-{scrTime}\n")


    scrTimeDates = startDate
    minsTot = 0
    avgMins = 0
    timeLogs = []

    for i in range(0, daysNum, 1):
        # Total minutes calculation
        mins = dailyTime[i].split(" ")
        mins = list(map(int, mins))
        minsTot += sum(mins)

        # Timelogs display
        scrTime = f"{scrTimeDates.strftime('%d.%m.%Y')}"
        dailyTime[i] = dailyTime[i].replace(" ", "/")
        timeLogs.append(f"{scrTime}: {dailyTime[i]}")
        scrTimeDates += timedelta(days=1)

    avgMins += minsTot / daysNum

    newFile.write(f"Total minutes: {minsTot}\n")
    newFile.write(f"Average minutes: {avgMins:.1f}\n")
    for i in range(0, daysNum, 1):
        newFile.write(f"{timeLogs[i]}\n")
    print(f"Data stored in file {fileName}")

# -------------------
# # MODEL SOLUTION
# week = timedelta(days=7)
# def format(aika): 
#     return aika.strftime("%d.%m.%Y")

# file = input("Filename: ")
# start = input("Starting date: ").split(".")
# days = int(input("How many days: "))
# print("Please type in screen time in minutes on each day (TV computer mobile):")

# screen_time = []
# total = 0
# start = datetime(int(start[2]), int(start[1]), int(start[0]))

# for i in range(days): 
#     day = start + timedelta(days=i)
#     times = input(f"Screen time {format(day)}: ").split(" ")
#     tv = int(times[0])
#     pc = int(times[1])
#     mobile = int(times[2])
#     total += tv + pc + mobile
#     screen_time.append((day, tv, pc, mobile))

# with open(file, "w") as tdsto: 
#     tdsto.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
#     tdsto.write(f"Total minutes: {total}\n")
#     tdsto.write(f"Average minuts: {total/days:.1f}\n")
#     for pv, tv, pc, mob in screen_time:
#         tdsto.write(f"{format(pv)}: {tv}/{pc}/{mob}\n")

# print(f"Data stored in file {file}")
