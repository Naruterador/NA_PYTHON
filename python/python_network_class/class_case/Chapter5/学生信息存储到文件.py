
'''
1、案例描述
输入若干个学生的姓名Name、性别Gender、年龄Age，把它存储到文件students.txt中，每个数据项占一行。

2、案例分析
如果fobj是文件对象，那么学生的姓名Name、性别Gender、年龄Age存储语句如下：
fobj.write(Name + "\n")
fobj.write(Gender + "\n")
fobj.write(str(Age) + "\n")
或者：
fobj.write(Name + "\n" + Gender + "\n" + str(Age) + "\n")
即输出Name、Gender、Age后都换行。
'''


def getStudent(i):
    print("输入第", i, "个学生信息")
    try:
        Name = input("姓名:")
        if Name.strip() == "":
            raise Exception("无效的姓名")
        Gender = input("性别:")
        if Gender != "男" and Gender != "女":
            raise Exception("无效的性别")
        Age = input("年龄:")
        Age = float(Age)
        if Age < 18 or Age > 30:
            raise Exception("无效的年龄")
        s = {}
        s["Name"] = Name
        s["Gender"] = Gender
        s["Age"] = Age
        return s
    except Exception as err:
        print(err)
        return None


i = 1
try:
    fobj = open("students.txt", "wt")
    while True:
        s = getStudent(i)
        if s:
            fobj.write(s["Name"] + "\n" + s["Gender"] +
                       "\n" + str(s["Age"]) + "\n")
            i = i + 1
        s = input("继续输入吗(Y/N)")
        if s != "Y" and s != "y":
            break
    fobj.close()
except Exception as err:
    print(err)
