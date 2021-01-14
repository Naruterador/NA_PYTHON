#coding = utf - 8


'''
在fk_package包中的__init__.py文件为空的情况下，我们使用import fk_package这句话将毫无作用。
在__init__.py为空的情况下导入模块:


#fk_package包，实际上就是导入包下的__init__.py文件
import fk_package
#导入fk_package包下的print_shape模块
import fk_package.print_shape
#导入fk_package包下的billing模块
from fk_package import billing
#导入fk_package包下的arithmetic_chart模块
import fk_package.arithmetic_chart



fk_package.print_shape.print_blank_triangle(5)
im = billing.Item(4.5)
print(im)
fk_package.arithmetic_chart.print_multiple_chart(5)


上面的程序虽然可以正常运行，但是存在两个问题:
1.为了调用包内模块中的程序单元，需要使用很长的前缀，太麻烦了
2.包内__init__.py文件的功能完全被忽略了

由于__init__.py文件用于导入该包内模块的成员，我们只要将模块中的成员都变成包内成员，以后使用起来会更加方便。
下面我们修改以下__init__.py文件
'''
