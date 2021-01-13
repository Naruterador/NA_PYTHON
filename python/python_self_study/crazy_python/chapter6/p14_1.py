#coding=utf-8
'''
对象动态添加方法，但是所添加的方法只是对当前对象有效，如果希望为所有实例都添加方法，则可通过类添加方法来实现。
MethodType可以把外部函数(方法)绑定到类或类的实例中

而python2跟python3中MethodType的用法不尽相同，下面是它们的区别：

python2:

公共部分：

class Student(object):
    pass
 
def set_name(self, name):
    self.name = name

（1）把方法绑定到类的实例中：
s1 = Student()
s2 = Student()
s3 = Student()
#将方法绑定到s1和s2实例中
s1.set_name = MethodType(set_name, s1, Student)
s2.set_name = MethodType(set_name, s2, Student)
#使用刚绑定的方法
s1.set_name('s1')
s2.set_name('s2')
#输出
print(s1.name)#s1
print(s2.name)#s2
print(s3.name)#报错:'Student' object has no attribute 'name'

（2）把方法绑定到类中（无None参数）
s1 = Student()
s2 = Student()
s3 = Student()
#将方法绑定到类中(没有None参数)
Student.set_name = MethodType(set_name,Student)
s1.set_name('s1')
s2.set_name('s2')
#输出
print(s1.name)#s2
print(s2.name)#s2
print(s3.name)#s2
MethodType把方法绑定在类上并且没有None参数时，通过该类创建的实例的该方法都会指向相同的区域，
相当于Java或C++中的static方法，导致后面s2实例的值会覆盖前面s1实例的值，即使s3没有使用该方法也会带上s2值。

（3）把方法绑定到类中（有第二个参数None）
s1 = Student()
s2 = Student()
s3 = Student()
#将方法绑定到类上（注意第二个参数多了None）
Student.set_name = MethodType(set_name,None,Student)
s1.set_name('s1')
s2.set_name('s2')
#输出
print(s1.name)#s1
print(s2.name)#s2
print(s3.name)#报错：'Student' object has no attribute 'name'
MethodType把方法绑定在类上且有第二个None参数时，相当于没指定给哪个实例绑定此方法，
则默认为该类的全部实例都绑定上此方法。这种情况下和绑定到实例上效果一样，
通过该类创建的实例会指向各自不同的区域，各个实例之间的方法和name属性互不干扰。

 
-------------------------------------------------------------
python3:

公共部分：

class Student(object):
    pass
 
def set_name(self, name):
    self.name = name


（1）把方法绑定到类的实例中：
s1 = Student()
s2 = Student()
s3 = Student()
#分别给s1和s2实例绑定此方法
s1.set_name = MethodType(set_name, s1)           #跟2版本相比变成两个参数，即去掉了后面的所属类参数
s2.set_name = MethodType(set_name, s2)
#输出
s1.set_name('s1')
s2.set_name('s2')
print(s1.name)#s1
print(s2.name)#s2
print(s3.name)#报错：AttributeError: 'Student' object has no attribute 'name'
注意：与python2相比MethodType()只接收两个参数，即去掉了所属类的参数。
也就没有为全部实例绑定该方法的情况了

（2）把方法绑定到类中（情况只有一种了，如上面python2的没有None参数）
s1 = Student()
s2 = Student()
s3 = Student()
#将方法绑定到类上
Student.set_name = MethodType(set_name,Student)
s1.set_name('s1')
s2.set_name('s2')
#输出
print(s1.name)#s2
print(s2.name)#s2
print(s3.name)#s2


如果类本身也有其它设置name属性的方法呢？
把公共部分改成如下：

class Student(object):
    def set_name_self(self,name):
        self.name = name
    pass
 
def set_name(self, name):
    self.name = name
即增加了类本身的设置name属性的方法set_name_self

s1 = Student()
s2 = Student()
s3 = Student()
#将方法绑定到类中
Student.set_name = MethodType(set_name,Student)
s1.set_name_self('s1_self')
s2.set_name('s2')
s2.set_name_self('s2_self')
#输出
print(s1.name)#s1_self
print(s2.name)#s2_self
print(s3.name)#s2

s1先调用类本身的方法赋值's1_self'，后s2调用的set_name并没有覆盖掉s1中name属性的值，
而s2的set_name_self把s2第一次调用的set_name为name属性设置的值给覆盖掉了，
s3没有为name设值，而因为s2.set_name方法是类方法，因而s3的name也是s2
'''

class Cat(object):
    def __init__(self,name):
        self.name = name

def walk_func(self):
    print("%s 慢慢地走过一片草地" % self.name)

d1 = Cat('Garfield')
d2 = Cat('Kitty')

#d1.walk()   因为类中没有这个方法,所以这里调用时会报错

#为Cat动态添加walk方法，该方法的第一个参数会自动绑定
Cat.walk = walk_func     #1

d1.walk()
d2.walk()

'''
程序中1号代码为Cat动态添加了walk方法，为类动态添加方法时，不需要使用MethodType进行包装，该函数的第一个参数会自动绑定。
'''