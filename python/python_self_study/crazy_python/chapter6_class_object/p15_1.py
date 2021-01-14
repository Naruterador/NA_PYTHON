#coding=utf-8
'''
Python 实例方法、类方法、静态方法的区别与作用
实例方法

    定义：第一个参数必须是实例对象，该参数名一般约定为“self”，
    通过它来传递实例的属性和方法（也可以传类的属性和方法）；

    调用：只能由实例对象调用。

类方法

    定义：使用装饰器@classmethod。第一个参数必须是当前类对象，
    该参数名一般约定为“cls”，通过它来传递（不能传实例的属性和方法）；

    调用：实例对象和类对象都可以调用。

静态方法

    定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，
    但是方法体中不能使用类或实例的任何属性和方法；

    调用：实例对象和类对象都可以调用。
    实例方法
简而言之，实例方法就是类的实例能够使用的方法。这里不做过多解释。

类方法
使用装饰器@classmethod。

原则上，类方法是将类本身作为对象进行操作的方法。
假设有个方法，且这个方法在逻辑上采用类本身作为对象来调用更合理，那么这个方法就可以定义为类方法。
另外，如果需要继承，也可以定义为类方法。

如下场景：sxds

假设我有一个学生类和一个班级类，想要实现的功能为：
    执行班级人数增加的操作、获得班级的总人数；
    学生类继承自班级类，每实例化一个学生，班级人数都能增加；
    最后，我想定义一些学生，获得班级中的总人数。

思考：这个问题用类方法做比较合适，为什么？因为我实例化的是学生，
但是如果我从学生这一个实例中获得班级总人数，在逻辑上显然是不合理的。
同时，如果想要获得班级总人数，如果生成一个班级的实例也是没有必要的。
'''

class ClassTest(object):
    __num = 0

    @classmethod
    def addNum(cls):
        cls.__num += 1

    @classmethod
    def getNum(cls):
        return cls.__num

    # 这里我用到魔术方法__new__，主要是为了在创建实例的时候调用累加方法。
    def __new__(cls):
        ClassTest.addNum()  
        return super().__new__(cls)

    '''
    def __new__(self):
        ClassTest.addNum()
        return super(ClassTest,self).__new__(self)
    '''


class Student(ClassTest):
    pass

a = Student()
b = Student()
print(ClassTest.getNum())
