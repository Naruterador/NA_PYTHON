'''
输入一个有效的时间，并显示该时间。

设置时间格式为h:m:s，输入时保证输入且h、m、s的值有效，不然就抛出异常。
'''
def myTime():
    h = input("时:")
    h = int(h)
    if h < 0 or h > 23:
        raise Exception("无效的时")

    m = input("分:")
    m = int(m)
    if m < 0 or m > 59:
        raise Exception("无效的分")

    s = input("秒:")
    s = int(s)
    if s < 0 or s > 59:
        raise Exception("无效的秒")
    print("%02d:%02d:%02d" %(h,m,s))

try:
    myTime()
except Exception as e:
    print(e)
