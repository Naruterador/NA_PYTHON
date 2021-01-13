
'''
题目：两个兵乓球队进行比赛，各出三人。甲队为a,b,c三人，乙对为x,y,z三人。
以抽签决定比赛名单。有向队员打听比赛的名单。a说他不和x比，c说他不和x，z比，请编程找到三队赛手的名单。

思路：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
'''


for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print( 'order is a -- %s\t b -- %s\tc -- %s' % (chr(i),chr(j),chr(k)))
