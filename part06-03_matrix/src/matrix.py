# write your solution here

def sums(sum, num): 
    sum += int(num)
    return sum

def greatest(max, num): 
    if int(num) > max: 
        max = int(num)
    return max

def matrix_sum():
    with open("matrix.txt") as fileMatrix: 
        sum = 0
        for line in fileMatrix: 
            line = line.replace("\n", "")
            row = line.split(",")
            for num in row:
                sum = sums(sum, num) 
        return sum

def matrix_max(): 
    with open("matrix.txt") as fileMatrix: 
        max = 0
        for line in fileMatrix: 
            line = line.replace("\n", "")
            row = line.split(",")
            for num in row:
                max = greatest(max, num)
        return max

def row_sums():
    with open("matrix.txt") as fileMatrix: 
        rowSumsList = []
        for line in fileMatrix: 
            line = line.replace("\n", "")
            row = line.split(",")
            sum = 0
            for num in row:
                sum = sums(sum, num) 
            rowSumsList.append(sum)
        return rowSumsList

if __name__ == "__main__":
        print("Sum of numbers:", matrix_sum())
        print("Greatest number:", matrix_max())
        print("Sums of rows:", row_sums())
    
