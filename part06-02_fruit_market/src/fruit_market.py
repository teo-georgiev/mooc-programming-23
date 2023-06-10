# write your solution here
def read_fruits(): 
    fruitsDict = {}
    with open("fruits.csv") as newFile: 
        for line in newFile: 
            line = line.replace("\n", "")
            fruit = line.split(";")
            fruitsDict[fruit[0]] = float(fruit[1])
            
    return fruitsDict

if __name__ == "__main__": 
    print(read_fruits())