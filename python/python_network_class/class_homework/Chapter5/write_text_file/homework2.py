def save():
    f = open("test.txt", "wt")
    f.write("abc\nxyz")
    f.close()


def read():
    f = open("test.txt", "rt")
    s = f.readline()
    print(len(s))
    f.close()


save()
read()
