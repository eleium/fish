#列表的方法有： 增/删/改/查

a=['abd',1,2,3]

print(a)
a.append(88)#列表名.append（x）:在列表的默认后面增加一个元素。
a.append('你好')

print(a)
a.remove(1)

a.remove('abd')
print(a)

print('*'*88)


"""
append和remove都只能有一个参数？如何一次增加或删除多个元素呢？
用extend添加 可迭代的对象,一定是可迭代的对象：[]
"""

mylist=[1,3,5]
mylist.extend(['abc','yellow',888])#列表可迭代
print(mylist)
# mylist.extend(55)#整数不可迭代，会报错。换成
mylist.extend('abc')
mylist.extend('888')#888为字符串，可以迭代。
print(mylist)

print(mylist)
mylist.extend('hello')

#字符串是不可变的，而列表是可变的。

#还可以用切片的方法改变列表,这种方法是替换而不是添加。
mylist[1:4]=['a','b','c']
print(mylist)

mylist[1:1]=[99,999,9999]#[1:1]这才是在第2下边开始增加。
print(mylist)

mylist[3:1]=[000,00,0000]
print(mylist)

#mylist[n:n]=[新列表]这这方法是在指定的下标处增加新列表内容。

s=[1,2,3,4,5]

s[len(s):]=[78]#相当与 s.append(78)

s[len(s):]=[6,7,8,9]#相当于 s.extend([6,7,8,9])
print(s)

a=[1,2,3,4,5,6]
a.extend({7,8,9})#extend的可迭代对象是集合，乱序？
print(a)

#元组()，列表[],集合{}，字典{key:value}都可以用extend增加，其中set{}是无序的唯一的，dict{}只增加key。

s=[1,3,4,5,6]
s.insert(1,2)#insert(下标，元素）
print(s)
s.insert(len(s),00)#在python中，00就是0.
print(s)

#s.pop(下标)，直接删除指定下标的元素。
s.pop(3)
print(s)#没有4了。

s.clear()#一次性清空列表。
print(s)

"""

原因：00 就是 0
在 Python 中， 00 和 0 是 完全相同 的整数：

```
print(00输出:0
print(0)输出:0
print(00==0)输出:True
```
为什么？
- 整数的前导零在 Python 中 没有意义
- 00 、 000 、 0 都表示同一个数值：零
- Python 会自动忽略整数前面的零
"""

# ==================== 列表方法合集 ====================

# 一、增加元素
# append(x)      - 末尾添加一个元素
# extend(iter)   - 末尾添加多个元素（可迭代对象）
# insert(i, x)   - 在下标i处插入元素

# 二、删除元素
# remove(x)      - 删除第一个匹配的元素（按值删）
# pop(i)         - 删除并返回下标i的元素（按位置删，默认最后）
# clear()        - 清空列表

# 三、查找与统计
# index(x)       - 返回元素第一次出现的下标
# count(x)       - 统计元素出现次数
# x in list      - 判断元素是否存在（返回True/False）

# 四、排序与反转
# sort()                - 原地升序排序
# sort(reverse=True)    - 原地降序排序
# reverse()             - 原地反转

# 五、复制
# copy()         - 返回列表的浅拷贝
# list[:]        - 切片复制

# 六、切片操作（增删改）
# list[n:n] = [x]    - 在下标n处插入
# list[n:m] = []     - 删除下标n到m-1
# list[n:m] = [x]    - 替换下标n到m-1

# 七、内置函数
# len(list)      - 列表长度
# max(list)      - 最大值
# min(list)      - 最小值
# sum(list)      - 求和
# sorted(list)   - 返回新排序列表（不修改原列表）

# 速记口诀：
# 增：append(1个) / extend(多个) / insert(指定位置)
# 删：remove(按值) / pop(按位置) / clear(全删)
# 查：index(找位置) / count(数次数) / in(是否存在)
# 排：sort(排序) / reverse(反转)
# 拷：copy() / 切片[:]


