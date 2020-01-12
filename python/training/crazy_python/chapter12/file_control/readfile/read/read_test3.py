#coding = utf - 8



'''
如果在调用read()方法时不传入参数，该方法默认会读取全部文件内容。
'''
#实例代码如下:

f = open("test.txt",'r',True)
#直接将文件内容全部读取出来
print(f.read())
f.close()
