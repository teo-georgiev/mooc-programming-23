# Write your solution here
def filter_incorrect(): 
    correctNums = {}
    with open("lottery_numbers.csv") as newFile: 
        for line in newFile: 
            line = line.replace("\n", "")
            parts = line.split(";")
            check = True

            # Checking 
            weekData = parts[0].split(" ")
            try:
                weekNum = int(weekData[1])
            except ValueError: 
                continue

            lotteryNums = parts[1].split(",")
            for num in lotteryNums: 
                try: 
                    num = int(num)
                    if num < 1 or num > 39: 
                        check = False
                        continue
                except ValueError: 
                    check = False 
                    continue

            for i in range(len(lotteryNums)):
                if lotteryNums[i] in lotteryNums[i + 1 : ]: 
                    check = False
                    break
            
            if len(lotteryNums) < 7 or check == False: 
                continue

            correctNums[parts[0]] = parts[1]
    
    with open("correct_numbers.csv", "w") as newFile:     
        for key, value in correctNums.items(): 
            newFile.write(f"{key};{value}\n")
        
if __name__ == "__main__": 
    
    filter_incorrect()