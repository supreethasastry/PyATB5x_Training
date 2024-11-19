#/Type1
def greeting(name):
    print("Hello ",name)

name=input("Enter your name:\n")
greeting(name)

#/Type 2
def greeting(name):
    print(f"Hello ,{name}")

greeting("Sup")#/name parameter is set to "Sup" here
greeting(123)