# Write your solution here
def anagrams(strOne: str, strTwo: str): 
    # Check how many characters are the words 
    # Sort strings 
    # Compare sorted strings 

    inOrderOne = sorted(strOne)
    inOrderTwo = sorted(strTwo)

    for i in range(0, len(strOne), 1):
        if inOrderOne == inOrderTwo: 
            return True
        else: 
            return False
            break
        
if __name__ == "__main__": 
    print(anagrams("house", "mouse"))