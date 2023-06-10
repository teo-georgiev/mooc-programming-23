# Write your solution here
def same_chars(text: str, num1: int, num2: int):
    if (num1 < 0 or num1 > len(text) - 1) or (num2 < 0 or num2 > len(text) - 1):
        return False 
    
    if text[num1] == text[num2]:
        return True
    elif text[num1] != text[num2]: 
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))