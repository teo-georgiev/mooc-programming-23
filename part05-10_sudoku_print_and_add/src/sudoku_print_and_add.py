# Write your solution here

# COMMUNITY SOLUTION

# def print_sudoku(sudoku: list): 
#     for row in range(0, len(sudoku)): 
#         for j in range(0, len(sudoku[row])):
#             if sudoku[row][j] == 0:
#                 sudoku[row][j] = "_"
    
#         for column in range(0, len(sudoku[row]), 3): 
#             box = (sudoku[row][column: column + 3])
#             if column == 3 or column == 6 or column == 9:
#                 print(end = " ")
#             print(" ".join(map(str, box)), end = " ")
        
#         if row == 2 or row == 5: 
#             print()
#         print()

# def add_number(sudoku: list, row_no: int, column_no: int, number: int): 
#     sudoku[row_no][column_no] = number

# MODEL SOLUTION

# def print_sudoku(sudoku: list): 
#     r = 0
#     for row in sudoku: 
#         s = 0
#         for character in row: 
#             s += 1
#             if character == 0: 
#                 character = "_"
#             m = f"{character} "
#             if s % 3 == 0 and s < 8: 
#                 m += " "
#             print(m, end = "")

#         print()
#         r += 1 
#         if r % 3 == 0 and r < 8: 
#             print()


def print_sudoku(sudoku: list): 
    r = 0 
    for row in sudoku: 
        s = 0
        for item in row: 
            s += 1 
            if item == 0: 
                item = "_"
            m = f"{item} "
            if s % 3 == 0 and s < 8: 
                m += " "
            print(m, end = "")
        
        print ()
        r += 1 
        if r % 3 == 0 and r < 8: 
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int): 
    sudoku[row_no][column_no] = number 

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)

    print()
    print("Three numbers added:")
    print_sudoku(sudoku)