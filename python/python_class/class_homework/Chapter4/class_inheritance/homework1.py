class Student:
    name = "yyy"
    age = 30

    def __init__(self):
        self.name = "xxx"
        self.age = 20


s = Student()
Student.name = "zzz"
print(s.name, s.age, Student.name, Student.age)

