def save():
    f = open("test.txt", "wt", encoding="gbk")
    f.write("我abc\nxyz")
    f.close()


save()


def read():
    content = 0
    f = open("test.txt", "rb")
    for i in f.read():
        content += 1
    print(content)
    f.close()


save()
read()
