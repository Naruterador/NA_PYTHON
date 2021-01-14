#coding=utf-8
'''

python完全允许使用type()函数来创建type()对象，又由于type类的实例就是类，
因此python可以使用type()函数来动态创建类。

'''


def fn(self):
	print('fn函数')

#使用type()定义dog类
Dog = type('Dog',(object,),dict(walk=fn,age=6))
'''
参数分别代表：
参数1:创建类名
参数2:该类继承的父类集合。由于python支持多继承，因此这里使用元组指定它的多个父类。需要多写一个逗号
参数3:使用字典对象为该类绑定的类变量和方法。其中key是类变量名或者类的方法名，如果字典value是普通值
那就代表类变量；如果字典的value是函数，则代表方法。
'''

d = Dog()

print(type(d))

print(type(Dog))

d.walk()

print(d.age)