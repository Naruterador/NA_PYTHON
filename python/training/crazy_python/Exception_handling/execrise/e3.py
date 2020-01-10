#coding=utf-8

'''
提供一个字符串元组，程序要求字元组中每一个元素的长度都在5~20之间;否则,程序引发异常。
'''

class SelfExcepttion(Exception):
	pass

a = ['123456','123456','1235','1234ladsfjlajsflj']

index  = 0
for i in a:
	try:
		if len(i) >= 5 and len(i) <= 20:
			print("NO.%s elements are in correct formula." % index)
		else:
			raise SelfExcepttion("The incorrect formula!")
	except SelfExcepttion as e:
		print(e)
	index = index + 1
