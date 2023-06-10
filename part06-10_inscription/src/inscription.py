# Write your solution here
name = input("Whom should I sign this to: ")
fileName = input("Where shall I save it: ")

with open(fileName, "w") as newFile: 
    newFile.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")