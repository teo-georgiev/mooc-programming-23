# Write your solution here
def longest_series_of_neighbours(numbers: list): 
    counter = 1
    highest = 1

    for i in range(0, len(numbers) - 1, 1): 
        if numbers[i] - numbers[i + 1] == 1 or numbers[i] - numbers[i + 1] == -1: 
            counter += 1
            if counter > highest: 
                highest += 1
        else:
            counter = 1
            continue
    
    return highest

if __name__ == "__main__": 
    my_list = [0, 2, 4, 5, 6, 7, 10, 11, 12, 100, 101]
    print(longest_series_of_neighbours(my_list))
