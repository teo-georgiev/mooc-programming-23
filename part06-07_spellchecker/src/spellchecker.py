# # write your solution here
text = input("Write text: ")
wordList = []

with open("wordlist.txt") as wordTest: 
    for line in wordTest: 
        line = line.strip()
        wordList.append(line)

textWords = text.split(" ")
newText = ""
for word in textWords: 
    check = word.lower()
    if check in wordList: 
        newText += f"{word} "
    else: 
        newText += f"*{word}* "

print(newText)