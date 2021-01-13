#coding=utf-8
'''

打印出所有的水仙花数。
水仙花数是指一个三位数，其各位数字的立方和等于该数本身。例如153时一个水仙花数，因为153 = 1^3 + 5^3 + 3^3


'''

class daffodil(object):

	def __init__(self,num):
		self.num = num

	def __handleNum(self,num):
		a = str(num)
		b = 0
		q = 0

		for i in a:
			b = int(i)
			q = q + (b * b * b)

		if num == q:
			return True
		else:
			return False

	def checkOnenum(self):
		if (self.__handleNum(self.num)):
			return "This is a daffodil number!"
		else:
			return "This is not a daffodil number!"


	def rangeNum(self):
		list1 = []
		for i in range(1,self.num + 1):
			if (self.__handleNum(i)):
				list1.append(i)
			else:
				pass
		return list1

d1 = daffodil(153)
#print(d1.checkOnenum())
print(d1.rangeNum())





