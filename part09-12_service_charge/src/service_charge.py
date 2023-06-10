# WRITE YOUR SOLUTION HERE:

class BankAccount: 
    def __init__(self, name: str, acc_num: str, balance: float) -> None:
        self.__name = name
        self.__acc_num = acc_num
        self.__balance = balance

    def deposit(self, amount: float): 
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float): 
        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self): 
        return self.__balance

    def __service_charge(self): 
        service_charge = 0.01 * self.__balance
        self.__balance -= service_charge

def main():
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)

if __name__ == "__main__": 
    main()