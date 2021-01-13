#coding = utf - 8

'''
自定义一个序列，该序列按顺序包含52张扑克牌，分别是:
黑桃(spade)、红心(heart)、草花(clubs)、方块(diamond)的2~A。
要求:提供序列的各种操作方法
'''


class Poke(object):

	def __init__(self):
		#用于放置修改的值
		self.__changed = {}
		#用于放置被删除的值
		self.__deleted = []

	def __check(self,key):
		#对序列的索引值进行检查是否符合要求
		if not isinstance(key,int):
			raise TypeError('Please type a integer!')

		if key < 1:
			raise IndexError('Index number can not less than 0')

		if key > 52:
			raise IndexError('Index number can not bigger than 52')

	#输出序列的长度
	def __len__(self):
		return 52    

	def __getitem__(self,key):
		self.__check(key)
		s = 'spade'
		h = 'heart'
		c = 'clubs'
		d = 'diamond'

		#如果key在修改的序列中就输出修改的数据
		if key in self.__changed:
			return self.__changed[key]

		#如果序列被删除就输出None
		if key in self.__deleted:
			return None


		if key >= 1 and key <=13:
			if key + 1 == 11:
				return s + ',' + 'j'
			elif key + 1 == 12:
				return s + ',' + 'q'
			elif key + 1 == 13:
				return s + ',' + 'K'
			elif key + 1 == 14:
				return s + ',' + 'A'
			else:
				return s + ',' + str(key + 1)

		if key >=14 and key <= 26:
			if key + 1 == 24:
				return h + ',' + 'j'
			elif key + 1 == 25:
				return h + ',' + 'q'
			elif key + 1 == 26:
				return h + ',' + 'K'
			elif key + 1 == 27:
				return h + ',' + 'A'
			else:
				return h + ',' + str(key + 1)

		if key >=27 and key <= 39:
			if key + 1 == 36:
				return c + ',' + 'j'
			elif key + 1 == 37:
				return c + ',' + 'q'
			elif key + 1 == 39:
				return c + ',' + 'K'
			elif key + 1 == 40:
				return c + ',' + 'A'
			else:
				return c +',' + str(key + 1)

		if key >=40 and key <= 52:
			if key + 1 == 50:
				return d + ',' + 'j'
			elif key + 1 == 51:
				return d + ',' + 'q'
			elif key + 1 == 52:
				return d + ',' + 'K'
			elif key + 1 == 53:
				return d + ',' + 'A'
			else:
				return d + ',' + str(key + 1)




	def __setitem__(self,key,value):
		self.__check(key)

		#修改索引为Key的序列的值
		self.__changed[key] = value

	#判断key在不在序列中
	def __contains__(self,item):
		if item in self.__changed:
			return True

		if item >= 1 and item <= 52:
			return True

		return False



	def __delitem__(self,key):
		self.__check(key)
		#如果删除序列的key不在删除表中，就将他放在删除表中
		if key not in self.__deleted:
			self.__deleted.append(key)

		#如果删除的序列key在__changed中就将其删除
		if key in self.__changed:
			del self.__changed[key]



p = Poke()
print(len(p))


