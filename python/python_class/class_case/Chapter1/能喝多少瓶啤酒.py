'''
啤酒2元一瓶，4个啤酒瓶盖子可以免费换1瓶啤酒，2个空瓶子可以免费换1瓶啤酒，现在有10元钱，那么总共可以喝多少瓶啤酒？
'''

m = 10
beers = m // 2
caps = 0
bottles = 0
count = 0

while beers > 0:
    caps = caps + beers
    bottles = bottles + beers
    count = count + beers
    print("这次喝掉%d瓶啤酒，总计%d瓶啤酒" % (beers, count))
    beers = 0
    print("  (%d瓶啤酒, %d个盖子, %d个瓶子)" % (beers, caps, bottles))
    if caps >= 4:
        print("  %d个盖子换%d瓶啤酒" % (caps - caps % 4, caps // 4))
        beers = beers + caps // 4
        caps = caps % 4
    if bottles >= 2:
        print("  %d个瓶子换%d瓶啤酒" % (bottles - bottles % 2, bottles // 2))
        beers = beers + bottles // 2
        bottles = bottles % 2
    print("  (%d瓶啤酒, %d个盖子, %d个瓶子)" % (beers, caps, bottles))
print("总计喝掉%d瓶啤酒，剩下%d个盖子和%d个瓶子" % (count, caps, bottles))
