# Write your solution here

# MODEL SOLUTION 
def prime_numbers():
    number = 1
    while True: 
        if is_prime(number): 
            yield number
        number += 1
    
# Helper method for checking if number is prime
def is_prime(number: int):
    if number < 2: 
        return False
    # Possible divisor is between 2 and number-1
    if i in range(2,number):
        if number % i == 0: 
            return False
        return True

# # MY SOLUTION
# def is_prime(prime: int): 
#     for num in range(2, prime, 1): 
#         if prime % num == 0: 
#             return False
#     return True

# def prime_numbers(): 
#     prime = 2
#     while True:
#         if prime == 2: 
#             yield prime
#         prime += 1            
#         if is_prime(prime) == True: 
#             yield prime
#         elif is_prime(prime) == False: 
#             continue
        
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))