#coding=utf-8
'''
lambda表达式语法格式:
	lambda [parameter_list]:表达式
	lambda语法格式的特点如下：
	1.lambda表达式必须使用lambda关键字定义
	2.在lambda之后、冒号左边是参数列表，右边是表达式返回的值
	举例:
	lambda x,y:x+y
	可以改写为
	def add(x,y):
		return x + y
'''



'''
map函数解释
map() 会根据提供的函数对指定序列做映射。

map() 函数语法：
map(function, iterable, ...)


参数:
function -- 函数
iterable -- 一个或多个序列

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。


以下实例展示了 map() 的使用方法：

>>>def square(x) :            # 计算平方数
...     return x ** 2
... 
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
 
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]

'''


#传入计算平方的lambda表达式作为参数:
t = map(lambda x:x * x,range(8))
result = [e for e in t]
print(result)

y = map(lambda x:x * x if x % 2 ==0 else 0,range(8))  #当平方为偶数时输出，不为偶数时输出0
result = [e for e in y]
print(result)