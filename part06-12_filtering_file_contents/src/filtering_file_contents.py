# Write your solution here
def filter_solutions(): 

# MODEL SOLUTION 

    # with open("solutions.csv") as source, open("correct.csv", "w") as correctFile, open("incorrect.csv", "w") as incorrectFile: 
    #     for row in source: 
    #         # Split into pieces
    #         pieces = row.split(";")

    #         calculation = pieces[1]
    #         result = pieces[2]

    #         # Addition or substraction
    #         if "+" in calculation: 
    #             operands = calculation.split("+")
    #             # correct is True or False based on whether the calculation was correct or not
    #             correct = int(operands[0]) + int(operands[1]) == int(result)
    #         else: 
    #             operands = calculation.split("-")
    #             # correct is True or False based on whether the calculation was correct or not
    #             correct = int(operands[0]) - int(operands[1]) == int(result)

    #         # Write to file 
    #         if correct: 
    #             correctFile.write(row)
    #         else: 
    #             incorrectFile.write(row)

    # MY SOLUTION

    open("incorrect.csv", "w").close()
    open("correct.csv", "w").close()

    with open("solutions.csv") as newFile: 
        for line in newFile: 
            entry = line.split(";")

            if "-" in entry[1]: 
                nums = entry[1].split("-")
                num1 = int(nums[0])
                num2 = int(nums[1])
                if num1 - num2 != int(entry[2]): 
                    with open("incorrect.csv", "a") as incorrectFile: 
                        incorrectFile.write(f"{line}\n")
                else: 
                    with open("correct.csv", "a") as correctFile: 
                        correctFile.write(f"{line}\n")

            elif "+" in entry[1]: 
                nums = entry[1].split("+")
                num1 = int(nums[0])
                num2 = int(nums[1])

                if num1 + num2 != int(entry[2]): 
                    with open("incorrect.csv", "a") as incorrectFile: 
                        incorrectFile.write(f"{line}\n")
                else: 
                    with open("correct.csv", "a") as correctFile: 
                        correctFile.write(f"{line}\n")

if __name__ == "__main__":
    filter_solutions()