# Write your solution here
def even_numbers(beginning: int, maximum: int): 
    if beginning % 2 != 0:
        number = beginning + 1
    else: 
        number = beginning
        
    while number <= maximum: 
        yield number
        number += 2

if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers: 
        print(number)