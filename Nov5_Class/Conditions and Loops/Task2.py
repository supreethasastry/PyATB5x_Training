#/Program to find out leap year
y=int(input("Enter year:"))
if y<=0:
    print("Invalid value")
elif y%4==0 and y%100!=0 or y%400==0:
    print("Leap year")
else:
    print("Not a leap year")