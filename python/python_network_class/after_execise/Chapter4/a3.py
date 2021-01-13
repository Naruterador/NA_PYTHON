'''
寻找字符串子串，返回对应的第一个子串的索引位置
编写myFind(s,t)实现s.find(t)
如果找不到子串则返回-1
'''

s = 'abcabc'
t = 'abc'

def myFind(s,t):
    index_s = 0
    index_t = 0
    index_temp = 0
    positionlist = []
    while index_s < len(s):
        while index_t < len(t):
            if index_s >= len(s):
                break

            if s[index_s] == t[index_t]:
                index_s = index_s + 1
                index_t = index_t + 1
                index_temp = index_temp + 1
    
                #取出头索引
                if index_t > len(t) - 1:
                    positionlist.append(index_s - index_temp)
                    index_s -= 1
            else:
                index_s = index_s - index_temp
                break   
      
        index_s = index_s + 1
        index_t = 0
        index_temp = 0

    return positionlist


print(myFind(s,t))
