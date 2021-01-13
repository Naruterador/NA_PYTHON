#coding=utf-8
'''
静态方法
使用装饰器@staticmethod。

静态方法是类中的函数，不需要实例。静态方法主要是用来存放逻辑性的代码，
逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作。可以理解为，
静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护。

譬如，我想定义一个关于时间操作的类，其中有一个获取当前时间的函数。
'''


import time

class TimeTest(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())


#print(TimeTest.showTime())
t = TimeTest(2, 10, 10)
nowTime = t.showTime()
print(nowTime)


'''
如上，使用了静态方法（函数），然而方法体中并没使用（也不能使用）类或实例的属性（或方法）。
若要获得当前时间的字符串时，并不一定需要实例化对象，此时对于静态方法而言，所在类更像是一种名称空间。
'''