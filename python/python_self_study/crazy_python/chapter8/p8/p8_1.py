#coding=utf-8


'''
序列相关的方法:

Python序列可以包含多个元素，开发者只要实现符合序列要求的特殊方法，就可实现
自己的序列。

序列最重要的特征就是包含多个元素，因此和序列有关的特殊方法有如下几个:

__len__(self):该方法的返回值决定序列中元素的个数
__getitem__(self,key):该方法获取指定索引对应的元素。该方法的key应该是整数值
					  或slice对象，否则该方法会引发KeyError异常
__contains__(self,item):该方法判断序列是否包含指定元素
__setitem__(self,key,value):该方法设置指定索引对应的元素。该方法的key应该是整数值
                            或slice对象，否则该方法会引发KeyError异常
__delitem__(self,key):该方法删除指定索引对应的元素


如果程序要实现不可变序列（程序只能获取序列中的元素，不能修改），只要实现上面前三个方法就行；如果
程序要实现可变序列（程序既能获取序列中的元素，也可修改），则需要实现上面5个方法。
'''

'''
下面程序实现一个字符串序列，在该字符串序列中默认每个字符串的长度都是3，该序列元素
按照AAA、AAB、AAC这种格式排列
'''


def check_key(key):
	'''
	该函数将会负责检查序列的索引，该索引必须是整数值，否则引发TypeError异常
	且程序要求索引必须为非负整数值，否则引发IndexError异常。
	'''
	
	if not isinstance(key,int):
		raise TypeError('索引值必须是整数')

	if key < 0:
		raise IndexError('索引值必须是非负整数')

	if key >= 26 ** 3:
		raise IndexError("索引值不能超过%d" % 26 ** 3)


class StringSeq(object):
	def __init__(self):
		#用于存储修改的数据
		self.__changed = {}
		#用于存储已删除元素的索引
		self.__deleted = []

	def __len__(self):
		return 26 ** 3    #26的三次方

	def __getitem__(self,key):
		'''
		根据索引获取序列中元素
		'''
		check_key(key)
		#如果在self.__changed中找到修改后的数据
		if key in self.__changed:
			return self.__changed[key]

		#如果key在self.__deleted中，说明该元素已经被删除
		if key in self.__deleted:
			return None

		#否则根据计算返回序列元素
		three = key //(26 * 26)
		two = (key - three *26 * 26) //26
		one = key % 26
		return chr(65 + three) + chr(65+two) + chr(65 + one)

	def __setitem__(self,key,value):
		'''
		根据索引修改序列中的元素
		'''
		check_key(key)
		#将修改的元素以key-value对的形式保存在__changed中
		self.__changed[key] = value

	def __delitem__(self,key):
		'''
		根据索引删除序列中元素
		'''

		check_key(key)
		#如果__deleted列表中没有包含被删除的key,则添加被删除的key
		if key not in self.__deleted:
			self.__deleted.append(key)
		#如果__changed中包含被删除的key,则删除它
		if key in self.__changed:
			del self.__changed[key]


#创建一个序列
sq = StringSeq()
#获取序列的长度，实际上就是__len__()方法的返回值
print(len(sq))
#打印序列sq[0]的值
print(sq[0])    #AAA
#修改元素sq[1]的值
sq[1] = 'fkit'
#删除sq[1]
del sq[1]
print(sq[1]) #None
#再次对sq[1]赋值
sq[1] = 'crazyit'
print(sq[1]) #crazyit