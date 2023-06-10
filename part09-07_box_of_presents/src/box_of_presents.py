# WRITE YOUR SOLUTION HERE:
class Present: 
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight
    
    def __str__(self) -> str:
        return f"{self.name} ({self.weight})"

class Box: 
    def __init__(self) -> None:
        self.presents = []

    def add_present(self, present: Present): 
        self.presents.append(present)
    
    def total_weight(self): 
        weight = 0
        for present in self.presents: 
            weight += present.weight

        return weight

def main(): 
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())

if __name__ == "__main__": 
    main()