#coding=utf-8

'''
使用super函数调用父类的构造方法

python子类也会继承得到父类的构造方法，如果子类有多个直接父类，那么排在前面的父类的构造方法会被优先使用。
'''

class Employee(object):
    def __init__(self,salary):
        self.salary = salary
    def work(self):
        print('普通员工正在写代码，工资是: %d' % self.salary)


class Customer(object):
    def __init__(self,favorite,address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print('我是一名顾客，我的爱好是：%s,地址是%s' % (self.favorite,self.address))

class Manager(Employee,Customer):
    pass



m = Manager(25000)
m.work()     #1
#m.info()     #2

'''
在上面的程序中，Manager类将会优先使用Employee类的构造方法(因为在继承时候Employee排在前面)，所以在程序使用Manager(250000)来创建Manager对象时，该构造方法
只会初始化salary实例的变量，因此执行上面程序#1的代码是没有任何问题的。但是当执行到#2时候，就会引发错误。因为继承顺序的关系，程序并没有初始化Customer对象所需要的
两个实例变量(favoirte和address),因此程序引发错误。
'''


