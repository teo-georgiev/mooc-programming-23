# Write your solution here
def who_won(gameBoard: list): 
    counter1 = 0
    counter2 = 0

    for row in gameBoard: 
        for cell in row: 
            if cell == 1: 
                counter1 += 1
            elif cell == 2: 
                counter2 += 1
            else: 
                continue
    
    if counter1 > counter2: 
        return 1
    elif counter1 < counter2: 
        return 2
    elif counter1 == counter2: 
        return 0;

if __name__ == "__main__": 
    game_board = [[1,0,1,2,0],[1,0,1,1,2],[1,2,1,1,0],[1,0,2,1,0],[1,0,2,2,0]]
    print(who_won(game_board))

