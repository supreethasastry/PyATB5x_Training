a=10

def display():
    b=20
    print(b)
    a=25 #/global var value is overridden by local value
    print(a)

display()