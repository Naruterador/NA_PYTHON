#coding=utf-8
'''
python为所有类都提供了一个__bases__属性，通过该属性可以查看该类的所有直接父类，该属性返回所有直接父类组成的元组。

python还为所有类都提供了一个__subclasses__()方法，通过该方法可以查看该类的所有直接子类，该方法返回该类的所有子类组成列表。

'''

class A:
	pass

class B:
	pass

class C(A,B):
	pass


print('类A所有父类:',A.__bases__)
print('类B所有父类:',B.__bases__)
print('类C所有父类:',C.__bases__)

print('类A的所有子类',A.__subclasses__())

print('类B的所有子类',B.__subclasses__())