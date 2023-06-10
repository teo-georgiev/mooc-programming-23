# Write your solution here

# SEARCH BY NAME
def search_by_name(filename: str, word: str): 
    recipesAll = {}
    foodRecipe = []
    
    with open(filename) as recipesText: 
        for line in recipesText: 
            line = line.replace("\n", "")
            if line == "" :
                recipesAll[foodRecipe[0]] = foodRecipe[1:]
                foodRecipe = []
            else: 
                foodRecipe.append(line)
        recipesAll[foodRecipe[0]] = foodRecipe[1:]

    foundRecipes = []
    for key in recipesAll: 
        word = word.lower()
        keyCheck = key.lower()
        if word in keyCheck: 
            foundRecipes.append(key)
    
    return foundRecipes

# SEARCH BY TIME
def search_by_time(filename: str, prep_time: int):
    recipesAll = {}
    foodRecipe = []
    
    with open(filename) as recipesText: 
        for line in recipesText: 
            line = line.replace("\n", "")
            if line == "" :
                recipesAll[foodRecipe[0]] = foodRecipe[1]
                foodRecipe = []
            else: 
                foodRecipe.append(line)
        recipesAll[foodRecipe[0]] = foodRecipe[1]
    
    prepTimeRes = []
    for key, value in recipesAll.items(): 
        if prep_time >= int(value): 
            x = f"{key}, preparation time {value} min"
            prepTimeRes.append(x)
    
    return prepTimeRes    

# SEARCH BY INGREDIENT
def search_by_ingredient(filename: str, ingredient: str):
    recipesAll = {}
    foodRecipe = []
    
    with open(filename) as recipesText: 
        for line in recipesText: 
            line = line.replace("\n", "")
            if line == "" :
                recipesAll[foodRecipe[0]] = foodRecipe[1:]
                foodRecipe = []
            else: 
                foodRecipe.append(line)
        recipesAll[foodRecipe[0]] = foodRecipe[1:]

    ingredientList = []
    for key, value in recipesAll.items(): 
        ingredient = ingredient.lower()
        if ingredient in value: 
            x = f"{key}, preparation time {value[0]} min"
            ingredientList.append(x)
    
    return ingredientList

# BODY 
if __name__ == "__main__": 
    print(10 * "-")
    print("SEARCH BY NAME")
    foundRecipes = search_by_name("recipes1.txt", "cake")
    for recipe in foundRecipes:
        print(recipe)

    print(10 * "-")
    print("SEARCH BY TIME")
    foundRecipes = search_by_time("recipes1.txt", 20)
    for recipe in foundRecipes:
        print(recipe)

    print(10 * "-")
    print("SEARCH BY INGREDIENT")
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)


