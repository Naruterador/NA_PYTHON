#coding = utf - 8

#导入all_module模块中所有的成员
from all_module import *

hello()
world()
test() #会提示找不到test()函数


'''
由于该模块包含了__all__变量，因此该语句只导入了__all__变量所列出的程序单元。
代码输出结果为:
Hello,Python
python world is funny
Traceback (most recent call last):
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter9/p8/all_module_test.py", line 8, in <module>
    test() #会提示找不到test()函数
NameError: name 'test' is not defined

#---------------------------------------------------------------------------------------------------------------------------




事实上，__all__变量的意义在于为模块定义一个开放的公共接口。通常来说，只有__all__变量列出的程序单元，才是
希望该模块被外界使用的程序单元。因此，为模块设置__all__变量还是比较有用的。

如果确实希望程序使用模块内__all__列表之外的程序单元，有两种解决方法：
第一种是使用"import 模块名"来导入模块。在通过这种方式导入模块之后，总可以通过模块名前缀来
调用模块内的成员。
第二种是使用"from 模块名 import 程序单元"来导入指定程序单元。在这种方式下，即使想导入的程序单元没有
位于__all__列表中，也依然可以导入。
'''
