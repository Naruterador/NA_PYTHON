#coding = utf - 8

'''
遍历当前目录以及子目录下的所有文件
'''

import os

def Traversefile(path = '/opt/mechanic/githubcode/'):
	dirs = os.listdir(path)

	for i in dirs:
		#显示目录或文件的完整名称，用于isdir判断
		fullname = os.path.join(path,i)
		#isdir用于判断路经是否是目录
		if os.path.isdir(fullname):
			#使用递归函数遍历子目录
			Traversefile(fullname)
		else:
			print(fullname)



t = Traversefile()

print(t)