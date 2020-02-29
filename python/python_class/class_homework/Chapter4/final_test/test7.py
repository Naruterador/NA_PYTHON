class Student:

    def __init__(self, n = "xxx"):
        self.name = n

    @classmethod
    def show(cls):
        s = cls()
        print(s.name)


s = Student("yyy")
Student.show(s)
