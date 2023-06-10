# Write your solution here
from fractions import Fraction

def fractionate(amount: int): 
    # MY SOLUTION
    fract = []
    for i in range(0, amount, 1): 
        fract.append(Fraction(1, amount))

    return fract

    # MODEL SOLUTION 
    # fraction = Fraction(1, amount)
    # return [fraction] * amount

if __name__ == "__main__": 
    print(fractionate(5))