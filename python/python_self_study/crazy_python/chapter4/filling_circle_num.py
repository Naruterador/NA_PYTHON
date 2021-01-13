#coding=utf-8
'''
给定4，应该输出如下形式的数据:

01 12 11 10
02 13 16 09
03 14 15 08
04 05 06 07

给定5，应该输出如下形式的数据:
01 16 15 14 13
02 17 24 23 12
03 18 25 22 11
04 19 20 21 10
05 06 07 08 09

仔细观察上面的试题，不难发程序就是“绕圈圈”填入整数。

掌握上面的规律之后，我们打算使用列表嵌套列表（相当于二维列表）的方式来存储这些整数，将
数值存入嵌套列表时需要遵守这种“绕圈圈”的规则，然后再以二维方式将这个嵌套列表打印出来。

为了控制“绕圈”，该程序的关键点就是控制绕圈的拐弯点。


输出空的二维列表:
方法1:
a = []
for i in range(4):
	a.append([])
	for i in range(4):
		a[i].append(0)


方法二：
a =[[0 for in range(4)]for in range(4)]


'''


class Fillnum(object):

	def __init__(self,num):
		self.num = num

	def __createEmptyContainer(self):
		self.list = [[0 for i in range(self.num)]for i in range(self.num)]


	def __drawCircle(self):
		self.__createEmptyContainer()
		x = 0
		y = 0
		i = 0
		t = self.num * self.num

		while(i < t):
			if(x + y) == (self.num - 1):
				if(x > y):
					if(x > y and y == 0):
						i = i + 1
						self.list[x][y] = i
					while( x != y):
						y = y + 1
						i = i + 1
						self.list[x][y] = i
				elif(x < y):
					while(x != y - 1):
						y = y - 1
						i = i + 1
						self.list[x][y] = i
		
			elif(x == y) and (x != 0) and (y != 0):
				self.list[x][y] = i
			
				while(((x + y) != (self.num - 1))):
					x = x - 1
					i = i + 1
					self.list[x][y] = i 

			elif(x == (y - 1)):
				while(((x + y) != (self.num - 1))):
					x = x + 1
					i = i + 1
					self.list[x][y] = i	
			else:
				i = i + 1
				self.list[x][y] = i
				x = x + 1

		return self.list


	def output(self):
		for i in self.__drawCircle():
			print(i)

list1 = Fillnum(4)
list1.output()


