# Write your solution here
def line(num :int, text :str):
    if len(text) > 0:
        print(num * text[0])
    else: 
        print(num * "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")