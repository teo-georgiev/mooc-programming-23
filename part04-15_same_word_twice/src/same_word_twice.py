# Write your solution here
wordList = []
word = ""

while True: 
    word = input("Word: ")
    if word in wordList: 
        break
    else: 
        wordList.append(word)

print(f"You typed in {len(wordList)} different words")