#输入p
p = 0
while p <= 0:
     p = input("Enter p:")
     p = int(p)
#输入q
q = 0
while q <= 0:
     q = input("Enter q:")
     q = int(q)
#输入n
n = 0
while n <= 0:
     n = input("Enter n:")
     n = int(n)

s = str(p//q)
r = p % q
if r != 0:
     s = s + "."
i = 0

while r != 0 and i < n:
     r = 10 * r
     s = s + str(r // q)
     r = r % q
     i = i + 1

print("%d/%d=%f" % (p,q,p / q))
print("%d/%d=%s" %(p,q,s))


