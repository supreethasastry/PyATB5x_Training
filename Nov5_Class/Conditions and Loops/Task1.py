#/Triangle classifier
#/Program to find maximum of 3 nos
a=int(input("Enter first side:\n"))
b=int(input("Enter second side:\n"))
c=int(input("Enter third side:\n"))
if a==b and a==c:
    print("Equilateral")
elif a==b and a!=c:
    print("Isosceles")
elif b==c and b!=a:
    print("Isosceles")
elif c==a and c!=b:
    print("Isosceles")
elif a<=0 or b<=0 or c<=0:
     print("Invalid values")
else:
    print("Scalene")