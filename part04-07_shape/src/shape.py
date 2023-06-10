# Copy here code of line function from previous exercise and use it in your solution
def line(size :int, character :str):
    print(size * character)

def shape(size :int, text_1 :str, height :int, text_2 :str): 
    index = 0; 
    character = text_1

    while index <= size: 
        line(index, character)
        index += 1
    
    index = 0
    character = text_2
    while index < height: 
        line(size, character)
        index += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")