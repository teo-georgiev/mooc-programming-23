# Write your solution here
def even_numbers(nums: list): 
    evenList = []

    for i in range(0, len(nums), 1): 
        if nums[i] % 2 == 0:
            evenList.append(nums[i])
        else: 
            continue
    
    return evenList

if __name__ == "__main__": 
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
