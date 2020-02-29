#coding=utf-8
'''
python中有三个工具函数用来获取指定范围内的“变量字典”
1.globals(): 该函数返回全局范围内所有变量组成的“变量字典”
2.locals(): 该函数返回当前局部范围内所有变量组成的“变量字典”
3.vars(object) 获取在指定对象范围内所有变量组成的“变量字典” 如果不传入object参数，vars()和locals()的作用完全相同
'''


def test():
	age = 20
	print(age)
	print(locals())
	print(locals()['age'])
	locals()['age'] = 12  #修改局部变量的值
	print('xxx',age)      #var(object)这种形式
	print(globals())
	globals()['x'] = 19   #修改全局变量的值

x = 5
y = 20

#test()



#print(globals())
print(locals())
#print(globals()['x'])