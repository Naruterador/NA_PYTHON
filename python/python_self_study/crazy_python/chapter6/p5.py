#coding=utf-8
'''
property函数语法格式如下：
property(fget=None,fset=None,fdel=None,doc=None)

从上面的语法格式可以看出，使用property()函数时，可以传入4个参数，分别代表getter方法，setter方法，del方法和doc，其中
doc是一个文档字符串，用于说明该属性。当然，开发者调用property也可以传入0个(既不能读也不能写的属性)，1个（只读属性），2个（读写属性3个（读写属性，也可以删除））
和4个（读写属性，也可删除，包含文档说明）参数。
'''

class Rectangle(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def setsize(self,size):
        self.width , self.height = size

    def getsize(self):
        return self.width,self.height

    def delsize(self):
        self.width,self.height = 0,0

    #使用property定义属性
    size = property(getsize,setsize,delsize,'用于描述矩形大小的属性')

print(Rectangle.size.__doc__)  #访问size属性查看说明文档

help(Rectangle.size)           #通过内置的help函数查看Rectangle.size的文档说明

rect = Rectangle(4,3)

print(rect.size)               #访问rect的size属性

rect.size = 9,7                #对rect的size属性赋值

print(rect.width)
print(rect.height)

rect.delsize()


