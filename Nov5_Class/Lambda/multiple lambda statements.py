#/Write a program to find even or odd number using lambda
n=int(input("Enter a number:\n"))

result= lambda num : "Even" if num%2==0 else "Odd" #/Using ternary operator
print(result(n))