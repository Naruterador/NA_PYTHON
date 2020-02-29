
'''
这个项目是通过面向对象的方法设计学生类Student，包含一个学生姓名(Name)、性别(Sex)、年龄(Age)，然后设计学生记录管理类StudentList来管理一组学生记录。

程序运行后显示">"的提示符号
在">"后面可以输入show、insert、update、delete等命令实现记录的显示、插入、修改、删除等功能
执行一个命令后继续显示">"提示符号
如果输入exit就退出系统
输入的命令不正确时会提示正确的输入命令

>show
No               Name             Gender   Age
>insert
No=1
Name=AA
Gender=男
Age=23
增加成功
>show
No               Name             Gender   Age
1                AA               男        23
>update
No=1
Name=BB
Gender=女
Age=21
修改成功
>show
No               Name             Gender   Age
1                BB               女        21
> 
'''


class Student:
    def __init__(self, No, Name, Gender, Age):
        self.No = No
        self.Name = Name
        self.Gender = Gender
        self.Age = Age

    def show(self):
        print("%-16s %-16s %-8s %-4d" %
              (self.No, self.Name, self.Gender, self.Age))


class StudentList:
    def __init__(self):
        self.students = []

    def show(self):
        print("%-16s %-16s %-8s %-4s" % ("No", "Name", "Gender", "Age"))
        for s in self.students:
            s.show()

    def __insert(self, s):
        i = 0
        while (i < len(self.students) and s.No > self.students[i].No):
            i = i + 1
        if (i < len(self.students) and s.No == self.students[i].No):
            print(s.No+" 已经存在")
            return 
        self.students.insert(i, s)
        print("增加成功")
        return 

    def __update(self, s):
        flag = False
        for i in range(len(self.students)):
            if (s.No == self.students[i].No):
                self.students[i].Name = s.Name
                self.students[i].Gender = s.Gender
                self.students[i].Age = s.Age
                print("修改成功")
                flag = True
                break
        if(not flag):
            print("没有这个学生")
        return flag

    def __delete(self, No):
        flag = False
        for i in range(len(self.students)):
            if (self.students[i].No == No):
                del self.students[i]
                print("删除成功")
                flag = True
                break
        if (not flag):
            print("没有这个学生")
        return flag

    def delete(self):
        No = input("No=")
        if(No != ""):
            self.__delete(No)

    def insert(self):
        No = input("No=")
        Name = input("Name=")
        while True:
            Gender = input("Gender=")
            if(Gender == "男" or Gender == "女"):
                break
            else:
                print("Gender is not valid")
        Age = input("Age=")
        if(Age == ""):
            Age = 0
        else:
            Age = int(Age)
        if No != "" and Name != "":
            self.__insert(Student(No, Name, Gender, Age))
        else:
            print("学号、姓名不能为空")

    def update(self):
        No = input("No=")
        Name = input("Name=")
        while True:
            Gender = input("Gender=")
            if(Gender == "男" or Gender == "女"):
                break
            else:
                print("Gender is not valid")
        Age = input("Age=")
        if(Age == ""):
            Age = 0
        else:
            Age = int(Age)
        if No != "" and Name != "":
            self.__update(Student(No, Name, Gender, Age))
        else:
            print("学号、姓名不能为空")

    def process(self):
        while True:
            s = input(">")
            if (s == "show"):
                self.show()
            elif (s == "insert"):
                self.insert()
            elif (s == "update"):
                self.update()
            elif (s == "delete"):
                self.delete()
            elif (s == "exit"):
                break
            else:
                print("show:   show students")
                print("insert: insert a new student")
                print("update: insert a new student")
                print("delete: delete a student")
                print("exit:   exit")


st = StudentList()
st.process()
