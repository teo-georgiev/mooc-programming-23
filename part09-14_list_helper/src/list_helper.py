# WRITE YOUR SOLUTION HERE:

# MODEL SOLUTION
class ListHelper: 
    @classmethod 
    def greatest_frequency(cls, my_list: list):
        # If there is no items at all, then there is no frequency
        if not my_list: 
            return None
        
        max_frequency = 0
        max_item = None 
        for item in my_list: 
            frequency = my_list.count(item)
            if not max_item or frequency > max_frequency: 
                max_frequency = frequency
                max_item = item

        return max_item
    
    @classmethod
    def doubles(cls, my_list: list): 
        counts = {}
        for item in my_list: 
            counts[item] = my_list.count(item)

        doubles = 0 
        for value in counts.values():
            if value > 1: 
                doubles += 1 

        return doubles

# MY SOLUTION 
# class ListHelper: 

#     @classmethod
#     def greatest_frequency(cls, my_list: list):
#         frequency_number = 0
#         most_common_item = 0
#         frequency_items = {}

#         for item in my_list: 
#             if item not in frequency_items: 
#                 frequency_items[item] = 1
#             elif item in frequency_items: 
#                 frequency_items[item] += 1
         
#         for key, value in frequency_items.items():
#             if value > frequency_number: 
#                 most_common_item = key
#                 frequency_number = value
#             else: continue
        
#         return most_common_item

#     @classmethod
#     def doubles(cls, my_list: list): 
#         frequency_number = 0
#         frequency_items = {}
#         doubles_counter = 0

#         for item in my_list: 
#             if item not in frequency_items: 
#                 frequency_items[item] = 1
#             elif item in frequency_items: 
#                 frequency_items[item] += 1
        
#         for ket, value in frequency_items.items():
#             if value >= 2: 
#                 doubles_counter += 1 
#             else: continue
        
#         return doubles_counter

def main(): 
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

if __name__ == "__main__": 
    main()
    
