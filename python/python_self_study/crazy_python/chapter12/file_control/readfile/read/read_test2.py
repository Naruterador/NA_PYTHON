#coding = utf - 8


'''
如果需要更安全地关闭文件，推荐将关闭文件的close()方法调用在finally块中执行。例如，将上面程序改写为如下形式。
'''


#下面程序采用循环读取文件的内容:
f = open("test.txt",'r',True)
try:
	while True:
	    #每次读取一个字符
	    ch = f.read(1)
	    #如果没有读取到数据，则跳出循环
	    if not ch:
	        break
	    #输出ch
	    print(ch,end='')
finally:
	f.close()
