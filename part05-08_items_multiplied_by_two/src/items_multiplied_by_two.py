# Write your solution here
def double_items(numbers: list): 
    numsDoubled = []

    for item in numbers:
        numsDoubled.append(item * 2)
    
    return numsDoubled

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
