# Write your solution here
def transpose(matrix: list): 
    
    # MODEL SOLUTION
    # n = len(matrix)
    # for i in range(n):
    #     for j in range(i, n): 
    #         temp = matrix[i][j]
    #         matrix[i][j] = matrix[j][i]
    #         matrix[j][i] = temp

    print("---")
    print("ORIGINAL")
    for row01 in matrix: 
        print(row01)

    print("---")
    print("TRANSPOSED")
    holder = []
    for row in range(len(matrix)): 
        holder.append(matrix[row][:])

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] = matrix[c][r]
        
    
    for r in range(len(holder)):
        for c in range(len(holder[r])):
            if holder[r][c] == matrix[c][r]: 
                continue
            else:
                matrix[c][r] = holder[r][c]
        print(matrix[r][:])
        

if __name__ == "__main__": 
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transpose(matrix)