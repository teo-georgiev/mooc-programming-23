# Write your solution here
def sum_of_positives(nums: list):
    numSum = 0

    for i in range(0, len(nums), 1): 
        if nums[i] >= 0:
            numSum += nums[i]
        else: 
            continue
    
    return numSum

if __name__ == "__main__": 
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)