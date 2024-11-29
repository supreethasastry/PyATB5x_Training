class PyATB:
    name = None
    age = None
    gender = None
    qualification = None
    courses_opted = None

    def __init__(self, name, age, gender, qualification, courses_opted):

        self.name = name
        self.age = age
        self.gender = gender
        self.qualification = qualification
        self.courses_opted = courses_opted

    def print_studentinfo(self):
        print("Student name: ", self.name)
        print("Student age: ", self.age)
        print("Student gender: ", self.gender)
        print("Student qualification: ", self.qualification)
        print("Student courses opted: ", self.courses_opted)

    def sleep(self):
        print("Which Student-> " + self.name)

    def talk(self):
        pass


s1 = PyATB("Supreetha", 31, "Female", "B.E", "Python- Selenium")
s2 = PyATB("Shreshta", 25, "Female", "Mtech", "JAVA- Selenium")
s3 = PyATB("Satish", 35, "Male", "B.E", "Agile Testing")
print("Student1 details")
s1.print_studentinfo()
print("Student2 details")
s2.print_studentinfo()
print("Student3 details")
s3.print_studentinfo()
