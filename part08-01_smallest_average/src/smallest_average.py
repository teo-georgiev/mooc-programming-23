# Write your solution here

# MODEL SOLUTION
# def average(person: dict): 
#     ex_sum = person["result1"] + person["result2"] + person["result3"]
#     return ex_sum / 3

# def smallest_average(person1: dict, person2: dict, person3: dict): 
#     smallest = person1 
#     if average(person2) < average(smallest): 
#         smallest = person2
    
#     if average(person3) < average(smallest): 
#         smallest = person3
    
#     return smallest

# MY SOLUTION 
def calculate_average(person: dict): 
    avg = 0
    for key, value in person.items():
        if key != "name": 
            avg += value
    
    avg = avg / (len(person) - 1)
    avg = round(avg, 2)
    return avg

def smallest_average(person1: dict, person2: dict, person3: dict): 
    people = {}
    people["person1"] = person1
    people["person2"] = person2
    people["person3"] = person3

    people_averages = []
    people_averages.append(calculate_average(person1))
    people_averages.append(calculate_average(person2))
    people_averages.append(calculate_average(person3))
    min_avg = min(people_averages)
    indexMin = f"person{int(people_averages.index(min_avg)) + 1}"

    return people[indexMin]

if __name__ == "__main__": 
    person1 = {"name": "Mary", "result1": 1,"result2": 1,"result3": 1}
    person2 = {"name": "Gary", "result1": 2,"result2": 2,"result3": 2}
    person3 = {"name": "Larry", "result1": 3,"result2": 3,"result3": 3}

    print(smallest_average(person1, person2, person3))