# Write your solution here:

class Stopwatch: 
    def __init__(self): 
        self.seconds = 0
        self.minutes = 0
    
    def tick(self): 
        self.seconds += 1
        if self.seconds == 60: 
            self.seconds = 0
            self.minutes += 1 
            if self.minutes == 60: 
                self.minutes = 0
    
    def __str__(self): 
        return f"{self.minutes:02}:{self.seconds:02}"

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self): 
        self.seconds += 1
        if self.seconds == 60: 
            self.seconds = 0
            self.minutes += 1 
            if self.minutes == 60: 
                self.minutes = 0
                self.hours += 1
                if self.hours == 24: 
                    self.hours = 0 
    
    def set(self, hours: int, minutes: int): 
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    
    def __str__(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

def main(): 
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)


if __name__ == "__main__": 
    main()  