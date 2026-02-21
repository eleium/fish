"""关于列表的方法的合集？

Python学习管家

思考过程

## Python 列表方法完整合集
### 一、增加元素
方法      语法                               说明                     示例
append()  list.append(x)                     末尾添加一个元素         [1,2].append(3) → [1,2,3]
extend()  list.extend(iterable(可迭代))      末尾添加多个元素         [1,2].extend([3,4]) → [1,2,3,4]
insert()  list.insert(i, x)                  在下标i处插入元素        [1,3].insert(1,2) → [1,2,3]

### 二、删除元素
方法       语法                说明                               示例
remove()   list.remove(x)      删除第一个匹配的元素                [1,2,1].remove(1) → [2,1]
pop()      list.pop(i)         删除并返回下标i的元素（默认最后）    [1,2,3].pop() → 返回3
clear()    list.clear()        清空列表                            [1,2,3].clear() → []
del del    list[i:j]           删除切片范围的元素                  del list[1:3]

### 三、查找与统计
方法                  语法                  说明                      示例
index()              list.index(x)         返回元素第一次出现的下标     [1,2,3].index(2) → 1
count()             list.count(x)          统计元素出现次数            [1,2,1].count(1) → 2
in                x in list               判断元素是否存在            2 in [1,2,3] → True

### 四、排序与反转
方法                  语法                  说明                      示例
sort()              list.sort()             原地排序（升序）        [3,1,2].sort() → [1,2,3]
sort(reverse=True) list.sort(reverse=True) 原地排序（降序）     [1,2,3].sort(reverse=True) → [3,2,1]
reverse()           list.reverse()          原地反转                [1,2,3].reverse() → [3,2,1]


### 五、复制
方法              语法               说明                      示例
copy()            list.copy()       返回列表的浅拷贝            b = a.copy()
切片              list[:]            返回列表的浅拷贝           b = a[:]

### 六、切片操作（增删改）
操作              语法                                 说明
增加              list[n:n] = [x]                     在下标n处插入
删除              list[n:m] = []                     删除下标n到m-1
修改              list[n:m] = [x]                     替换下标n到m-1


### 七、内置函数（不是方法，但常用）
函数                     语法                说明                  示例
len()                   len(list)           列表长度               len([1,2,3]) → 3
max()                   max(list)           最大值                 max([1,2,3]) → 3
min()                   min(list)           最小值                 min([1,2,3]) → 1
sum()                   sum(list)           求和                   sum([1,2,3]) → 6
sorted()                sorted(list)        返回新排序列表          sorted([3,1,2]) → [1,2,3]

### 八、方法对比速记
```
增：append(1个)/extend(多个)/insert(指定位置)
删：remove(按值)/pop(按位置)/clear(全删)
查：index(找位置)/count(数次数)/in(是否存在)
排：sort(排序)/reverse(反转)
拷：copy()/切片[:]
```
"""
