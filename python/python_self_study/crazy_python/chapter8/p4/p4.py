#coding=utf -8

'''
__dict__属性用于查看对象内部存储的所有属性名和属性值组成的字典，通常程序直接使用该属性即可。
程序使用__dict__属性既可查看对象的所有内部状态，也可通过字典语法来访问或修改指定属性的值。
'''

class Item(object):
	def __init__(self,name,price):
		self.name = name 
		self.price = price

im = Item('鼠标',29.8)

print(im.__dict__)  #返回对象内部的属性及属性名
print(im.__dict__['name'])        #通过__dict__访问对象内的属性name
print(im.__dict__['price'])       #通过__dict__访问对象内的属性price
