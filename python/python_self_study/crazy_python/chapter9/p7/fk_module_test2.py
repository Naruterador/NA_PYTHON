#coding = utf - 8

'''
使用from...import语句来执行导入
'''

from fk_module import name,hello

print("======================")
print(name)
print(hello)
#打印fk_module
print(fk_module)

'''
程序输出结果为:
this is fk_module
======================
fkit
<function hello at 0x7f100956a2f0>
Traceback (most recent call last):
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter9/p7/fk_module_test2.py", line 13, in <module>
    print(fk_module)
NameError: name 'fk_module' is not defined



从上面的输出结果可以看出，即使使用了from...import只导入模块中部分成员，该模块中的输出语句也会在import时自动执行。
这说明python依然会加载并执行模块中的代码。

使用"from fk_module import name,hello"的本质就是:将fk_module.py中的全部代码加载到内存中去并执行，然后
只导入指定变量、函数等成员单元，并不会将整个模块导入，因此上面的程序在输出fk_module时将看到错误提示:name 'fk_module' is not defined

在导入模块之后，可以在模块文件所在的目录下看到一个名为"__pycache__"的文件夹，打开该文件夹，可以看到python为每一个模块都
生成了一个*.cpython-36.pyc文件，比如python为fk_module模块生成一个fk_module.cpython-36.pyc文件，该文件其实是python
为模块编译生成的字节码，用于提升模块的运行效率。
'''