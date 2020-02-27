'''
1、案例描述
编写myFind(s,t)实现s.find(t)

2、案例分析
设置s为字符串变量，在s中查找是否包含子字符串t是一个常用的操作。例如s="I am testing", t="am"， 那么s包含t，如果t="test"，s也包含t，但是t="tested"时s不包含t。我们设计函数index(s,t)测试s是否包含t，如果包含就返回t在s的开始下标位置，不然返回-1。
查找的方法是从s[i]开始，把t与s[i]对齐，查看s[i]与t[0], s[i+1]与t[1]，.......,s[i+len(t)-1]与t[len(t)-1]是否相同，如果都相同那么说明s包含t，不然就更换一个i再次比较。
'''


def myFind(s,t):
  m = len(s)
  n = len(t)

  if m < n:
    return -1

  i = 0
  while i <= m - n:
    j = 0
    while j < n:
      if s[i + j] != t[j]:
        break
      j = j + 1
    if j == n:
      return i
    i = i + 1
    
  return -1

s="ababcabcd12ab"
print(myFind(s,"abc"),s.find("abc"))
print(myFind(s,"ad"),s.find("ad"))

