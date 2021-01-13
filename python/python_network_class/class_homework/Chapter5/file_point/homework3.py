#在test.txt文件不存在时会自动创建test.txt

f = open("test.txt", "wt")
f.write("abc")
f.close()

