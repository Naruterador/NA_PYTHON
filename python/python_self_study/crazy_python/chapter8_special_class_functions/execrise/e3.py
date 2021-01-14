#coding = utf-8

'''
自定义一个迭代器，该迭代器分别返回1,1+2,1+2+3....的累积和。
'''




#定义一个累加的迭代器
class Aplus(object):
	def __init__(self,len):
		self.__len = len
		self.result = 0
		self.nextn = 1

	#定义累加迭代器的__next__()方法
	def __next__(self):
		#如果迭代器的长度为0就抛出停止迭代的异常
		if self.__len == 0:
			raise StopIteration

		#完成累加的数学计算
		self.result = self.result + self.nextn
		self.nextn += 1

		#数列长度每次减一
		self.__len = self.__len	- 1
		#返回结果
		return self.result

	def __iter__(self):
		return self

ap = Aplus(10)

print(next(ap))
print(next(ap))
print(next(ap))
print(next(ap))
print(next(ap))
print(next(ap))
print(next(ap))
print(next(ap))


