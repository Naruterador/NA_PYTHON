'''
1、案例描述
编写个人信息类并建立对象访问属性。
 
2、案例分析
个人信息类Person定义如下：
class Person:
    name="XXX"
    gender="X"
    age=0
其中name,gender,age都是类属性，类属性一般使用类名称Person访问。
'''


class Person:
    name = "XXX"
    gender = "X"
    age = 0



p = Person()
print(p.name, p.gender, p.age)
print(Person.name, Person.gender, Person.age)

print("*************************************")

p.name = "A"
p.gender = "Male"
p.age = 20
Person.name = "B"
Person.gender = "Female"
Person.age = 21
print(p.name, p.gender, p.age)
print(Person.name, Person.gender, Person.age)
