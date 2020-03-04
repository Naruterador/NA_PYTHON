#编写一个程序，它能统计一篇英文文章中的a~z各个字母出现的次数（不分大小写），并按出现次数的多少按顺序输出。

import codecs
import operator
amountcount = []
s = ''
a = 0
b = 0
c = 0
d = 0
e = 0
f1 = 0 
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0 
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t1 = 0
u = 0
v = 0
w = 0 
x = 0
y = 0
z = 0

with codecs.open("a7text.txt","r+",encoding = "utf - 8") as f:
    while True:
        t = f.read(1)
        if 'a' == t or 'A' == t:
            a += 1
        if 'b' == t or 'B' == t:
            b += 1
        if 'c' == t or 'C' == t:
            c += 1
        if 'd' == t or 'D' == t:
            d += 1
        if 'e' == t or 'E' == t:
            e += 1
        if 'f' == t or 'F' == t:
            f1 += 1
        if 'g' == t or 'G' == t:
            g += 1
        if 'h' == t or 'H' == t:
            h += 1
        if 'i' == t or 'I' == t:
            i += 1
        if 'j' == t or 'J' == t:
            j += 1
        if 'k' == t or 'K' == t:
            k += 1
        if 'l' == t or 'L' == t:
            l += 1
        if 'm' == t or 'M' == t:
            m += 1
        if 'n' == t or 'N' == t:
            n += 1
        if 'o' == t or 'O' == t:
            o += 1
        if 'p' == t or 'P' == t:
            p += 1
        if 'q' == t or 'Q' == t:
            q += 1
        if 'r' == t or 'R' == t:
            r += 1
        if 's' == t or 'S' == t:
            s += 1
        if 't' == t or 'T' == t:
            t1 += 1
        if 'u' == t or 'U' == t:
            u += 1         
        if 'v' == t or 'V' == t:
            v += 1
        if 'w' == t or 'W' == t:
            w += 1
        if 'x' == t or 'X' == t:
            x += 1
        if 'y' == t or 'Y' == t:
            y += 1
        if 'z' == t or 'Z' == t:
            z += 1
        if not t:
            break
amountcount.append(a)
amountcount.append(b)
amountcount.append(c)
amountcount.append(d)
amountcount.append(e)
amountcount.append(f1)
amountcount.append(g)
amountcount.append(h)
amountcount.append(i)
amountcount.append(j)
amountcount.append(k)
amountcount.append(l)
amountcount.append(m)
amountcount.append(n)
amountcount.append(o)
amountcount.append(p)
amountcount.append(q)
amountcount.append(r)
amountcount.append(s)
amountcount.append(t1)
amountcount.append(u)
amountcount.append(v)
amountcount.append(w)
amountcount.append(x)
amountcount.append(y)
amountcount.append(z)


dict1 = {}
dict2 = {}
j = 0
for i in range(97,123):
    dict1[chr(i)] = amountcount[j]
    dict2.update(dict1)
    j += 1

sorted_dict = sorted(dict2.items(),key=operator.itemgetter(1),reverse=True)

print(sorted_dict)