def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper


@decorator1
@decorator2
def say_hello():
    print("Hello!")


say_hello() #/whenever we are using multiple decorators we need to call the func explicitly