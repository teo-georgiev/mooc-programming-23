# WRITE YOUR SOLUTION HERE:
class Car: 
    def __init__(self) -> None:
        self.__petrol_amount = 0
        self.__odometer = 0
    
    def fill_up(self):
        tank = 60 
        fill = tank - self.__petrol_amount
        self.__petrol_amount += fill

    def drive(self, km: int): 
        if km > self.__petrol_amount:
            km = self.__petrol_amount

        self.__odometer += km
        self.__petrol_amount -= km

    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol_amount} litres"

def main(): 
    car = Car()
    car.fill_up()
    print(car)
    car.drive(10)
    car.drive(20)
    car.drive(10)
    car.drive(20)
    car.drive(5)
    print(car)

if __name__ == "__main__": 
    main()