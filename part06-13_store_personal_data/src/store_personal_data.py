# Write your solution here
def store_personal_data(people: tuple): 
    with open("people.csv", "a") as peopleList: 
        peopleList.write(f"{people[0]};{people[1]};{people[2]}\n")

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))
