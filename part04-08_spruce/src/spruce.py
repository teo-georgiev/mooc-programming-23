# Write your solution here
def spruce(size: int): 
    print("a spruce!")
    
    index = 1
    counter = 1
    side = 0

    while index <= size:
       side = (2 * size - counter) // 2
       print(side * " " + counter * "*" + side * " ")
       index += 1 
       counter += 2
    
    side = (2 * size - 1) // 2
    print(side * " " + 1 * "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(6)