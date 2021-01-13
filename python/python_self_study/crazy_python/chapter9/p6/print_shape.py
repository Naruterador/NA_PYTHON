#coding = utf - 8


#这个程序编写一个python模块文件，并将该文件复制在/usr/lib/python3/dist-packages下

'''
简单的模块，该模块包含以下内容
my_list:保存列表的变量
print_triangle:打印由星号组成的三角函数

以上的注释如果要以__doc__的方式打印，必须进入python解释器才可以，不是使用python解释器，必须要定义__doc__属性。
'''

my_list = ['Python','Kotlin','Swift']
def print_triangle(n):
	'''
	打印一个由星号组成的一个三角形
	'''

	if n <= 0:
		raise ValueError('n的值必须大于0')
	for i in range(n):
		print(' ' * (n - i - 1),end = '')
		print('*' * (2 * i + 1),end = '')
		print('')

#======以下是测试代码======
def test_print_triangle():
	print_triangle(3)
	print_triangle(4)
	print_triangle(7)

if __name__ == '__main__':
	test_print_triangle()


'''
上面我们定义了一个print_triangle()函数，把该模块文件拷贝/usr/lib/python3/dist-packages
就相当于为Python扩展了一个print_shape模块，这样任何python程序都能使用这个模块。

下面可直接在python交互式解释其中测试该模块。python交互式解释器中输入如下命令:
>>> import print_shape
>>> print(print_shape.__doc__)

简单的模块，该模块包含以下内容
my_list:保存列表的变量
print_triangle:打印由星号组成的三角函数

>>> print_shape.print_triangle.__doc__
'打印一个由星号组成的一个三角形'


上面第一行代码用于导入print_shape模块；第一行代码用于查看print_shape模块的文档
，交互式解释器输出了该模块开始定义的文档内容；第三行代码用于查看print_shape模块下
print_triangle函数的文档。

接下来在交互式解释器中测试my_list变量和print_triangle()函数。在交互式解释器中输入如下命令:
>>> print_shape.my_list[1]
'Kotlin'

>>> print_shape.print_triangle(4)
   *
  ***
 *****
*******

'''