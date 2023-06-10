# Write your solution here
def create_tuple(x: int, y: int, z: int):
    holdTuple = (x, y, z)

    newTuple = (
        min(holdTuple), 
        max(holdTuple), 
        sum(holdTuple)
    )

    return newTuple

    # MODEL SOLUTION
    # smallest = min([x, y, z])
    # greatest = max([x, y, z])
    # numSum = sum([x, y, z])

    # return (smallest, greatest, numSum)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
