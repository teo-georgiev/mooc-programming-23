# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int): 
    """
    sudokuBlock = []

    for i in range(0, 3, 1):
        list = []
        for j in range(0, 3, 1):
            list.append(sudoku[row_no + i][column_no + j])
        sudokuBlock.append(list)

    print(sudokuBlock)

    i = 0
    numbersRow = []
    numbersCol = []

    for number in sudokuBlock[i]:
        if number > 0 and number in numbersRow: 
            return False
        numbersRow.append(number)
        i += 1
    
    for row in sudokuBlock: 
        j = 0
        for number in row:
            if number > 0 and number in numbersCol: 
                return False
            numbersCol.append(number)
            j += 1 
        
    return True
    """

    numbers = []
    for r in range(row_no, row_no + 3): 
        for s in range(column_no, column_no + 3): 
            number = sudoku[r][s]
            if number > 0 and number in numbers: 
                return False
            numbers.append(number)

    return True

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [2, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))