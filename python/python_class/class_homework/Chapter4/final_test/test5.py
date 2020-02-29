class Person:
    def __init__(self, n = "xxx"):
        self.name = n


class Student(Person):
    def __init__(self, n = "aaa", s = "male"):
        Person.__init__(self)
        self.sex = s

    def show(self):
        print(self.name, self.sex)


s = Student("yyy", "female")
s.show()
