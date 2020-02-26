#python排序函数

1.排序函数sort()
sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。

list.sort( key=None, reverse=False)

参数
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
返回值
该方法没有返回值，但是会对列表的对象进行排序。

实例1:
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
 aList.sort()
print ( "List : ", aList)

以上实例输出结果如下：
List :  ['Facebook', 'Google', 'Runoob', 'Taobao']


实例2:
vowels = ['e', 'a', 'u', 'o', 'i']
 
vowels.sort(reverse=True)
 
print ( '降序输出:', vowels )
以上实例输出结果如下：

降序输出: ['u', 'o', 'i', 'e', 'a']

实例3:

def takeSecond(elem):
    return elem[1]
 
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=takeSecond)
print ('排序列表：', random)


以上实例输出结果如下：
排序列表：[(4, 1), (2, 2), (1, 3), (3, 4)]