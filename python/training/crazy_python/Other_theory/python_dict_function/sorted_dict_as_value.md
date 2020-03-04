#根据字典值对字典进行排序
> 方法1:<br>
    > dic1SortList = sorted( dic1.items(),key = lambda x:x[1],reverse = True)<br>
      备注:reverse = True 指定为降序排序


> 方法2:<br>
    > import operator<br>
      sorted_x = sorted(d.items(),key = operator.itemgetter(1))
    
    > operator.itemgetter说明:
      operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号）
      
      示例:
      a = [1,2,3] 
      >>> b = operator.itemgetter(1)      //定义函数b，获取对象的第1个域的值
      >>> b(a) 
      2 


