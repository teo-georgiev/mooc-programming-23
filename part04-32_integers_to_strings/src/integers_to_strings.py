# Write your solution here
def formatted (numList: list): 
    secondList = []
    
    for item in numList: 
        secondList.append(f"{item:.2f}")

    return secondList

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
