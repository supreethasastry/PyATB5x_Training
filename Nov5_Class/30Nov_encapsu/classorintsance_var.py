class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name


bob = Person("bob")
marry = Person("marry")

print(bob.name)
print(marry.name)

print("Who is walking", bob.walk())
print("Who is walking", marry.walk())