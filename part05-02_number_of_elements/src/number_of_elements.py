# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    counter = 0

    for row in my_matrix: 
        for i in range(len(row)): 
            if row[i] == element: 
                counter += 1 
            else:
                continue
    
    return counter

if __name__ == "__main__": 
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
