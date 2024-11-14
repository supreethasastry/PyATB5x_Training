#/Write program that calculates and displays grade for given numerical score
s=int(input("Enter your score:"))
if s>=90 and s<=100:
    print("Grade is A")
elif s>=80 and s<=89:
    print("Grade is B")
elif s>=70 and s<=79:
    print("Grade is C")
elif s>=60 and s<=69:
    print("Grade is D")
elif s<=0 or s>100:
    print("Invalid score")
else:
    print("Grade is F")

