# write your solution here
def largest():
    largestNum = ""
    with open("numbers.txt") as new_file: 
        for line in new_file: 
            if line > largestNum: 
                largestNum = line 
            else: 
                continue
    return int(largestNum)

if __name__ == "__main__": 
    print(largest())