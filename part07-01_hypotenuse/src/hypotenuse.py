# Write your solution here
import math

def hypotenuse(leg1: float, leg2: float):
    hyp = leg1 ** 2 + leg2 ** 2
    hyp = math.sqrt(hyp)

    return hyp

if __name__ == "__main__": 
    print(hypotenuse(3,4)) # 5.0
    print(hypotenuse(5,12)) # 13.0
    print(hypotenuse(1,1)) # 1.4142135623730951
