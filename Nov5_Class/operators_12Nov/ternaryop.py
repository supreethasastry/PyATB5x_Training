#/if-else statement
"""if(x>y):
    print("x is greater")
else:
    print("y is greater")"""
#/Program: if age >=18 - allowed to vote
age=int(input("Enter your age:"))
if(age>=18):
    print("Your are eligible for voting")
else:
    print("Not allowed for voting")

print("Your are eligible for voting"if age>=18 else"Not allowed for voting") #/ternary operator not preferred
#/2nd way, print("Your are eligible for voting"if int(input("Enter your age:"))>=18 else"Not allowed for voting") #/ternary operator
