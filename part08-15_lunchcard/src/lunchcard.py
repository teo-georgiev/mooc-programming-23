# Write your solution here:
class LunchCard: 
    def __init__(self, balance: float):
        self.balance = balance
    
    def __str__(self) -> str:
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_lunch(self):
        if self.balance >= 2.6:
            self.balance -= 2.6

    def eat_special(self): 
        if self.balance >= 4.6: 
            self.balance -= 4.6

    def deposit_money(self, deposit: float): 
        if deposit >= 0: 
            self.balance += deposit
        else: 
            raise ValueError("You cannot deposit an amount of money less than zero")


card_peter = LunchCard(20)
card_grace = LunchCard(30)

card_peter.eat_special()
card_grace.eat_lunch()
print("Peter:", card_peter)
print("Grace:", card_grace)

card_peter.deposit_money(20)
card_grace.eat_special()
print("Peter:", card_peter)
print("Grace:", card_grace)

card_peter.eat_lunch()
card_peter.eat_lunch()
card_grace.deposit_money(50)

print("Peter:", card_peter)
print("Grace:", card_grace)