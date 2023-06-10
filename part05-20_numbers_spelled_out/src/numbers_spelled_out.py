# Write your solution here
def numDigit(digit: int): 
    if digit == 0: return "zero"
    elif digit == 1: return "one"
    elif digit == 2: return "two"
    elif digit == 3: return "three"
    elif digit == 4: return "four"
    elif digit == 5: return "five"
    elif digit == 6: return "six"
    elif digit == 7: return "seven"
    elif digit == 8: return "eight"
    elif digit == 9: return "nine"

def numTeens(digit: int): 
    if digit == 10: return "ten"
    elif digit == 11: return "eleven"
    elif digit == 12: return "twelve"
    elif digit == 13: return "thirteen"
    elif digit == 14: return "fourteen"
    elif digit == 15: return "fifteen"
    elif digit == 16: return "sixteen"
    elif digit == 17: return "seventeen"
    elif digit == 18: return "eighteen"
    elif digit == 19: return "nineteen"

def numTens(digit: int): 
    if digit >= 2 and digit < 3: return "twenty"
    elif digit >= 3 and digit < 4: return "thirty"
    elif digit >= 4 and digit < 5: return "forty"
    elif digit >= 5 and digit < 6: return "fifty"
    elif digit >= 6 and digit < 7: return "sixty"
    elif digit >= 7 and digit < 8: return "seventy"
    elif digit >= 8 and digit < 9: return "eighty"
    elif digit >= 9: return "ninety"

def dict_of_numbers(): 
    numbers = {}
    for i in range(0, 100, 1): 
        if i >= 0 and i < 10: 
            numbers[i] = numDigit(i)
        elif i >= 10 and i < 20: 
            numbers[i] = numTeens(i)
        elif i >= 20: 
            x = i // 10 
            y = i % 10
            if y == 0: 
                z = numTens(x)
            else: 
                z = f"{numTens(x)}-{numDigit(y)}"
            numbers[i] = z

    return numbers


if __name__ == "__main__":
    numbers = dict_of_numbers()
    # for key, value in numbers.items(): 
    #     print("key: ", key, end=" | ")
    #     print("value: ", value)
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[30])

