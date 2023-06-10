# Write your solution here

def print_sudoku(sudoku: list): 
    r = 0 
    for row in sudoku: 
        s = 0
        for character in row: 
            s += 1
            if character == 0: 
                character = "_"
            m = f"{character} "
            if s % 3 == 0 and s < 8: 
                m += " "
            print(m, end = "")

        print()
        r += 1 
        if r % 3 == 0 and r < 8: 
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int): 
    newSudoku = []
    
    for row in range(len(sudoku)): 
        newSudoku.append(sudoku[row][:])

    newSudoku[row_no][column_no] = number

    return newSudoku

if __name__ == "__main__": 
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 1, 1, 5)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
