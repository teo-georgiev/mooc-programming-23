# Write your solution here:

# MODEL SOLUTION
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

# MY SOLUTION 
# class Stopwatch:
#     def __init__(self):
#         self.seconds = 0
#         self.minutes = 0
#         self.counter = 0
    
#     def __str__(self) -> str:
#         return f"{self.minutes:02d}:{self.seconds:02d}"
    
#     def tick(self): 
#         if self.seconds == 59: 
#             self.minutes += 1
#             self.seconds = 0
#         elif self.seconds < 59: 
#             self.seconds += 1
        
#         if self.seconds == 60 or self.minutes == 60: 
#             self.minutes = 0
#             self.seconds = 0

def main(): 
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()

if __name__ == "__main__": 
    main()