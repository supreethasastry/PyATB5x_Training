class student:
    sname=None
    sage=None
    gender=None
    def name(self, sname):
        print("Name:\n", sname)

    def age(self,sage):
        print("Age:\n", sage)

obj=student()
obj.sname="Soundarya"
obj.name(obj.sname)