n=int(input("Enter number:\n"))

"""Using normal function
def pow_func(num):
    return num**3

result=pow_func(n)
print(result)"""

#/Using lambda function
result=lambda num: num**2
print(result(n))