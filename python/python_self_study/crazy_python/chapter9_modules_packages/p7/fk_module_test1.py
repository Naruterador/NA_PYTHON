#coding = utf - 8 


'''
接下来，在相同的路经下定义如下程序来使用fk_module模块
'''

import fk_module

print("=====================")
#打印module的类型
print(type(fk_module))
print(fk_module)

'''
输出结果如下:
this is fk_module
=====================
<class 'module'>
<module 'fk_module' from '/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter9/p7/fk_module.py'>

从上面的输出结果来看，当程序导入fk_module时，该模块中的输出语句会在import时自动执行。该模块还包含了一个
与模块同名的变量，该变量的类型为module

使用"import fk_module"导入模块的本质就是:将fk_module.py中的全部代码加载到内存并执行，然后将整个模块内容赋值给与模块
同名的变量，该变量的类型是module,而在该模块中定义的所有程序单元都相当于该module对象的成员。

'''