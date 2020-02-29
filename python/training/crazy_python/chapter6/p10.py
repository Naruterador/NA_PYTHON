#coding=utf-8
'''
关于多继承:
如果多个父类中包含了同名方法，此时排在前面的父类中的方法会“遮蔽”排在后面的父类中的同名方法
'''

class Item(object):
    def info(self):
        print("Item中方法:" + "这是一个商品")

class Product(object):
    def info(self):
        print("Product中的方法" + "这是一个工业产品")

 #继承时，哪个父类在前就调用哪个方法
class Mouse(Item,Product):
	pass

i = Mouse()
i.info()