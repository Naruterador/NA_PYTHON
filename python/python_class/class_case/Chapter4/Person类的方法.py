'''
1、案例描述
编写个人信息类的实例方法、类方法、静态方法。
 
2、案例分析
个人信息类Person定义实例方法、静态方法、类方法，然后程序分析它们的调用。
'''


class Person:
    name = "XXX"
    gender = "X"
    age = 0

    def instanceShow(self):
        print(self.name, self.gender, self.age)

    @classmethod
    def classShow(cls):
        print(cls.name, cls.gender, cls.age)

    @staticmethod
    def staticShow():
        print(Person.name, Person.gender, Person.age)


p = Person()
p.instanceShow()
Person.classShow()
Person.staticShow()
