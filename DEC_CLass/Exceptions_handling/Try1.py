print(" --- Start of the Program")
try:
    a = int(input("Ent the num1")) # ValueError: invalid literal for int() with base 10: 'pramod'
    b = int(input("Ent the num2"))
    c = a / b # ZeroDivisionError: division by zero
    print("Result Div is ", c)
except Exception as e:
    print(e)


print(" --- End of the Program")

# try and Except