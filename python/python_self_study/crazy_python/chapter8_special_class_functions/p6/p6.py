#coding = utf-8

'''
与反射相关的属性和方法:
如果程序在运行过程中要动态判断是否包含某个属性(包括方法),甚至要
动态设置某个属性值，则可通过python的反射支持来实现。

动态操作属性:
hasattr(obj,name):检查属性是否包含名为name的属性或方法
getattr(obj,name[,default]):获取obj对象中名为name的属性的属性值
setattr(obj,name,value,/):将obj对象的name属性设为value
'''

class Comment(object):

	def __init__(self,detail,view_times):
		self.detail = detail
		self.view_times = view_times

	def info():
		print("一条简单的评论，内容是%s" % self.detail)

c = Comment('疯狂python讲义很不错','20')

#判断是否包含指定的属性和方法
print(hasattr(c,'detail'))           #True
print(hasattr(c,'view_times'))       #True
print(hasattr(c,'info'))             #True

#获取指定属性的属性值
print(getattr(c,'detail'))           #'疯狂Python讲义很不错'
print(getattr(c,'view_times'))       # 20

#由于info是方法，故下面代码会提示:name 'info' is not defined
#print(getattr(c,info,'默认值'))

#为指定属性设置属性值
setattr(c,'detail','天气不错')
setattr(c,'view_times',32)

#输出重新设置的值
print(c.detail)
print(c.view_times)

#设置不存在的属性test，即为对象添加属性
setattr(c,'test','新增测试方法')
print(c.test)

#通过setattr()函数还可以对方法进行设置，setattr()函数重新设置对象的方法时，新设置的方法是未绑定方法。
def bar():
	print ('一个简单的bar方法')	
#将c的info方法设为bar函数
setattr(c,'info',bar)
c.info()

#settar函数还可以将info()方法设置成普通值，这样会把info变成一个属性，而不是方法
#将c的info设置为字符串'fkit'
setattr(c,'info','fkit')
c.info()                 #这里代码会提示TypeError: 'str' object is not callable错误，因为info方法变成了属性。
