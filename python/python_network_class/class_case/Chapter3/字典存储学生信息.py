'''
1、案例描述
使用列表与字典存储学生信息，方便查找，学生信息包括的姓名、性别、年龄。
 

2、案例分析
一个学生的信息是字典对象，例如：
{"Name":"张三","Gender":"男","Age":20}
设计一个列表st=[]，它存储多个学生，每个列表元素是一个学生字典对象，例如：
st=[{"Name":"张三","Gender":"男","Age":20},{"Name":"张四","Gender":"女","Age":20}]
'''

st = []
def getStudents():
    global st
    st = []
    st.append({"Name":"张三","Gender":"男","Age":20})
    st.append({"Name": "李四", "Gender": "女", "Age": 21})
    st.append({"Name": "王五", "Gender": "男", "Age": 22})

def seekStudent(Name):
    for s in st:
        if s["Name"] == Name:
            print(s["Name"], s["Gender"], s["Age"])
            return
    print("没有姓名是",Name,"的学生")


getStudents()
seekStudent("张三")
seekStudent("张四")

