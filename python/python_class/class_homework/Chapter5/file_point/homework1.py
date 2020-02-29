def save():
    f = open("test.txt", "wt")
    f.write("abc\nxyz")
    f.close()


def read():
    f = open("test.txt", "rb")
    s = f.read()
    for x in s:
        print(hex(x), end=" ")
    f.close()


save()
read()

