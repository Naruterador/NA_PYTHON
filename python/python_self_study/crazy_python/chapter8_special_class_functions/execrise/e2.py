#coding = utf - 8

'''
自定义一个序列，该序列按顺序包含所有三位数(如100,101,102...)。
要求:提供序列的各种操作方法
'''


class Seq(object):
	def __init__(self):
		self.__changed = {}
		self.__deleted = []

	def __len__(self):
		return 899

	def __check(self,key):
		if not isinstance(key,int):
			raise TypeError('Please type a integer')
		if key < 0:
			raise IndexError('Index number must be bigger 0')
		if key > 899:
			raise IndexError('Index number out of the range!')

	def __getitem__(self,key):
		self.__check(key)
		result = 0

		if key in self.__changed:
			return self.__changed[key]

		if key in self.__deleted:
			return None

		result = key + 100

		return result

	def __setitem__(self,key,value):
		self.__check(self)

		self.__changed[key] = value

	def __contains__(self,item):
		pass

	def __delitem__(self,key):
		self.__check(key)

		if key not in self.__deleted:
			self.__deleted.append(key)

		if key in self.__changed:
			del self.__changed[key]

s = Seq()
print(s[100])