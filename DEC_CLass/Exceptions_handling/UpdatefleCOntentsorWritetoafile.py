with open("SS.txt",'a') as file:
    file.write("hello")

with open("SS.txt","r") as file:
    contents=file.read()
    print(contents)