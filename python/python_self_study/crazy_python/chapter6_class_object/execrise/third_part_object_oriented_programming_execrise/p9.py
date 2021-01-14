#coding=utf-8
'''
面向对象三大特性

封装 根据 职责 将 属性 和 方法 封装 到一个抽象的 类 中

定义类的准则
继承 实现代码的重用，相同的代码不需要重复的编写

设计类的技巧
子类针对自己特有的需求，编写特定的代码
多态 不同的 子类对象 调用相同的 父类方法，产生不同的执行结果

多态 可以 增加代码的灵活度
以 继承 和 重写父类方法 为前提
是调用方法的技巧，不会影响到类的内部设计


                        class designer----------Class human-----------class programmer                                     
                         work(self)              work(self)            work(self)



'''



'''
---------------------------------------------------------------
在 Dog 类中封装方法 game

普通狗只是简单的玩耍
定义 XiaoTianDog 继承自 Dog，并且重写 game 方法

哮天犬需要在天上玩耍
定义 Person 类，并且封装一个 和狗玩 的方法

在方法内部，直接让 狗对象 调用 game 方法
'''

class Dog(object):
	def __init__(self,name):
		self.name = name
	def game(self):
		print("%s dog is playing on the ground!" % self.name)

class XiaoTianDog(Dog):
	def game(self):
		print("%s dog is playing int the sky!" % self.name)

class Person(object):
	def __init__(self,name):
		self.name = name
	def game_with_dog(self,dog):
		print("%s is playing with %s now!" % (self.name,dog.name))
		

d1 = Dog("wangcai")
d1.game()

xtd = XiaoTianDog("xiaotian")
xtd.game()

p1 = Person("xiaoming")
p1.game_with_dog(d1)

