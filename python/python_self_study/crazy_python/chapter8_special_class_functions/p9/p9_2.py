#coding = utf - 8

'''
程序使用iter()函数将列表、元祖等转换成迭代器
'''

#将列表转换为迭代器
my_iter = iter([2,'fkit',4])

#依次获取迭代器的下一个元素
print(my_iter.__next__())
print(my_iter.__next__())