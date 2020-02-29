class Person:
    def __init__(self, n = "xxx"):
        self.name = n


class Student(Person):
    def __init__(self,s = "male"):
        self.sex = s

    def show(self):
        print(self.name, self.sex)


s = Student()
s.show()
