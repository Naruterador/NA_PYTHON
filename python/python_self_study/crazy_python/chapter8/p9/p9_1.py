#coding = utf-8

'''
迭代器(iterator)：
for循环遍历列表、元组、字典等，这些对象都是可迭代的，因此他们都属于迭代器

如果开发者要实现迭代器，只要实现下面两个方法即可:
__iter__(self):该方法返回一个迭代器，迭代器必须包含一个__next__()方法，该方法
			   返回迭代器的下一个元素
__reversed__(self):该方法主要为内建的reversed()反转函数提供支持，当程序调用reversed()函数
				   对指定迭代器执行反转时，实际上是由改方法实现的

如果程序不需要让迭代器反转迭代，其实只需要实现第一个方法即可。

'''

'''
斐波那契数列:
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，
故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
在数学上，斐波那契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用，为此，美国数学会从1963年起出版了以
《斐波纳契数列季刊》为名的一份数学杂志，用于专门刊载这方面的研究成果。
'''

#定义一个斐波那契数列的迭代器:
class Fibs(object):
	def __init__(self,len):
		self.first = 0 
		self.sec = 1
		self.__len = len
	#定义迭代器所需的__next__方法
	def __next__(self):
	#如果__len__属性为0,结束迭代
		if self.__len == 0:
			raise StopIteration
		#完成数学计算
		self.first ,self.sec = self.sec,self.first + self.sec 
		''' 
		 这种写法，Python先计算等号的右边(self.first+self.sec)赋值给self.sec
		 再将self.sec赋值给self.first
		'''

		#数列长度减1
		self.__len = self.__len - 1
		return self.first
	#定义__iter__方法，该方法返回迭代器
	def __iter__(self):
		return self

#创建Fibs对象
fibs = Fibs(10)
#获取迭代器的下一个元素
print(next(fibs))     #next()函数其实就是通过__next__方法来实现的

#使用for循环遍历迭代器
for el in fibs:
	print(el)


'''
程序开始使用内置的next()函数来获取迭代器的下一个元素，该next()函数其实就是通过迭代器的
__next__方法来实现的。
'''