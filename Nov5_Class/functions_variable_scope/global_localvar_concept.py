globalvar=10

def demo():
    localvar=20
    print(localvar)
    print(globalvar)
#//  print(localvar)- local var cannot be accessed outside the func

demo()


#/local var have more preference when compared to global var