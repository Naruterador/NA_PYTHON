#coding = utf-8
'''
Python不同于C/C++，程序执行并不需要主程序，如main()，而是文件自上而下的执行。
但很多Python程序中都有
if __name__ == '__main__':
     statements

这样的语句。
------------------------------------------------------------------------

这段代码的主要作用主要是让该python文件既可以独立运行，也可以当做模块导入到其他文件。
当导入到其他的脚本文件的时候，此时__name__的名字其实是导入模块的
名字，不是’__main__’, main代码里面的就不执行了。
比如写一个程序test_main.py：

def fun():
    print 'This is function'
if __name__ == '__main__':
    fun()
    print 'This is main'
　　

执行这个程序，得到结果：
This is function
This is man


此结果为test_main.py顺序执行的结果，然后将test_main作为模块引入
import test_main

得到结果：
test.main.fun()
This is function


可以发现，’__main__’模块中的代码并未执行。
'''