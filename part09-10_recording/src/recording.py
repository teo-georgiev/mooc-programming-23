# WRITE YOUR SOLUTION HERE:
class Recording: 
    def __init__(self, length: int) -> None:
        if length < 0:
            raise ValueError()
        self.__length = length
    
    @property
    def length(self): 
        return self.__length
    
    @length.setter
    def length(self, new_length: int): 
        if new_length < 0:
            raise ValueError()
        self.__length = new_length

if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
