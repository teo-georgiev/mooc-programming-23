# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers_all = []

    def add_number(self, number:int):
        self.numbers_all.append(number)

    def count_numbers(self):
        return len(self.numbers_all)
    
    def get_sum(self): 
        return sum(self.numbers_all)
    
    def average(self): 
        if not self.numbers_all:
            return 0.0
        else: 
            return self.get_sum() / self.count_numbers()
    
stats = NumberStats()
odd = NumberStats()
even = NumberStats()

print("Please type in integer numbers:")
while True: 
    num = int(input())
    if num == -1: 
        break

    stats.add_number(num)
    if num % 2 == 0: 
        even.add_number(num)
    elif num % 2 == 1: 
        odd.add_number(num)

print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())
    

