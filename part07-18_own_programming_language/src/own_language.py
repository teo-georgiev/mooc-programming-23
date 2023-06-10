# Write your solution here
import csv
from string import ascii_uppercase

# # MODEL SOLUTIONS
# def value(x, data): 
#     characters = ascii_uppercase
#     if x in characters: 
#         return data[characters.index(x)]
#     else: 
#         return int(x)

# def condition(a, condition, b): 
#     if condition == "==":
#         return a == b
#     if condition == "!=": 
#         return a != b
#     if condition == "<": 
#         return a < b
#     if condition == "<=": 
#         return a <= b
#     if condition == ">":
#         return a > b
#     if condition == ">=": 
#         return a >= b

# def run(program): 
#     length = len(program)
#     row = 0
#     characters = ascii_uppercase
#     data = [0]*26
#     result = []
    
#     while True: 
#         if row == length: 
#             break
#         parts = program[row].split(" ")
#         if parts[0] == "PRINT":
#             result.append(value(parts[1]), data)
#         if parts[0] == "MOV": 
#             data[characters.index(parts[1])] = value(parts[2], data)
#         if parts[0] == "ADD": 
#             data[characters.index(parts[1])] += value(parts[2], data)
#         if parts[0] == "SUB": 
#             data[characters.index(parts[1])] -= value(parts[2], data)
#         if parts[0] == "MUL": 
#             data[characters.index(parts[1])] *= value(parts[2], data)
#         if parts[0] == "JUMP": 
#             row = program.index(parts[1] + ":")
#             continue
#         if parts[0] == "IF":
#             if condition(value(parts[1], data), parts[2], value(parts[3], data)): 
#                 row = program.index(parts[5] + ":")
#                 continue
#         if parts[0] == "END": 
#             break
#         row += 1 
#     return result

def add(x: int, y: int):
    x += y
    return x

def sub(x: int, y: int): 
    x -= y
    return x

def mul(x: int, y: int): 
    x *= y
    return x

def run(program: list):
    # Checking the type of value that 
    # Y has for the arithmetic functions
    def check(y): 
        if y in vars:
            y = vars[y]
        else: 
            y = int(y)
        return y
    
    # JUMPING TO A LOCATION
    def jumpLocation(loc: str): 
        loc = f"{loc}:"
        if loc in program: 
            i = program.index(loc)
        return i

    vars = {}
    result = [] 
    i = 0
    if vars == {}:
        variables = ascii_uppercase
        for letter in variables: 
            vars[letter] = 0

    
    while i < len(program): 
        parts = program[i].split(" ")
        instruction = parts[0].upper()

        # PRINT
        if instruction == "PRINT": 
            x = check(parts[1])
            result.append(x)
            i += 1
            continue
        
        # ASSIGN
        elif instruction == "MOV":
            y = check(parts[2])
            vars[parts[1]] = y
            i += 1
            continue
        # ADD
        elif instruction == "ADD": 
            x = vars[parts[1]]
            y = check(parts[2])
            vars[parts[1]] = add(x, y)
            i += 1
            continue

        # SUBSTRACT
        elif instruction == "SUB": 
            x = vars[parts[1]]
            y = check(parts[2])
            vars[parts[1]] = sub(x, y)
            i += 1
            continue

        # MULTIPLY
        elif instruction == "MUL": 
            x = vars[parts[1]]
            y = check(parts[2])
            vars[parts[1]] = mul(x, y)
            i += 1
            continue

        # JUMP
        elif instruction == "JUMP":  
            loc = f"{parts[1]}:"
            if loc in program: 
                i = program.index(loc)
            continue

        # COMPARE
        elif instruction == "IF": 
            x = vars[parts[1]]
            y = check(parts[3])

            condition = parts[2]
            if condition == "==" and x == y:
                i = jumpLocation(parts[5])
            elif condition == "<=" and x <= y:
                i = jumpLocation(parts[5])
            elif condition == "<" and x < y:
                i = jumpLocation(parts[5])
            elif condition == ">=" and x >= y:
                i = jumpLocation(parts[5])
            elif condition == ">" and x > y:
                i = jumpLocation(parts[5])
            elif condition == "!=" and x != y:
                i = jumpLocation(parts[5])
            else: 
                i += 1
                continue

        elif ":" in parts[0] and i != len(program) - 1: 
            i += 1
            continue

        # EXIT       
        elif instruction == "END": 
            break
        
    return result
                
if __name__ == "__main__": 
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)
