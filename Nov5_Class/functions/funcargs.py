def print_mul_args(*args):
    #args->list
    for i in args:
        print(i)

print_mul_args() #/nothing gets printed
print_mul_args("Sup")
print_mul_args("Sup",111,"Shreshtu")
print_mul_args("Sup",111,True,"Shreshtu")
