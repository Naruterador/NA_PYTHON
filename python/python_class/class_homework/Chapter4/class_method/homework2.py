class Student:
    name = "xxx"

    @staticmethod
    def show():
        name = "yyy"
        print(name, Student.name)

    @staticmethod
    def display():
        show()


s = Student()
s.display()
