# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str): 
    if  x > 2 or x < 0 or y > 2 or y < 0: 
        return False
    
    if game_board[y][x] == "X" or game_board[y][x] == "O":
        return False
    else: 
        game_board[y][x] = piece
        return True

if __name__ == "__main__": 
    game_board = [
        ["", "", ""], 
        ["", "", ""], 
        ["", "", ""]
    ]

    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)