class Student:
    age = 20

    def __init__(self, n = "xxx", s = "男"):
        self.name = n
        self.sex = s

    def show(self):
        print(s.name, s.sex, s.age)


s = Student("yyy")
s.age = 30
s.show()
