#coding = utf - 8

'''
自定义一个生成器，可以依次访问当前目录下的所有Python源文件(以.py后缀结尾的文件)
'''

#调用os模块
import os

def listfile(path = './'):

	#调用listdir方法遍历path目录,其中dirs变量的类型为列表
	dirs = os.listdir(path)


	for i in dirs:
		#找到文件名中点的位置
		n = i.find('.')
		#判断点后面的值是否'py'
		if i[n+1:] == 'py':
			yield i

l = listfile()

print(next(l))
print(next(l))
print(next(l))