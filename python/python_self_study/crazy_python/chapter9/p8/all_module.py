#coding = utf - 8

'''
模块的__all__变量

在默认情况下，如果使用"from 模块名 import *"这样的语句来导入模块，程序会导入
该模块中所有不以下划线开头程序单元。

有时候模组中虽然包含很多成员，但并不希望每个成员都被暴露出来供外界使用，此时
与模块__all__变量，将变量的值设置成为一个列表，只有该列表中的程序单元才会暴露出来。

下面程序定义了一个包含__all__变量的模块
'''

def hello():
	print("Hello,Python")

def world():
	print("python world is funny")

def test():
	print('--test--')

#定义__all__变量，默认只导入hello和world两个程序单元
__all__ = ['hello','world']


'''
__all__变量指定该模块默认只被导入hello和world两个程序单元。
'''