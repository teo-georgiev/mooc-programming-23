# Write your solution here

def distinct_numbers(listNumbers: list): 
    distList = []
    for i in range(0, len(listNumbers), 1):
        if listNumbers[i] in distList: 
            continue
        else: 
            distList.append(listNumbers[i])
            continue
    
    distList.sort()
    return distList

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))