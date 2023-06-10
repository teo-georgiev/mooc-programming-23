# Write your solution here
# CHECK ROW
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers: 
            return False 
        numbers.append(number)

    return True

# CHECK COLUMN
def column_correct(sudoku: list, column_no: int): 
    numbers = []
    for row in sudoku: 
        number = row[column_no]
        if number > 0 and number in numbers: 
            return False
        numbers.append(number)

    return True    

#CHECK BLOCK
def block_correct(sudoku: list, row_no: int, column_no: int): 
    numbers = []
    for r in range(row_no, row_no + 3): 
        for s in range(column_no, column_no + 3): 
            number = sudoku[r][s]
            if number > 0 and number in numbers: 
                return False
            numbers.append(number)

    return True

#CHECK GRID
def sudoku_grid_correct(sudoku: list): 
    row = True 
    column = True 
    block = True

    for i in range(len(sudoku)):
        row = row_correct(sudoku, i)
        if row == False:
            print("row is false") 
            return False
    
    for i in range(len(sudoku)):
        row = column_correct(sudoku, i)
        if row == False:
            print("col is false")
            return False
    
    for i in range(0, len(sudoku), 3): 
        for j in range(0, len(sudoku), 3): 
            block = block_correct(sudoku, i, j)
            if block == False:
                print("block is false")
                return False
    return True

if __name__ == "__main__": 

    sudoku3 = [
        [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
        [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
        [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
        [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
        [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
        [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
        [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
        [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
        [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

    print(sudoku_grid_correct(sudoku3))