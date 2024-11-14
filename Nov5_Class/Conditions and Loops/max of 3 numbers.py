#/Program to find maximum of 3 nos
a=int(input("Enter first number:\n"))
b=int(input("Enter second number:\n"))
c=int(input("Enter third number:\n"))
if a>=b and a>=c:
    print("Maximum value is:",a)
elif b>=c:
    print("Maximum value is:", b)
else:
    print("Maximum value is:", c)