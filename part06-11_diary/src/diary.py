# Write your solution here

while True: 
    print("1 - add an entry, 2 - read entries, 0 - quit")
    option = int(input("Function: "))
    if option == 1: 
        with open("diary.txt", "a") as diaryEntry:
            entry = input("Diary entry: ")
            diaryEntry.write(f"{entry}\n")
            print("Diary saved\n")
        continue
    elif option == 2:
        print("Entries:")
        with open("diary.txt") as diaryEntry: 
            for line in diaryEntry: 
                print(line)
        continue
    elif option == 0: 
        print("Bye now!")
        break
    else: 
        continue 