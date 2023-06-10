# # MODEL SOLUTION
# def balanced_brackets(mj: str): 
#     # string is empty so it is oka
#     if len(mj) == 0:
#         return True
    
#     # if first character is not any bracket, let's eat it away
#     if not mj[0] in "()[]":
#         return balanced_brackets(mj[1:])
    
#     # if last is not any bracket, let's eat it away
#     if not mj[-1] in "()[]":
#         return balanced_brackets(mj[:-1])
    
#     #now is known that first and last characters are brackets
#     # check if they are a pair
#     if mj[0] == "(" and mj[-1] == ")":
#         return balanced_brackets(mj[1:-1])
#     if mj[0] == "[" and mj[-1] == "]":
#         return balanced_brackets(mj[1:-1])
    
#     # were not, the string is not okay
#     return False

# MY SOLUTION 
def clear_string(my_string: str): 
    brackets = "()[]"
    new_string = ""
    for char in my_string: 
        if char in brackets: 
            new_string += char
        else:
            continue
    my_string = new_string
    return my_string

def balanced_brackets(my_string: str):
    my_string = clear_string(my_string)

    if len(my_string) == 0:
        return True
    
    if not (my_string[0] == '(' and my_string[-1] == ')'): 
        if not (my_string[0] == '[' and my_string[-1] == ']'):
            return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    test = "(python version [3.7]) please use this one!"
    print("TEST", clear_string(test))
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)


