#coding = utf - 8


'''
扩展列表、元组和字典

列表、元组等不本身都实现了序列方法和迭代器方法，因此他们既是序列也是迭代器。


如果程序明确的需要一个特殊的列表、元组、或字典类，我们有两种选择:
1.自己实现序列、迭代器等各种方法，自己来实现这个特殊的类
2.扩展系统已有的列表、元组或字典

方法1比较繁琐，这意味着我们需要自己所有的方法都实现一遍
方法2比较简单，只要继承系统已有的列表、元组、或字典类，然后重写或新增方法既可。
'''


'''
下面程序开发一个新的字典，这个字典类可以根据value来获取key。由于字典中value是可以重复的
，因此该方法会返回指定value对应全部key组成的列表
'''

#定义ValueDict类，继承dict类

class ValueDict(dict):

	def __init__(self,*args,**kwargs):
		#调用父类构造函数
		super().__init__(*args,**kwargs)

	#新增getkeys方法
	def getkeys(self,val):
		result = []
		for key ,value in self.items():
			if value == val:
				result.append(key)
		return result


my_dict = ValueDict(Math = 1,chinese = 2,english = 2)
print(my_dict.getkeys(2))
my_dict['computer'] = 2
print(my_dict.getkeys(2))