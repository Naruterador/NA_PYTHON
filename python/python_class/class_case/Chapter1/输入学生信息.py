

'''
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
'''


try:
    Name = input("姓名:")
    if Name.strip() == "":
        raise Exception("无效的姓名")
    Gender = input("性别:")
    if Gender != "男" and Gender != "女":
        raise Exception("无效的性别")
    Age = input("年龄:")
    Age = float(Age)
    if Age < 18 or Age > 30:
        raise Exception("无效的年龄")
    print(Name,Gender,Age)
except Exception as err:
    print(err)
