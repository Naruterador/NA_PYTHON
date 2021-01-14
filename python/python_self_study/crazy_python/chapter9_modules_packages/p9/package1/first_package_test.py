#coding = utf - 8


'''
测试包
下面通过如下程序来使用该包
'''

#导入first_package包(模块)
import first_package

print('========================')
print(first_package.__doc__)
print(type(first_package))
print(first_package)#coding = utf - 8

'''
导入包的本质就是加载并执行该包下所有的__init__.py文件，然后将整个文件内容赋值给与包同名的变量
该变量的类型是module

与模块类似，包被导入之后也会在目录下生成一个__pycache__文件夹，并在该文件夹内为包生成一个__init__.cpython-36.pyc文件

'''
