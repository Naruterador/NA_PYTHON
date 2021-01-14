#coding=utf-8

'''
使用未绑定方法调用被重写的方法

1.如果在子类中调用重写之后的方法，Python总是会执行子类重写的方法，不会执行父类中被重写的方法。如果需要在子类中调用父类中被重写的实例方法，那该怎么办呢？
2.由于python类中的方法本质上相当与类空间内的函数，所以即使是实例方法，python也允许通过类名调用。
3.通过类名调用实例方法时，PYTHON不会为实例方法的第一个参数self自动绑定参数值，而是需要程序显示绑定第一个参数self。这种机制被称为未绑定方法。
4.通过未绑定方法即可在子类中再次调用父类中被重写的方法。
'''


class BaseClass(object):

    def foo(self):
        print('父类中定义的foo方法')

class SubClass(BaseClass):

    def foo(self):
        print('子类重写父类中的foo方法')

    def bar(self):
        print('执行bar方法')

        #直接执行foo方法，将会调用子类重写之后的foo()方法
        self.foo()


        #使用类名调用实例方法（未绑定方法）调用父类被重写的方法
        #未绑定方法对象，需要传递一个实例
        #未绑定方法调用1
        x = BaseClass()
        BaseClass.foo(x)

        #未绑定方法调用2
        #BaseClass.foo(self)

sc = SubClass()
sc.bar()