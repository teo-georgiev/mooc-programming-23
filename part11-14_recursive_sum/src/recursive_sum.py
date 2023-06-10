# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int): 
    if number <= 1: 
        return number
    
    return recursive_sum(number - 1) + number

if __name__ == "__main__": 
    result = recursive_sum(3)
    print(result)