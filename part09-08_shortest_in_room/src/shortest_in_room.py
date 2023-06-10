# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room: 
    def __init__(self):
        self.persons = []
        self.combined_height = 0
    
    def add(self, person: Person): 
        self.persons.append(person)
        self.combined_height += person.height

    def is_empty(self):
        if len(self.persons) == 0: 
            return True
        return False

    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {self.combined_height} cm")
        for person in self.persons: 
            print(f"{person.name} ({person.height} cm)")

    def shortest(self): 
        if self.is_empty() is not True:
            shortest_person = self.persons[0]
            for person in self.persons: 
                if person.height < shortest_person.height: 
                    shortest_person = person
            return shortest_person
        return None
        
    def remove_shortest(self): 
        if self.is_empty() is not True: 
            shortest_person = self.shortest()
            self.persons.remove(shortest_person)
            return shortest_person
        return None

def main():
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()

if __name__ == "__main__": 
    main()