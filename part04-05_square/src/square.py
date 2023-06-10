# Copy here code of line function from previous exercise

def line(size :int, character :str):
    print(size * character)

def square(size, character):
    # You should call function line here with proper parameters
    index = 0
    
    while index < size: 
        line(size, character)
        index += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")
