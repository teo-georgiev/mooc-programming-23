# Write your solution here
def find_words(search_term: str): 
    wordsList = []

    with open("words.txt") as wordsFile: 
        for line in wordsFile:
            line = line.replace("\n", "")

            # . CHARACTER
            if "." in search_term and len(line) == len(search_term):
                check = False # Word tracking

                for i in range(0, len(line)): 
                    if line[i] == search_term[i]: 
                        check = True
                    elif search_term[i] == ".": 
                        continue
                    else: 
                        check = False
                        break
                
                if check == True:
                    wordsList.append(line)

            # * CHARACTER 
            if search_term.endswith("*"): 
                search_term2 = search_term[0 : len(search_term) - 1]
                if line.startswith(search_term2): 
                    wordsList.append(line)

            if search_term.startswith("*"): 
                search_term2 = search_term[1 : len(search_term)]
                if line.endswith(search_term2): 
                    wordsList.append(line)

            # EXACT MATCH
            if "." not in search_term and "*" not in search_term:
                if line == search_term: 
                    wordsList.append(line)
    return wordsList
    

if __name__ == "__main__": 
    search_term = input("Search term: ")
    
    print(find_words(search_term))

    