def test():
    f = open("test.txt", "wt+")
    f.write("我abc")
    f.seek(3, 0)
    f.write("xyz")
    #f.seek(1, 0)
    #s = f.read()
    #print(s)
    f.close()

test()
