#文件test.txt不存在时会自动创建test.txt
f = open("test.txt", "rb+")
f.write("abc")
f.close()

