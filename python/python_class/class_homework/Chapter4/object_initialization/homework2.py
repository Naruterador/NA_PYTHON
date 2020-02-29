class Student:

    def __init__(self, n = "xxx"):
        self.name = n

    def show(self):
        print(self.name)


s = Student("yyy")
s.show()
