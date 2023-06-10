# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    # MODEL SOLUTION
    # Helper method for returning the value in cents
    # --> makes the comparison easier
    def __value(self): 
        return self.__euros * 100 + self.__cents
    
    # Another helper mmethod which converts cents to value
    def __set_value(self, cents: int): 
        self.__euros = cents // 100
        self.__cents = cents - self.__euros * 100
    
    def __eq__(self, other: "Money") -> bool:
        return self.__value() == other.__value()
    
    def __lt__(self, other: "Money") -> bool: 
        return self.__value() < other.__value()
    
    def __gt__(self, other: "Money") -> bool: 
        return self.__value() < other.__value()
    
    def __ne__(self, other: "Money") -> bool: 
        return self.__value() != other.__value()
    
    def __add__(self, other: "Money") -> bool: 
        msum = Money(0, 0)
        msum.__set_value(self.__value() + other.__value())
        return msum
    
    def __sub__(self, other: "Money") -> bool:
        difference = self.__value() - other.__value()
        if difference < 0: 
            raise ValueError("a negative result is not allowed")
        dmoney = Money(0, 0)
        dmoney.__set_value(self.__value() - other.__value())
        return dmoney
    
    # MY SOLUTION
    # def __eq__(self, value: object) -> bool:
    #     return self.__euros == value.__euros and self.__cents == value.__cents
    
    # def __lt__(self, value: object) -> bool: 
    #     return self.__euros < value.__euros or (self.__euros == value.__euros and self.__cents < value.__cents)
    
    # def __gt__(self, value: object) -> bool: 
    #     return self.__euros > value.__euros or (self.__euros == value.__euros and self.__cents > value.__cents)

    # def __ne__(self, value: object) -> bool:
    #     return self.__euros != value.__euros or self.__cents != value.__cents
    
    # def __add__(self, value: object): 
    #     new_value = Money(euros=0, cents=0)
    #     new_value.__euros = self.__euros + value.__euros 
    #     new_value.__cents = self.__cents + value.__cents

    #     if new_value.__cents >= 100:
    #         new_value.__euros += 1
    #         new_value.__cents = new_value.__cents - 100
        
    #     return new_value

    # def __sub__(self, value: object):
    #     new_value = Money(euros=0, cents=0)
    #     new_value.__euros = self.__euros - value.__euros 
    #     new_value.__cents = self.__cents - value.__cents

    #     if new_value.__cents < 0:
    #         new_value.__euros -= 1
    #         new_value.__cents = 100 - abs(new_value.__cents)
    #     if new_value.__euros < 0: 
    #         raise ValueError("a negative result is not allowed")
        
    #     return new_value

def main(): 
    e1 = Money(15, 95)
    e2 = Money(15, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    # e5 = e2-e1
    
if __name__ == "__main__": 
    main()