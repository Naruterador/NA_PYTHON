#coding = utf - 8

import itertools

'''
accumulate(p[,func]):默认生成根据序列p元素累加的迭代器，p0,p0+p1,p0+p1+p2……
序列，如果指定了func函数，则用func函数来计算下一个元素值

chain(p,q,...):将多个序列里的元素“链”在一起生成新的序列。

compress(data,selectors):根据selectors序列的值对data序列的元素进行过滤。如果selector[0]
为真，则保留data[0];如果selector[1]为真，则保留data[1]……依此类推

dropwhile(pred,seq):使用pred函数对序列进行过滤，从seq中第一个使用pred函数计算为
False的元素开始，保留从该元素到序列结束的全部元素。

takewhile(pred,seq):该函数和上一个函数恰好相反。使用pred函数对seq序列进行过滤，从
seq中第一个使用pred函数计算为False的元素开始，去掉从该元素到序列结束的全部元素。

filterfalse(pred,seq):使用pre函数对seq序列进行过滤，保留seq中使用pred计算为True
的元素。比如filterfalse(lambda x:x%2,range10)

islice(seq,[start,] stop [,step]):其功能类似于序列的slice方法，实际上就是返回
seq[start:stop:step]的结果

starmap(func,seq):使用func对seq序列的每个元素进行计算，将计算结果作为新的序列元素。当使用
func计算序列元素时，支持序列解包。比如seq序列的元素长度为3，那么func可以是一个接受三个参数的
函数，该函数将会根据这三个参数来计算新序列的元素。

zip_longest(p,q,……):将p、q等序列中的元素按索引合并成元组，这些元组将作为新序列的元素。
'''
#默认使用累加的方式计算下一个元素的值
for e in itertools.accumulate(range(6)):
	print(e,end=',')
print('\n------------------------------')
#使用x*y的方式来计算迭代器下一个元素的值
for e in itertools.accumulate(range(1,6),lambda x,y:x * y):
	print(e,end=', ')
print('\n------------------------------')
#将两个序列"链"在一起，生成新的迭代器
for e in itertools.chain(['a','b'],['Kotlin','Swift']):
	print(e,end=' ')
print('\n------------------------------')
#根据第二个序列来筛选第一个序列的元素
#由于第二个序列只有中间两个元素为1(True),因此第一个序列只保留中间两个元素
for e in itertools.compress(['a','b','Kotlin','Swift'],[0,1,1,0]):
	print(e,end=', ')
print('\n------------------------------')
#获取序列中从长度不小于4的元素开始到结束的所有元素
for e in itertools.dropwhile(lambda x:len(x) < 4,['a','b','Kotlin','x','y']):
	print(e,end = ', ')
print('\n------------------------------')
#去掉序列中长度不小于4的元素开始到结束的所有元素
for e in itertools.takewhile(lambda x:len(x) < 4,['a','b','Kotlin','x','y']):
	print(e,end=', ')
print('\n------------------------------')
#只保留序列中长度不小于4的元素
for e in itertools.filterfalse(lambda x:len(x) < 4,['a','b','Kotlin','x','y']):
	print(e,end=' ,')
print('\n------------------------------')
#使用pow函数对原序列的元素进行计算，将计算结果作为新序列的元素
for e in itertools.starmap(pow,[(2,5),(3,2),(10,3)]):
	print(e,end = ', ')
print('\n------------------------------')
#将'ABCD'、'xy'的元素按索引合并成元组，这些元组1将作为新序列的元素
#长度不够的序列使用'-'字符代替
for e in itertools.zip_longest('ABCD','xy',fillvalue='-'):
	print(e,end=', ')
print('\n------------------------------')


