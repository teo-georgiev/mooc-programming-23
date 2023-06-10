# Write your solution here
while True: 
    print("1 - Add word, 2 - Search, 3 - Quit")
    while True: 
        userFunc = int(input("Function: "))
        if userFunc == 1 or userFunc == 2 or userFunc == 3: 
            break 

    if userFunc == 1: 
        wordFin = input("The word in Finnish: ")
        wordEng = input("The word in English: ")

        # Check if already existing 
        with open("dictionary.txt", "r+") as newFile:
            check = True 

            for entry in newFile: 
                entry = entry.replace("\n", "")
                words = entry.split(";")

                if wordFin == words[0] or wordEng == words[1]:
                    print("Dictionary entry added")
                    check = False 
                    break

            if check: 
                newFile.write(f"{wordFin};{wordEng}\n")
                print("Dictionary entry added")  
            
    elif userFunc == 2: 
        with open("dictionary.txt") as newFile:
            searchTerm = input("Search term: ")
            for entry in newFile: 
                entry = entry.replace("\n", "")
                words = entry.split(";")

                if searchTerm in words[0] or searchTerm in words[1]: 
                    print(f"{words[0]} - {words[1]}")
    elif userFunc == 3: 
        print("Bye!")
        break

                
                