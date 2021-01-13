'''
1、案例描述
设计一个程序存储省份与其所辖城市的信息，实现查询功能。
 
2、案例分析
设计字典provinces如下：
provinces={"广东":["广州","深圳"],"四川":["成都", "内江", "乐山"]}
字典provinces的keys是各个省的名称，一个省的值时一个列表，是它下辖的各个城市。
'''
#provinces是全局的变量
provinces={}

def append(province,cities):
    global provinces
    if province not in provinces.keys():
        provinces[province] = cities
    else:
        print(province+"已经存在")

def show():
    for p in provinces.keys():
        print(p,provinces[p])

def seekProvince(province):
    if province in provinces.keys():
        print(province,end = ":")
        for c in provinces[province]:
            print(c,end = " ")
        print()
    else:
        print("没有这个省份")

def seekCity(city):
    for p in provinces.keys():
        if city in provinces[p]:
            print(city + "属于" + p + "省")
            return
    print("没有这个城市")

append("广东",["广州","深圳"])
append("四川",["成都", "内江", "乐山"])
append("贵州",["贵阳","六盘水","兴义"])
#show()
seekProvince("四川")
seekCity("六盘水")

