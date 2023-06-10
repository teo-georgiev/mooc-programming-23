# Write your solution here
def greatest_number(x: int, y: int, z: int): 
    if x >= y and x >= z: 
        return x 
    elif x <= y and y <= z: 
        return z
    else: 
        return y


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)