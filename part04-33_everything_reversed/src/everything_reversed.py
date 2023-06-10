# Write your solution here
def everything_reversed(wordList: list): 
    revList = []

    for item in wordList: 
        revList.append(item[::-1])

    return revList[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
