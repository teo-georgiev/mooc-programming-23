# Write your solution here
def length(myList: list):
    listLength = len(myList)
    return listLength

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(f"The length is {result}")