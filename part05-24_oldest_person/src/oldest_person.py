# Write your solution here
def oldest_person(people: list):
    # MODEL SOLUTION
    # oldest = people[0]
    # for person in people: 
    #     if person[1] < oldest[1]:
    #         oldest = person
    
    # return oldest[0]

    indexOld = 0
    oldest = 2023

    for index in range(0, len(people)): 
        if people[index][1] < oldest: 
            oldest = people[index][1]
            indexOld = index
        else: 
            continue
            
    return people[indexOld][0]

if __name__ == "__main__":
    p1 = ('Jacob', 2016)
    p2 = ('Harry', 2019)
    p3 = ('Oliver', 2012)
    p4 = ('Wendy', 2013)
    p5 = ('Jane Doe', 2020)
    people = [p1, p2, p3, p4, p5]

    print(oldest_person(people))
