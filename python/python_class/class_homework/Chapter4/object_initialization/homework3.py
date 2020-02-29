class Student:

    def __init__(self, n = "xxx", s = "男"):
        self.name = n
        self.sex = s

    def show(self):
        print(s.name, s.sex)


s = Student("yyy")
Student.show(s)