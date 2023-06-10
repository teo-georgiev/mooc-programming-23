# Write your solution here
from random import sample

def words(n: int, beginning: str):
    wordList = []

    with open("words.txt") as newFile: 
        for line in newFile: 
            line = line.replace("\n", "")
            if line.startswith(beginning): 
                wordList.append(line)
    
    try: 
        return sample(wordList, n)
    except ValueError:
        raise ValueError

if __name__ == "__main__": 
    word_list = words(3, "ca")
    for word in word_list:
        print(word)