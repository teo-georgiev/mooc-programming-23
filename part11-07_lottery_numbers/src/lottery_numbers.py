# WRITE YOUR SOLUTION HERE:
class LotteryNumbers: 
    def __init__(self, week_num: int, numbers: list):
        self.__week_num = week_num
        self.__numbers = numbers
        self.__counter = 0

    def number_of_hits(self, numbers: list):
        return sum([self.__counter + 1 for num in numbers if num in self.__numbers])

    def hits_in_place(self, numbers: list):
        return [num if num in self.__numbers else -1 for num in numbers]
        # return [numbers[i] if numbers[i] == self.__numbers[i] else -1 for i in range(0, len(numbers), 1)]

def main():
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))


if __name__ == "__main__":
    main()