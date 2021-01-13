#coding=utf-8
'''
用户随机输入n个大写字母，程序使用dict统计用户输入的每个字母次数
-------------------------------------------------------

>>>dict()                        # 创建空字典
{}
>>> dict(a='a', b='b', t='t')     # 传入关键字
{'a': 'a', 'b': 'b', 't': 't'}
>>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
{'three': 3, 'two': 2, 'one': 1} 
>>> dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
{'three': 3, 'two': 2, 'one': 1}
>>>
'''
#---------------------------------------------------------------------------


'''
class Lettercounts(object):
	def __init__(self,strings):
		self.strings = strings

	def __lenstring(self):
		i = len(self.strings)
		return i

	def __inputdict(self):
		i = 0
		dictem = {}
		while(i < self.__lenstring()):
			dictem[i + 1] = self.strings[i]
			i = i + 1
		return dictem

	def counttimes(self):
		i = 1
		c = 0 
		dictem = {}
		while(i <= self.__lenstring()):
			str1 = str(self.__inputdict())
			dictem[self.__inputdict()[i]] = str1.count(self.__inputdict()[i])
			i = i + 1
		return dictem

			
d1 = Lettercounts('AABBCCDDXTUOPPK')
print(d1.counttimes())
'''
#-------------------------------------------------------------------------------


'''
chr()          //将十进制值转化为字母
ord()          //将字母转化为对应ascii表的值
'''


str1 = input("请输入大写字母")
lstr = list(str1)

a_dict = dict.fromkeys([chr(i) for i in range(ord('A'),ord('Z')+1)],0)     #输出所有26字母的字典列表，键为26个大写字母，值为0
																		   #dict.fromkeys(） 用于输出当前字典所有的键值

for i in lstr:
    a_dict[i] += 1

print(a_dict)



