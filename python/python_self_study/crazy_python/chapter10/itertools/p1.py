#coding = utf - 8

import itertools

'''
itertools 模块中主要包含一些用于生成迭代器的函数。
使用[e for e in dir(itertools) if not e.startswith('_')]查看模块包含的所有功能和
属性。



>>> [e for e in dir(itertools) if not e.startswith('_')]
['accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 
'cycle', 'dropwhile', 'filterfalse', 'groupby', 'islice', 'permutations', 'product', 'repeat', 
'starmap', 'takewhile', 'tee', 'zip_longest']
'''



'''
itertools模块中三个生成无限迭代器的函数:
count(start,[step]):生成start,start+step,start+2*step,...迭代器，其中
step默认为1.比如count(10)生成的迭代器包含:10,11,12,13,14...

cycle(p):对序列p生成无限循环p0,p1,……,p0,p1,……,的迭代器。比如使用
cycle('ABCD')生成的迭代器包含:A,B,C,D,A,B,C,D,……。

repeat(elem,[,n]):生成无限个elem元素重复的迭代器，如果指定了参数n,则只
生成n个elem元素。比如使用repeat(10,3)生成的迭代器包含:10,10,10

'''

import itertools

#使用count(10,3)生成10、13、16……的迭代器
for e in itertools.count(10,3):
	print(e)
	#用于掉出无限循环
	if e > 20:
		break
print('------------')

#使用cycle用于生成无限循环的迭代器
my_counter = 0
for e in itertools.cycle(['python','Kotlin','Swift']):
	print(e)
	my_counter = my_counter + 1
	#用于跳出循环
	if my_counter > 7:
		break
#repeat用于生成n个元素重复的迭代器
for e in itertools.repeat('Python',3):
	print(e)