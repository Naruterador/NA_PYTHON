#coding=utf-8
'''
在使用property()函数定义属性时，也可以根据需要只传入少量的参数。
'''

class User(object):
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def getfullname(self):
        return self.first + ',' + self.last

    def setfullname(self,fullname):
        first_last = fullname.rsplit(',')
        self.first = first_last[0]
        self.last = first_last[1]

    fullname = property(getfullname,setfullname)


u = User('悟空','孙')

print(u.fullname)

u.fullname = '吃碰,黄'    #使用property函数为成员赋值

print(u.getfullname())


'''
在某些编程语言中，类似于这种property合成的属性被称为计算属性。
这种属性并不真正存储任何状态，它的值其实是通过某种算法计算得到的。
当程序属性赋值时，被赋的值也会被存储到其他实例变量中。
'''




