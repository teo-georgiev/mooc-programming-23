# Write your solution here

def palindromes (word): 
    mainWord = list(word)
    invWord = []

    for i in range(len(mainWord) - 1, -1, -1): 
        invWord.append(mainWord[i])

    if mainWord == invWord: 
        return True
    else: 
        return False

def play(): 
    while True: 
        word = input("Please type in a palindrome: ")
        if palindromes(word): 
            print(f"{word} is a palindrome! ")
            break
        else: 
            print("that wasn't a palindrome ")

play()



# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
 