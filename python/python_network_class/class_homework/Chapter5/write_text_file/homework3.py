
def save():
    f = open("test.txt", "wt", encoding="utf-8")
    f.write("我abc\nxyz")
    f.close()


def read():
    content = 0
    f = open("test.txt", "rb")
    for i in f.read():
        content += 1
    print(content)
    f.close()


save()
read()
