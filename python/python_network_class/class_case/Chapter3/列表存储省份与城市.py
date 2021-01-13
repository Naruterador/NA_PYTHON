'''
1、案例描述
使用列表provinces存储部分省份名称，再使用另外一个列表cities存储对应的省份的城市，实现省份与城市的查找。

2、案例分析
provinces与cities设计如下：
provinces=["广东","四川","贵州"]
cities=[["广州","深圳","惠州","珠海"],["成都","内江","乐山"],["贵阳","六盘水","遵义"]]
这样一个序号index下provinces[index]为省份，而cities[index]是这个省份的城市，也是一个列表。
'''
#(1) 输入省份查找城市
provinces = ["广东","四川","贵州"]
cities = [["广州","深圳","惠州","珠海"],["成都","内江","乐山"],["贵阳","六盘水","遵义"]]
p = input("输入省份:")
found = False 
for i in range(len(provinces)):
    if provinces[i] == p:
        print(provinces[i],end = ":")
        for j in range(len(cities[i])):
            print(cities[i][j],end = " ")
        found = True
        break

if not found:
    print("没有这个省份")
#程序中cities是一个二维的列表，即cities是一个列表，它的每个元素也是一个列表。


#(2) 输入城市查找省份
provinces = ["广东","四川","贵州"]
cities = [["广州","深圳","惠州","珠海"],["成都","内江","乐山"],["贵阳","六盘水","遵义"]]

def search(c):
    for i in range(len(cities)):
        for x in cities[i]:
            if x == c:
                print(c,"在",provinces[i] + "省")
                return
    print("没有查到")


c = input("输入城市:")
search(c)

