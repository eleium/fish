# 字典的 改：
d = dict.fromkeys("fishC")  # creart a dict without value.
print(d)  # --->{'f':None,'I':None,'s':None,'h':None,'C':None}
d["f"] = 100  # 给key f 赋值键值100
print(d)

# update()
d.update(ishC=230)  # 添加一个键值对，字典里原来没有该键值对。
print(d)  # -->{'f':100,'I':None,'s':None,'h':None,'C':None,'ishC':230}
# 增加了一个键值对：ishC:230

d.update({"I": 100, "s": 200})
print(d)  # -->{'f':100,'I':100,'s':200,'h':None,'C':None,'ishC':230}

d.update(C=250)  # 给单个键更改键值。
print(d)  # --->{'h':100,'I':100,'s':100,'h':None,'C':250,'ishC':200}

# 字典的 查
print(d["h"])  # -->None查找字典中的键的值。
# print(d["o"])  # 报错：当键不存在的键的时候，会报错。这时候要用get()方法：可以用default参数，
# 指定返回的值：
print(d.get("o", "不存在的键"))  # --->不存在的键

# 用setdefault()方法来查找一个键值，如果键不存在，就把它加入到字典里。
d.setdefault("o", "不存在的键")
print(d)  # --->{'f':100,'I':100,'s':100,'h':None,'C':250,'ishC':200,'o':'不存在的键'}
# 多了一个键值对：o:不存在的键。这时候可以用get().


# items() keys() values() 方法：分别获取字典的键值对、键、值。
d = dict.fromkeys("python")  # 创建一个字典
keys = d.keys()  # 获取字典的键
print(keys)
# --->dict_keys(['p','y','t','h','o','n'])
# d.keys() 方法返回的不是普通的列表（list），而是一个 dict_keys 对象，
# 这是字典的视图对象（view object）。
d.update({"p": 100, "y": 200, "t": 300, "h": 400, "o": 500, "n": 600})
values = d.values()
print(values)  # --->dict_values([100,200,300,400,500,600])得到该字典的value值.

items = d.items()
print(items)  # --->dict_items([('p',100),('y',200),('t',300),('h',400),('o',500),('n',600)])
# 以上dict_items()、dict_keys()、dict_values()方法，得到的都是视图对象。那么，视图对象是啥呢？
"""
什么是视图对象（View Object）？
视图对象是字典的动态映射，它能实时反映字典的变化。
关键特性：
1. 动态更新
2支持集合操作
视图对象可以进行集合运算（交集、并集、差集等）

当字典发生变化时，视图对象会自动更新，不需要重新调用方法。
为什么设计成视图对象？
性能优化！
不需要每次都复制整个字典的数据
节省内存
保持与字典的同步
总结
视图对象就像字典的"实时镜像"：
✅ 字典变了，视图自动变
✅ 支持迭代和集合操作
❌ 不是列表，不能修改
🔄 需要时用 list() 转换成普通列表
这样设计既高效又方便，是 Python 字典的一个很棒的特性！👍
"""
d.pop("p")  # 删除了字典中的'p'键值对。
print(d)  # --->{'y':200,'t':300,'h':400,'o':500,'n':600}

print(keys, items, values)  # 此时，并没有对字典d进行keys,items,values修改，但是他们的视图对象已经自动的发生了变化。
# --->dict_keys(['y','t','h','o','n'])
# dict_items([('y',200),('t',300),('h',400),('o',500),('n',600)])
# dict_values([200,300,400,500,600])
# 视图对象的价值在于：它能在字典变化后自动更新，而不需要重新调用方法！在后面的代码中可以直接调用了.直接就是更改后的新值。

# 与列表d也有浅拷贝功能：copy()
e = d.copy()
print(e)  # --->{'y':200,'t':300,'h':400,'o':500,'n':600}复制了字典：d。

# 用len()函数来获取字典的键值对数量：
print(len(d))  # --->5

# 用 in 和 not in 来判断某个键是否在字典中：
print("y" in d)  # --->true
print("z" not in d)  # --->True

# 用list()把字典转化为列表：
print(list(d))  # --->['y','t','h','o','n']用list()函数把字典d转为列表，由字典的key组成。等同于：list(d.keys())
print(list(d.values()))  # --->[200,300,400,500,600] 由字典的values组成。
print(list(d.items()))  # --->[('y',200),('t',300),('h',400),('o',500),('n',600)] 由字典的key-value组成。

print("-" * 80)

# 还有一个函数： iter()返回一个迭代器对象。这个迭代器只能用一遍。
print(iter(d))  # ---><dict_keyiterator object at 0x0000025EB0EA5E80>用字典的键，构成一个迭代器对象。
print(list(iter(d)))  # ---->['y','t','h','o','n']由字典的键组成的列表。
print(list(iter(d.values())))  # --->[200,300,400,500,600] 由字典的value组成的列表。
m = iter(d)  # 这个迭代器只能用一次。
print(next(m))  # --->y
print(next(m))  # --->t
print(next(m))  # --->h
print(next(m))  # --->o
print(next(m))  # --->n
# print(next(m))  # --->报错：StopIteration


# python3.8以后的版本，字典是有序的了。所以可以用reversed()的方法对字典的顺序进行反转：
print(reversed(d))  # ---> <dict_reversekeyiterator object at 0x0000025EB0EA5E80>返回的也是一个迭代器
print(list(reversed(d)))  # --->['n','o','h','t','y']字典内的键的顺序被反转了。

# 字典也可以嵌套：

f = {'吕布': {'语文': 60, '数学': 70, '英语': 80}, '关羽': {'语文': 90, '数学': 80, '英语': 90}}
print(f['吕布']['数学'])  # --->70用两次索引，取得字典中嵌套的字典的值
g = {'吕布': [60, 70, 80], '关羽': [80, 90, 100]}
print(g['吕布'][1])  # --->70用下标的方法取得吕布的数学成绩是70.

# 字典推导式：
d = {'f': 70, 'I': 105, 's': 100, 'h': 104, 'C': 120}
# 用字典推导式，把字典d 放到字典b中：
b = {v: k for k, v in d.items()}  # 把d的键值对对调后放入字典b中。
k = {k: v for k, v in d.items()}
print(b)  # --->{70:'f',105:'I',100:'s',104:'h',120:'C'}
print(k)  # --->{'f':70,'I':105,'s':100,'h':104,'C':120 }
l = {v: k for k, v in d.items() if v > 100}  # 加了条件的字典推导式
m = {k: v for k, v in d.items() if v > 100}
print(l)  # --->{105:'I',104:'h',120:'C'}
print(m)  # --->{'I':105,'h':104,'C':120}

# 求字典的key的编码值：
d = {x: ord(x) for x in 'python'}  # 遍历字符串 'python' 的每个字符，键是字符，值是 ASCII 码。
print(d)  # --->{'p':112,'y':121,'t':116,'h':104,'o':111,'n':110}

h = {x: y for x in {1, 3, 5} for y in {2, 4, 5}}
print(h)  # --->{1:2,1:4,1:5,3:2,3:4,3:5,5:2,5:4,5:5}}错啦
# 实际结果：{1: 5, 3: 5, 5: 5}
# 因为每个 x 对应的最后一个 y 都是 5，前面的被覆盖了。1:2,然后1：4,然后1：5，只保留1:5最后一个值.
# 因为一个字典里的键不能重复。d={a:3,a:4}不成立，key只能取一个值。value可以重复。
# 注释写的 {1:2,1:4,1:5...} 是错误的，字典不允许重复键。
