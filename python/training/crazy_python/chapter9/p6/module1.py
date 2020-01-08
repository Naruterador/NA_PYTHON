#coding = utf - 8


'''
Python中的模块实际上就是python程序。任何python程序都可以作为模块导入。
对于任何程序只要导入了模块，就可以使用该模块内的所有成员。
'''

#下面程序定义了一个简单的模块
print('这是module1')
my_book = '疯狂python讲义'

def say_hi(user):
	print('%s,您好，欢迎学习python' % user)

class User(object):
	def __init__(self,name):
		self.name = name
	def walk(self):
		print('%s 正在慢慢的走路' % self.name)
	def __repr__(self):
		return 'User[name=%s]' % self.name

'''
#为模块编写说明文档，告诉开发者模块的作用以及功能
#这些字符串的内容将会作为该模块的说明文档，可通过模块__doc__属性来访问文档
这是我们编好的第一个模块，该模块包含
my_book:字符串变量
say_hi:简单的函数
User:代表用户的类
'''
#----------------------------------------------------------------------------------------

'''
为模块编写测试代码,当模块完成之后，可能还需要为模块编写一些测试代码，用于测试模块中的每一个
程序单元是否能正常运行。
'''
#===以下部分是测试代码===
def test_my_book():
	print(my_book)

def test_say_hi():
	say_hi('孙悟空')
	
def test_User():
	u = User('白骨精')
	u.walk()
	print(u)

'''
上面三个函数分别用于测试模块中的变量、函数和类，不过这三个函数并没有得到调用的机会。
因此，如果使用python命令来运行上面的模块，程序并不会运行它们。
'''


'''
如果只是简单的调用一下上面的测试程序,调用方式如下:
test_my_book()
test_say_hi()
test_User()
会导致一个问题:当其他程序每次导入该模块时，这三个测试函数都会自动运行，这显然不是我们想要的结果。
我们希望的效果是:如果直接使用python命令运行该模块时（相当于测试），程序应该执行该模块的测试函数，如果是其他
程序导入这个模块时，都不应该执行该模块的这3个测试函数


此时可借助于所有模块内置的__name__变量进行分区，如果直接使用python命令来运行一个模块
__name__的值为__main__;如果该模块被导入其他程序中，__name__变量的值就是模块名。
因此如果希望测试函数只有在使用python命令直接运行时才执行，可在调用测试函数时增加判断。
代码如下:
'''
if __name__ == '__main__':
	test_my_book()
	test_say_hi()
	test_User()


#-----------------------------------------------------------------------------------------

'''
加载模块:
为了能让python找到我们编写（或第三方提供的模块)，我们可以用以下两种方式来告诉它。
1.使用环境变量:



2.将模块放在默认的模块加载路经下:
	python默认加载路经由sys.path变量代表，因此可通过在交互式解释器中执行如下来查看
	python默认的加载路经:
	>>> import sys,pprint
	>>> pprint.pprint(sys.path)
	['',
 	 '/usr/lib/python36.zip',
 	 '/usr/lib/python3.6',
 	 '/usr/lib/python3.6/lib-dynload',
 	 '/usr/local/lib/python3.6/dist-packages',
 	 '/usr/lib/python3/dist-packages']
上面代码使用pprint模块下的pprint()函数代替普通的print()函数，pprint可以显示友好的打印结果。

上面代码显示结果是Python 3.x默认的模块加载路经，这台机器将Python安装在了/usr/lib下。

上面显示运行结果列出的路经都是Python的默认模块加载路经，但通常来说，python的扩展模块都添加在lib/python3/dist-packages下
它专门用于存放Python的扩展模块和包。


Python的强大，其中一个重要原因是Python有很丰富的库（模块）从而可以比较方便地处理各种各样的问题。
Python的第三方modules一般都安装在一些固定的路径，如下：
Unix(Linux): prefix/lib/pythonX.Y/site-packages 默认路径：/usr/local/lib/pythonX.Y/site-packages
Windows: prefix\Lib\site-packages 默认路径：C:\PythonXY\Lib\site-packages
另外，在Unix-like系统上，Python自身build-in的模块一般位于：/usr/lib/pythonX.Y/site-packages
从源代码安装模块的命令一般为：setup.py install
当然，可以根据需要改变默认的第三方模块安装路径，在命令中可以加上参数：–user, or –home, or –prefix and –exec-prefix, or –install-base and –install-platbase 等来指定安装路径。
需要注意的是：模块的安装路径一定要在 sys.path 这个List中，才能在脚本中可以正常地 import 进来。

'''









