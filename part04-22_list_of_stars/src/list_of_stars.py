# Write your solution here
def list_of_stars(starList: list): 
    for i in range(0, len(starList), 1): 
        print(starList[i] * "*")

if __name__ == "__main__": 
    list_of_stars([3, 7, 1, 1, 2])

