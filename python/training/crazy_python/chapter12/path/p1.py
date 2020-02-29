#coding = utf - 8


#下面程序示范了Path的简单用法
from pathlib import *

#获取当前目录
#p = Path('.')
#遍历当前目录下的所有文件和子目录
#for x in p.iterdir():    #1代码处
#	print(x)

#获取上一级目录
p = Path('../')
#获取上级目录及其所有子目录下的.py文件
for x in p.glob('**/*.py'):  #2代码处
	print(x)

#获取g:/publish/codes对应的目录
#p = Path('../')
#获取上级目录及其所有子目录下的.py文件
#for x in p.glob('**/*.py'):  #3代码
#	print(x)


'''
上面程序中第#1代码调用了Path的iterdir()方法，该方法将会返回当前目录下所有文件和子目录
#2代码调用了glob()用法、获取上一级目录及其所有子目录下的*.py文件
#3代码用于获取g:/publish/codes目录及其所有子目录下的Path_test1.py文件

输出结果为:
#1代码输出
conception.md
p2.py
p1.py

#2代码输出
../path/p2.py
../path/p1.py
../pathlib/p2.py
../pathlib/p1.py
../pathlib/p3.py

#3代码输出
../path/p2.py
../path/p1.py
../pathlib/p2.py
../pathlib/p1.py
../pathlib/p3.py

从上面的输出结果来看，不管是遍历当前目录下的文件和子目录，还是搜索指定目录及其子目录
Path对象都能用一个方法搞定----对于不少语言来说，Path的glob()方法所能实现的功能
其他语言往往要通过递归才能实现，这可能就是Python的魅力所在
'''
