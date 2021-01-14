#coding = utf -8

'''
自定义代表扑克牌的Card类(包括花色和牌面值)，为Card类提供自定义的比较大小的运算符支持
大小比较标准是先比较牌面值
如果牌面值相等则比较花色，花色大小规则为:黑桃>红心>草花>方块
'''

class Card(object):
	#初始化花和牌
	def __init__(self,flower,cards):
		self.cards = cards
		self.flower = flower

	#定义__gt__方法，该对象可支持">"和"<"
	def __gt__(self,other):
		if not isinstance(other,Card):
			raise TypeError('>操作的目标必须是Card类')
		flowerlist = ['d','c','h','s']

		#先比较牌面大小
		if self.cards > other.cards:
			return True

		#在牌面大小一样的情况下比较花的大小
		if self.cards == other.cards:
			if flowerlist.index(self.flower) > flowerlist.index(other.flower):
				return True
		return False


	#定义__eq__方法，该对象可支持"=="和"!="
	def __gt__(self,other):
		if not isinstance(other,Card):
			raise TypeError('>操作的目标必须是Card类')
		flowerlist = ['d','c','h','s']

		#只要牌面相等就相等
		if self.cards == other.cards:
			return True

		#在牌面和花都必须要相等才能相等
		#if self.cards == other.cards:
		#	if flowerlist.index(self.flower) == flowerlist.index(other.flower):
		#		return True
		#return False




c1 = Card('s',1)
c2 = Card('h',1)

if c1 > c2:
	print(True)