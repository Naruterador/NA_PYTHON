#coding = utf - 8

'''
自定义一个生成器，该生成器可按顺序返回52张扑克牌，分别是黑桃、红心、草花、方块的2～A
'''



#使用生成器来输出52张扑克牌

def poke():
	print('========函数开始执行==========')
	flowers = ['spade','heart','clubs','diamond']

	for i in range(1,14):
		for j in flowers:
			if i == 1:
				yield 'A' + j
			elif i == 11:
				yield 'J' + j
			elif i == 12:
				yield 'Q' + j
			elif i == 13:
				yield 'K' + j
			else:
				yield str(i)+j

p = poke()

for i in p:
	print(i)