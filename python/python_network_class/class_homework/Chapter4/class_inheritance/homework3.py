class Student:
    name = "xxx"
    age = 20


s = Student()
s.name = "yyy"
s.age = 30
print(s.name, s.age, Student.name, Student.age)


