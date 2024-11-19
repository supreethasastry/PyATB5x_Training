#/Write a program that gives the sum of three numbers from the user input
#/If user does not enter any number then use default value as 100,200,300

n1=int(input("Enter value for first number:\n"))
n2=int(input("Enter value for second number:\n"))
n3=int(input("Enter value for three number:\n"))

def sum_3num(a=100,b=200,c=300):
    return a+b+c

result1=sum_3num(n1,n2,n3)
print(result1)

result2=sum_3num()
print(result2)
result2=sum_3num(1)
print(result2)
result2=sum_3num(1,2)
print(result2)
result2=sum_3num(1,2,2)
print(result2)
result2=sum_3num(1,1,1,4) #/err
print(result2)