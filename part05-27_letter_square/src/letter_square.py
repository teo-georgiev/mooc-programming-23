# # Write your solution here

# MODEL SOLUTION 

# n = int(input("Layers: "))

# alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# left = ""       # section, that goes downwards
# right = ""      # section, that goes upwards
# k = n - 1       # the location of next character in alphabets
# m = 2 * n - 1   # the number of characters in between

# while k >= 1: 
#     left = left + alphabets[k]
#     right = alphabets[k] + right
#     m -= 2
#     print(left + alphabets[k] * m + right)
#     k -= 1

# while k <= n-1: 
#     print(left + alphabets[k] * m + right)
#     left = left[:-1]
#     right = right[1:]
#     m += 2
#     k += 1


# MY SOLUTION

alphabet = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", 
    "Z"
]

layers = int(input("Layers: "))
width = layers * 2 - 1 
layers -= 1
square = []

for i in range(0, width):
    row = []
    for j in range(0, width): 
        if i == 0 or i == width - 1:
            row.append(alphabet[layers])
        elif i > 0 and i <= layers: 
            if j < i: 
                row.append(alphabet[layers - j])
            elif j == i: 
                for k in range(width - 2 * i):
                    row.append(alphabet[layers - j])
            elif j >= width - i:
                row.append(alphabet[layers - (width-j) + 1])
        else: 
            break

    if i > 0 and i > layers and i < width - 1:
        row = square[width - i - 1]
    
    square.append(row)

for row in square: 
    for col in row: 
        print(col, end="")
    print()
