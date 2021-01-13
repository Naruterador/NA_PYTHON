'''
【案例】从文件读出学生信息
1、案例描述
读出前一节中保存在students.txt中的全部学生记录。

2、案例分析
读出students.txt文件学生信息的关键代码如下：
f = open("student.txt", "rt")
while True:
    name = f.readline().strip("\n")
    if name == "":
        break
    gender = f.readline().strip("\n")
    age = float(f.readline().strip("\n"))
每次读取一行后使用strip("\n")
函数把这一行的
"\n"
去掉，因为readline()
函数读出的行是包含
"\n"
的。
'''

class Student:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def show(self):
        print(self.name, self.gender, self.age)


students = []

try:
    f = open("student.txt", "rt")
    while True:
        name = f.readline().strip("\n")
        if name == "":
            break
        gender = f.readline().strip("\n")
        age = float(f.readline().strip("\n"))
        students.append(Student(name, gender, age))
    f.close()

    for s in students:
        s.show()
        
except Exception as err:
    print(err)

