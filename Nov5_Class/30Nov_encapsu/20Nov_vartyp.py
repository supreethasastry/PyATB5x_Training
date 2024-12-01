a = 10


class Person:
    b = 11  # Instance - Belong to class

    def print_info(self):
        c = 20  # Local variable
        print(c)
        #/print (self.c) dont ref with self for local variable
        print(self.b)
        global a
        print(a)


object_ref = Person()
object_ref.print_info()