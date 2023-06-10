# Write your solution here
def histogram(word: str): 
    result = {}
    for letter in word: 
        if letter not in result: 
            result[letter] = "*"
        else: 
            result[letter] += "*"
        
    for key, value in result.items():
        print(key, value)

if __name__ == "__main__": 
    histogram("abba")