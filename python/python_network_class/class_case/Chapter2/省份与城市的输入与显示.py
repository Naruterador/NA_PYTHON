'''
用一个函数输入省份与城市，用另外一个函数显示。
'''


province = ""
city = ""


def enter():
    global province
    global city
    province = input("省份:")
    city = input("城市:")

def show():
	print("省份:" + province + "    " + "城市:" + city)



enter()
show()
