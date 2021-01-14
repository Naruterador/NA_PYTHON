#coding=utf-8
'''
利用二维列表还可以完成五子棋、连连看、俄罗斯方块、扫雷等常见小游戏。下面简单介绍利用二维列表实现五子棋。
先定义一个二维列表作为棋盘，每当一个对手下一步棋时，也就是二维列表的一个数组元素赋值。下面程序完成了这个游戏的初步功能：

编写电脑下棋，电脑下棋可以使用随机生成的两个坐标值来控制，当然也可以增加人工智能来控制下棋。


保证在用户和电脑下的棋的坐标上不能有棋子（通过判断对应数组元素只能是+来确定），还需要进行4次循环扫描，判断横、竖、左斜、右斜是否五颗棋子连在
一起，从而判定胜负。

下面程序，用于排列表中的连续数字(从小到大)：
from itertools import groupby

lst = [1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 19]    # 连续数字

fun = lambda x: x[1]-x[0]        #匿名函数lambda
for k, g in groupby(enumerate(lst), fun):
    l1 = [j for i, j in g]    # 连续数字的列表
    if len(l1) > 1:
        scop = str(min(l1)) + '-' + str(max(l1))    # 将连续数字范围用"-"连接
    else:
        scop = l1[0]
    print("连续数字范围：{}".format(scop))

函数介绍：
1.enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
例:
	seasons = ['Spring', 'Summer', 'Fall', 'Winter']
	list(enumerate(seasons))
	输出：
	[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]



	for循环使用:	
	>>>seq = ['one', 'two', 'three']
	>>> for i, element in enumerate(seq):
	...     print i, element
	... 
	0 one
	1 two
	2 three

2.groupby

	from operator import itemgetter #itemgetter用来去dict中的key，省去了使用lambda函数
	from itertools import groupby #itertool还包含有其他很多函数，比如将多个list联合起来。。
	d1={'name':'zhangsan','age':20,'country':'China'}
	d2={'name':'wangwu','age':19,'country':'USA'}
	d3={'name':'lisi','age':22,'country':'JP'}
	d4={'name':'zhaoliu','age':22,'country':'USA'}
	d5={'name':'pengqi','age':22,'country':'USA'}
	d6={'name':'lijiu','age':22,'country':'China'}
	lst=[d1,d2,d3,d4,d5,d6]

	#通过country进行分组：

	lst.sort(key=itemgetter('country')) #需要先排序，然后才能groupby。lst排序后自身被改变
	lstg = groupby(lst,itemgetter('country')) 
	#lstg = groupby(lst,key=lambda x:x['country']) 等同于使用itemgetter()


	for key,group in lstg:
	    for g in group: #group是一个迭代器，包含了所有的分组列表
	        print key,g
	返回：
	China {'country': 'China', 'age': 20, 'name': 'zhangsan'}
	China {'country': 'China', 'age': 22, 'name': 'lijiu'}
	JP {'country': 'JP', 'age': 22, 'name': 'lisi'}
	USA {'country': 'USA', 'age': 19, 'name': 'wangwu'}
	USA {'country': 'USA', 'age': 22, 'name': 'zhaoliu'}
	USA {'country': 'USA', 'age': 22, 'name': 'pengqi'}

原理：
groupby（）函数在每次迭代的时候，会返回一个分组后的日期值和一个迭代器对象，迭代器对象包含对应日期值的所有对象。

注：在使用groupby函数有一个很重要的步骤，就是我们要在使用groupby函数前，使用itemgetter函数将字典进行排序。如果没有排序，我们是得不到想要的结果。

'''

import random
from itertools import groupby

class Gobang(object):

	def __init__(self,size):
		#chess board size
		self.board_size = size 
		self.board_init = []
		self.board = ''

		self.humanstep = []
		self.comstep = []

		self.humanX = 0
		self.humanY = 0
		self.inputStr = 0

		self.comX = 0
		self.comY = 0


    #初始化棋盘
	def __initboard(self):
		for i in range(self.board_size):
			row = ["†"] * self.board_size
			self.board_init.append(row)

	#创建棋盘
	def __createboard(self):
		for i in range(self.board_size):
			for j in range(self.board_size):
				self.board = self.board + self.board_init[i][j]
			self.board = self.board + '\n'

	#人类下棋
	def __humanchess(self,inputStr):
		lista = []
		if(inputStr != None):
			x_str,y_str = inputStr.split(",")
			if(x_str.isdigit() and y_str.isdigit()):         #判断输入的值是否是数字
				if(int(x_str) <= self.board_size and int(y_str) <= self.board_size and int(x_str) != 0 and int(y_str) != 0):     #输入的坐标不能超过board_size且不能为0
					self.humanX = int(x_str) - 1。    #这里因为人输入的坐标从1，1开始，所以需要减去1
					self.humanY = int(y_str) - 1
					lista.append(self.humanX)
					lista.append(self.humanY)

					if ((lista in self.humanstep) or (lista in self.comstep)):     #检测人走的这步棋是否重复了（计算机重复或人重复）
						lista = []                                                 #将lista清空并直接返回假值
						return False
					else:
						self.humanstep.append(lista)                               #如果走的这步棋满足要求，就将这步棋放入humanstep这个列表，为后面计算规则做准备
						lista = []
						self.board_init[self.humanX][self.humanY] = '○'            #将这步棋放到棋盘上
						return True                                                #并且返回真，表示这步棋走过了
				else:
					return False    
			else:
				return False
		else:
			return False
			

	#计算机下棋
	def __computerchess(self):
		lista = []
		self.comX = random.randint(0,self.board_size - 1)                #生成随机数的横坐标
		self.comY = random.randint(0,self.board_size - 1)                #生成随机数的纵坐标
		lista.append(self.comX)
		lista.append(self.comY)

		while((lista in self.humanstep) or (lista in self.comstep)):     #如果这步棋已经下过了（包括机器和人）就重新将生成新的一步棋
			lista = []
			self.comX = random.randint(0,self.board_size - 1)
			self.comY = random.randint(0,self.board_size - 1)
			lista.append(self.comX)
			lista.append(self.comY)

		self.comstep.append(lista)。                                    #将每步棋记录 放入comstep列表
		self.board_init[self.comX][self.comY] = '●'                     #将计算机下的这步棋放到棋盘上


	#人类规则判断输赢
	def __HCombatrules(self):
		lista = []
		listb = []
		listc = []
		fun = lambda x:x[1] - x[0]
		fun1 = lambda x:x[0] + x[1]
		fun2 = lambda x:x[0] - x[1]
		revalue = False
		'''
		判断纵方向赢的思路：
		1.纵坐标相同，都是一个固定值，将所有纵坐标的便利一遍，找到所有纵坐标相同，横坐标不同的值，加入列表
		2.当列表等于或超过5个，对列表进行排序
		3.使用groupby找出是否有5个连续的值，如果有就赢了
		'''

		if len(self.humanstep) >= 5:                         #游戏步数大于等于5才进行判断
			for i in range(0,self.board_size):               #纵向判断游戏是否赢了
				for j in self.humanstep:
					if(j[1] == i):
						lista.append(j)
				if len(lista) >= 5:
					for i in lista:
						listb.append(i[0])
					listb = sorted(listb)
					for k, g in groupby(enumerate(listb), fun):
						l1 = [j for i, j in g]
						if len(l1) == 5:
							revalue = True
							return revalue
						else:
							revalue = False
							listb = []
			lista = []
			liatb = []

		 '''
		 判断横方向赢的思路：
		 1.横坐标相同，都是一个固定值，将所有横坐标的便利一遍，找到所有横坐标相同，纵坐标不同的值，加入列表
		 2.当列表等于或超过5个，对列表进行排序
		 3.使用groupby找出是否有5个连续的值，如果有就赢了
		 '''

			for i in range(0,self.board_size):               #横向判断游戏是否赢了
				for j in self.humanstep:
					if(j[0] == i):
						lista.append(j)
				if len(lista) >= 5:
					for i in lista:
						listb.append(i[1])
					listb = sorted(listb)
					for k, g in groupby(enumerate(listb), fun):
						l1 = [j for i, j in g]
						if len(l1) == 5:
							revalue = True
							return revalue
						else:
							revalue = False
							listb = []

			lista = []
			listb = []
			
			'''
			判断左斜是否赢了：
			1.左斜的特点是，所有节点，横坐标和纵坐标的和相等
			2.找出所有横坐标和纵坐标相加相等的值，去掉重复的值
			3.在列表中找出相加等于前面相等值的元素，放入新的列表
			4.使用groupby判断是否有5个连续的值，如果有就赢了
			'''

			for k,g in groupby(self.humanstep,fun1):        #判断左斜是否是否赢了
				lista.append(k)
			lista = list(set(lista))
			for i in lista:
				for j in self.humanstep:
					if((j[0] + j[1]) == i):
						listb.append(j)
				if(len(listb) >= 5):
					for i in listb:
						listc.append(listb[0])
					for k, g in groupby(enumerate(listc), fun):
						l1 = [j for i, j in g]
						if len(l1) == 5:
							revalue = True
							return revalue
						else:
							revalue = False

			lista = []
			listb = []
			listc = []

			'''
			判断右斜是否赢了：
			1.右斜的特点是，所有节点，横坐标和纵坐标的差相等
			2.找出所有横坐标和纵坐标相减相等的值，这个值不能为负数，去掉重复的值
			3.在列表中找出相减等于前面相减值的元素，放入新的列表
			4.使用groupby判断是否有5个连续的值，如果有就赢了
			'''

			for k,g in groupby(self.humanstep,fun2):     #判断左斜是否赢了
				if k >= 0:
					lista.append(k)
			lista = list(set(lista))
			for i in lista:
				for j in self.humanstep:
					if((j[0] - j[1]) == i):
						listb.append(j)
				if(len(listb) >= 5):
					for i in listb:
						listc.append(listb[0])
					for k, g in groupby(enumerate(listc), fun):
						l1 = [j for i, j in g]
						if len(l1) == 5:
							revalue = True
							return revalue
						else:
							revalue = False

		return revalue

    #计算机规则判断输赢
	def __CComputerrules(self):
		lista = []
		listb = []
		listc = []
		fun = lambda x: x[1]-x[0]
		fun1 = lambda x:x[0] + x[1]
		fun2 = lambda x:x[0] - x[1]
		revalue = False


		if len(self.comstep) >= 5:
			for i in range(0,self.board_size):
				for j in self.comstep:
					if(j[1] == i):
						lista.append(j)
				if len(lista) >= 5:
					for i in lista:
						listb.append(i[0])
					listb = sorted(listb)
					for k, g in groupby(enumerate(listb), fun):
						l1 = [j for i, j in g]
						if len(l1) == 5:
							revalue = True
							return revalue
						else:
							revalue = False
							listb = []
			lista = []
			liatb = []

			for i in range(0,self.board_size):
				for j in self.comstep:
					if(j[0] == i):
						lista.append(j)
				if len(lista) >= 5:
					for i in lista:
						listb.append(i[1])
					listb = sorted(listb)
					for k, g in groupby(enumerate(listb), fun):
						l1 = [j for i, j in g]
						if len(l1) == 5:
							revalue = True
							return revalue
						else:
							revalue = False
							listb = []


			lista = []
			listb = []

			for k,g in groupby(self.comstep,fun1):
				lista.append(k)
			lista = list(set(lista))
			for i in lista:
				for j in self.comstep:
					if((j[0] + j[1]) == i):
						listb.append(j)
				if(len(listb) >= 5):
					for i in listb:
						listc.append(listb[0])
					for k, g in groupby(enumerate(listc), fun):
						l1 = [j for i, j in g]
						if len(l1) == 5:
							revalue = True
							return revalue
						else:
							revalue = False

			lista = []
			listb = []
			listc = []


			for k,g in groupby(self.comstep,fun2):
				if k >= 0:
					lista.append(k)
			lista = list(set(lista))
			for i in lista:
				for j in self.comstep:
					if((j[0] - j[1]) == i):
						listb.append(j)
				if(len(listb) >= 5):
					for i in listb:
						listc.append(listb[0])
					for k, g in groupby(enumerate(listc), fun):
						l1 = [j for i, j in g]
						if len(l1) == 5:
							revalue = True
							return revalue
						else:
							revalue = False				
		
		return revalue

			


	#开始游戏
	def __HumanfirstCombat(self):
		lista = []
		self.__initboard()
		while(1):
			self.inputStr = input("Please enter your chess coordinate(the formulation is 'x,y'):")
			if(self.__humanchess(self.inputStr)):   #如果人类下棋返回真就输出当前棋盘
				if (self.__HCombatrules()):    #如果满足游戏规则，人赢
					print('Human win!')
					self.__createboard()
					print(self.board)
					break                     #人赢了就结束游戏                        

				self.__computerchess()         #机器人下棋

				if (self.__CComputerrules()):  #如果满足游戏规则，机器赢
					print('Computer win!')
					self.__createboard()
					print(self.board)
					break                      #机器赢了就结束游戏

				self.__createboard()
				print(self.board)
				self.board = ''







	def printout(self):
		self.__HumanfirstCombat()         #输出游戏画面

gobang = Gobang(10)
gobang.printout()




