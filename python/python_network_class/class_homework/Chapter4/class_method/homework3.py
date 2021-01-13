class Student:
    name = "xxx"

    @staticmethod
    def show():
        name = "yyy"   #因为重新定义了name
        print(name, Student.name)

    @classmethod
    def display(cls):
        cls.show()


s = Student()
s.display()
