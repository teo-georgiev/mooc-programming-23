# Write your solution here:
class Item: 
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def weight(self): 
        return self.__weight
    
    def name(self): 
        return self.__name
    
    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase: 
    def __init__(self, max_weight: int) -> None:
        self.__max_weight = max_weight
        self.__tot_weight = 0
        self.__items = []

    def add_item(self, item: Item):
        if item.weight() < self.__max_weight - self.__tot_weight: 
            self.__items.append(item)
            self.__tot_weight += item.weight()
            
    def weight(self): 
        return self.__tot_weight
    
    def heaviest_item(self): 
        heaviest_item = self.__items[0]
        for i in range(1, len(self.__items)): 
            if self.__items[i].weight() > heaviest_item.weight(): 
                heaviest_item = self.__items[i]
            else: continue
        
        return heaviest_item
    
    def print_items(self): 
        for item in self.__items: 
            print(f"{item.name()} ({item.weight()} kg)") 

    def __str__(self) -> str:
        if len(self.__items) == 1: 
            return f"{len(self.__items)} item ({self.__tot_weight} kg)"
        return f"{len(self.__items)} items ({self.__tot_weight} kg)"

class CargoHold: 
    def __init__(self, max_weight: int) -> None:
        self.__max_weight = max_weight
        self.__tot_cargo_weight = 0
        self.__suitcases = []

    def add_suitcase(self, suitcase: Suitcase): 
        if suitcase.weight() < self.__max_weight - self.__tot_cargo_weight:
            self.__suitcases.append(suitcase)
            self.__tot_cargo_weight += suitcase.weight()

    def print_items(self): 
        for suitcase in self.__suitcases: 
            suitcase.print_items()

    def __str__(self) -> str:
        remaining_space = self.__max_weight - self.__tot_cargo_weight
        if len(self.__suitcases) == 1: 
            return f"{len(self.__suitcases)} suitcase, space for {remaining_space} kg"    
        return f"{len(self.__suitcases)} suitcases, space for {remaining_space} kg"

if __name__ == "__main__": 
    
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()