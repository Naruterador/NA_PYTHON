#coding=utf-8

'''
使用type函数查看变量的类型，也可以是type函数查看某个类的类型
'''

class Role:
	pass

r = Role()

print(type(r))

print(type(Role))


'''
从上面的输出结果来看，role本身的类型是type。从python解释器的角度来讲，当程序使用class定义role类时
也可以理解为定义了一个特殊的对象，并将该对象赋值给role变量。
因此，程序使用class定义的所有类都是type类的实例

'''