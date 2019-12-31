#coding = utf - 8

'''
此外，sys.stdin也是一个类文件对象(类似于文件的对象，Python的很多I/O流都是
类文件对象)，因此，程序同样可以使用for循环遍历sys.stdin,这意味着程序可以
通过for循环来获取用户的键盘输入。
'''


#实际代码如下
import sys
#使用for循环遍历标准输入
for line in sys.stdin:
    print('用户输入:',line,end='')


'''
上面粗体字代码使用for循环遍历sys.stdin,这意味着程序可以通过for循环来读取用户的
键盘输入————用户每输入一行，程序就会输出用户输入这行。
'''

