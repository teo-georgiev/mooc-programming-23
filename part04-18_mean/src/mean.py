# Write your solution here
def mean(myList: list): 
    listLength = len(myList)
    listSum = sum(myList)
    result = listSum / listLength
    return result

# You can test your function by calling it within the following block
if __name__ == "__main__":
    myList = [3, 6, -4]
    result = mean(myList)
    print(result)