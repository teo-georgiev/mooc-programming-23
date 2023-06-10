# WRITE YOUR SOLUTION HERE:
class SimpleDate: 
    def __init__(self, day: int, month: int, year: int) -> None:
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self) -> str:
        return f"{self.__day}.{self.__month}.{self.__year}"
    
    def vaulue(self): 
        return (self.__year * 12) * 30 + self.__month * 30 + self.__day 

    def __lt__(self, other: "SimpleDate"):
        return self.vaulue() < other.vaulue()

    def __gt__(self, other: "SimpleDate"):
        return self.vaulue() > other.vaulue()

    def __eq__(self, other: "SimpleDate"):
        return self.vaulue() == other.vaulue()

    def __ne__(self, other: "SimpleDate"):
        return self.vaulue() != other.vaulue()
    
    def __add__(self, value_days): 
        new_value = self.vaulue() + value_days

        new_year = new_value // 360
        new_month = (new_value % 360) // 30
        new_day = (new_value % 360) % 30
        
        new_date = SimpleDate(new_day, new_month, new_year)

        return new_date
    
    def __sub__(self, other: "SimpleDate"): 
        return abs(self.vaulue() - other.vaulue())

def main():
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)

if __name__ == "__main__": 
    main()
