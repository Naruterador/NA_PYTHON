

class Student:
   
    def __init__(self, n = "xxx"):
        self.name = n

    @classmethod
    def show(cls):
        s = cls()
        print(s.name)


s = Student("yyy")
s.show()

'''
class People(object):
    country = 'china'  #类属性

print(People.country)   #china
p = People()
print(p.country)    #china
p.country = 'japan' 
print(p.country)  # 实例属性会屏蔽掉同名的类属性：japan
print(People.country)   #china
del p.country  # 删除实例属性
print(p.country)    #实例属性被删除后，再调用同名称的属性，会调用类属性：china

总结:
如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。
如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，不会影响到类属性
并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。
'''





