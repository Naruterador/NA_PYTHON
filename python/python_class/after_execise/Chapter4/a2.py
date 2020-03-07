#比较字符串是否对称,例如aaa就是对称的，abc就是不对称的




def reversestring(strings):
    newstrings = strings[::-1]
    return newstrings


def issymmetry(string1):
    if reversestring(string1) == string1:
        return True
    return False

if issymmetry('abc'):
    print('YES')
else:
    print('NO')