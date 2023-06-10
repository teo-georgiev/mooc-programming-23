# Write your solution here
def read_input(text, start, end): 
    while True: 
        try:
            number = int(input(text))
            if number >= start and number <= end: 
                return number
        except ValueError: 
            pass

        print(f"You must type in an integer between {start} and {end}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)