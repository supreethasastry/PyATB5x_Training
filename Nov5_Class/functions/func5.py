#with no return type but default argument
def greeting(name="Suppie"): #positional arguments
    print("Hi,", name)
    print("Hi,", name.upper())

greeting()
greeting("Shreshta")

#in case of default parameter- when calling the function if no parameter is used, default value is considered,
#but when the function is called with argument, the default value is overridden with passed argument