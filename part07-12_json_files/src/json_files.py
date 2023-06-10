# Write your solution here
import json

# MODEL SOLUTION
# def print_persons(filename: str): 
#     with open(filename) as f: 
#         content = f.read()
#     persons = json.loads(content)
#     for person in persons: 
#         name = person['name']
#         age = person['age']
#         hobbies = ", ".join(person['hobbies'])
#         print(f"{name} {age} years ({hobbies})")

# MY SOLUTION
def print_persons(filename: str): 
    with open(filename) as newFile:
        data = newFile.read()
        
    students = json.loads(data)

    for student in students: 
        hobbiesSt = ""
        for i in range(len(student['hobbies'])): 
            if i < len(student['hobbies'])-1:
                hobbiesSt += f"{student['hobbies'][i]}, "
            else: 
                hobbiesSt += f"{student['hobbies'][i]}"
        print(f"{student['name']} {student['age']} years ({hobbiesSt})")

if __name__ == "__main__":
    students = print_persons("file1.json")

    
