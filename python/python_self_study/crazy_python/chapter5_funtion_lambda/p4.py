#coding=utf-8

name = 'Charlie'

def test():
	print(name)
	globals()['name'] = 'Rich'    #通过全局字典修改变量名称

test()

print(name)