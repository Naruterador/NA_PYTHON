#coding = utf - 8



#程序也可以使用with语句来处理通过fileinput.input合并的多个文件

import fileinput
#使用with语句打开文件，该语句会负责关闭文件
with fileinput.input(files=('test.txt','info.txt')) as f:
    for line in f:
        print(line,end='')






#with_test1.py和with_test2.py这2个程序都使用了with来管理资源，因此它们都不需要显示
#关闭文件。
