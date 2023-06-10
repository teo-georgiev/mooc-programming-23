# Write your solution here
while True: 
    editorInput = input("Editor: ")
    editorInput = editorInput.lower()

    if editorInput == "visual studio code": 
        print("an excellent choice!")
        break
    elif editorInput == "word":
        print("awful")
        continue
    else: 
        print("not good")
        continue