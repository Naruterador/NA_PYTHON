#coding = utf - 8 

'''
查看模块包含，可以通过如下方式
1.dir()函数
2.使用模块本身提供的__all__变量

比如我们可以在解释器中导入string模块，但后使用dir()函数来查看输出结果:

>>> import string
>>> dir(string)
['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', 
'__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
'_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 
'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']

通过以上的输出我们发现，该模块内由很画线开头的程序单元，其实这些程序单元并不希望被其他程序使用，因此这里
列出的意义不大。

我们可以用以下的语句来过滤这些单元:
>>> [e for e in dir(string) if not e.startswith('_')]
['Formatter', 'Template', 'ascii_letters', 'ascii_lowercase', 
'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']

------------------------------------------------------------------------------------------------------------

此外我们还可以通过__all__变量来查看模块内的程序单元:

>>> string.__all__
['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 
'octdigits', 'printable', 'punctuation', 'whitespace', 'Formatter', 'Template']

并不是所有模块都会提供__all__变量的，有些模块并不提供__all__变量，在这种情况下，只能使用列表推导式
来查看模块中的程序单元。

'''