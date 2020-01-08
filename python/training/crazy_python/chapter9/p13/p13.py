#coding = utf - 8 

'''
__str__函数作用:

如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：
不使用 __str__  ，print打印出来是个对象；使用了就把对象变成字符串
__str__和__repr__很类似


'''



class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
'''
现在，在交互式命令行下用 print 试试：
 
>>> p = Person('Bob', 'male')
>>> print p
(Person: Bob, male)
但是，如果直接敲变量 p：
 
>>> p
<main.Person object at 0x10c941890>
似乎__str__() 不会被调用。
 
因为 Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员。
所以在交互式命令中__str__()函数不会运行，交互式命令行中只会出现__repr__()函数显示的内容
'''

class Cat:
    """
    定义了一个Cat类
    """
 
    #初始化对象
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
 
    def __str__(self):
        return "%s的年龄是:%d"%(self.name, self.age)
 
    #方法
    def eat(self):
        print("猫在吃鱼....")
 
    def drink(self):
        print("猫正在喝kele.....")
 
    def introduce(self):
        print("%s的年龄是:%d"%(self.name, self.age))
 
#创建一个对象
tom = Cat("汤姆", 40)
lanmao = Cat("蓝猫", 10)
print(tom)
print(lanmao)