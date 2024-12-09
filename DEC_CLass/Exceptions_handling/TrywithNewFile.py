import os

file_name = "suppie.txt"
content = "This is a Suppie's File, healer, Psychic, Successful Tarot Card Reader"

with open(file_name, "w") as file:
    file.write(content)

with open(file_name, "r") as file:
    content2 = file.read()
    print(content2)

# os.chdir("Desktop")