#coding = utf - 8


'''
使用__doc__属性来查看文档

我们可以使用help()函数来查看程序单元的帮助信息。比如导入了string模块之后，就可以使用
help()函数来查看指定程序单元的帮助信息。

在交互模式下使用help()函数查看string模块下的capwords()函数的作用


>>> import string
>>> help(string.capwords)

Help on function capwords in module string:

capwords(s, sep=None)
    capwords(s [,sep]) -> string
    
    Split the argument into words using split, capitalize each
    word using capitalize, and join the capitalized words using
    join.  If the optional second argument sep is absent or None,
    runs of whitespace characters are replaced by a single space
    and leading and trailing whitespace are removed, otherwise
    sep is used to split and join the words.


需要说明的是，使用help函数之所以能查看到程序单元的帮助信息，其实完全是因为该程序
单元本身具有文档信息，也就是定义了__doc__属性。


'''