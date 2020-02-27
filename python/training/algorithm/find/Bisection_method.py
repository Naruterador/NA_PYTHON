#Bisection_method(二分法查询)



'''
在用二分法进行查找时，查找对象的数组必须是有序的，即各数组元素的次序是按其值的大小顺序存储的。
其基本思想是先确定待查数据的范围（可用 [left,right] 区间表示），然后逐步缩小范围直到找到或找不到该记录为止。

具体做法是：先取数组中间位置（mid=(left+right)/2）的数据元素与给定值比较。若相等，则查找成功；
否则，若给定值比该数据元素的值小（或大），则给定值必在数组的前半部分[left,mid-1]（或后半部分[mid+1,right]），然后在新的查找范围内进行同样的查找。
如此反复进行，直到找到数组元素值与给定值相等的元素或确定数组中没有待查找的数据为止。因此，二分查找每查找一次，或成功，或使查找数组中元素的个数减少一半，当查找数组中不再有数据元素时，查找失败。

二分法查找是一种非常高效的搜索方法，主要原理是每次搜索可以抛弃一半的值来缩小范围。其时间复杂度是O(log2n)，一般用于对普通搜索方法的优化。
二分法的适用情况一般满足以下几点：（1）该数组数据量巨大，需要对处理的时间复杂度进行优化；（2）该数组已经排序；（3）一般要求找到的是某一个值或一个位置。
'''
alist = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
#[1, 5, 7, 8, 22, 54, 99, 123, 222, 300]


def Bisection_method(list,value):
    sortlist = sorted(list)
    
    low_index  = 0
    high_index = len(sortlist) - 1
    mid_index = (low_index + high_index) // 2


    while low_index <= high_index:
        if sortlist[mid_index] == value:
            return mid_index
    
        if sortlist[mid_index] < value:
            low_index = mid_index + 1
            mid_index = (low_index + high_index) // 2

        if sortlist[mid_index] > value:
            high_index = mid_index - 1
            mid_index = (low_index + high_index) // 2
        

print(Bisection_method(alist,123))