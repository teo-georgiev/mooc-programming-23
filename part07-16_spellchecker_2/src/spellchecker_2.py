# Write your solution here
from difflib import get_close_matches

with open("wordlist.txt") as wordsDoc: 
    
    txt = input("Write text: ")
    wordParts = txt.split(" ")
    
    txtCheck = ""
    wordList = []
    wrongWords = []

    for line in wordsDoc: 
        line = line.replace('\n', '')
        wordList.append(line)

    for word in wordParts: 
        if word.lower() in wordList:
            txtCheck += f"{word} "
            continue
        else: 
            txtCheck += f"*{word}* "
            wrongWords.append(word)
            continue

    print(txtCheck)
    print("suggestions:")

    possibilities = {}
    for wrong in wrongWords: 
        closeMatches = get_close_matches(wrong, wordList)
        matches = ", ".join(closeMatches)
        print(f"{wrong}: {matches}")