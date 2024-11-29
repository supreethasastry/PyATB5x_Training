class student:
    def __init__(self):
        self.name=input("ENter your name: ")
        self.age=input("ENter your age: ")
        self.gender=input("ENter your gender: ")
        self.qualification=input("ENter your qualification: ")

    def studentinfo(self):
        print("Student name: ", self.name,'|' ,"Student age: ",'|',self.age, "Student gender: ", self.gender,'|', "Student qualification: ", self.qualification)

s=student()
s.studentinfo()