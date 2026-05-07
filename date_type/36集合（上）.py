print(type({}))  # ---><class 'dict'>
print(type({1, 2}))
# ---><class 'set'>
# 集合：set{},集合中的元素是唯一的，不能重复，而且是无序的。
# 因为集合是无序的，所以不能用下标索引来定位取得元素。
a = {"python", "china", "java", 3}
# 集合推导式：

b = {x for x in 'python'}
print(b)  # --->{'h','y','n', 'p', 't'}无序的。

"""
列表、字典和集合都有推导式。而元组和字符串没有推导式。
其中元组有生成器，叫 元组的生成器表达式：元组生成器表达式：(x for x in range(10))
列表推导式：[x for x in iterable if] x是表达 iterable是可迭代对象
[x for x in [1,2,3]]
print(x) --->[1,2,3]

[x**2 for x in {2,3,4}]   x**2是表达式
print(x) --->[4,9,16] 不管可迭代对象的类别，都返回列表。

可以是任何可迭代对象，而不仅仅是range(),range()是序列生成器。不是随机，随机是random()。
[x for x in [1, 2, 3]]           # 列表
[x for x in (1, 2, 3)]           # 元组
[x for x in 'abc']               # 字符串
[x for x in {1, 2, 3}]           # 集合
[x for x in {'a': 1, 'b': 2}]    # 字典的键

字典的推导式：
{键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}
{x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}x是key,x**2是value,在（0，1，2，3，4）中遍历。

names = ['a', 'b', 'c']
scores = [90, 80, 70]
{name: score for name, score in zip(names, scores)} zip: 聚合两个列表为多个元组。list(zip(names, scores))---->
# [('a', 90), ('b', 80)]  是 多个元组.  zip(names,scores)是一个迭代器。用list把它呈现为一个多个元组的列表。
# {'a': 90, 'b': 80, 'c': 70}

d = {'a': 1, 'b': 2}
{v: k for k, v in d.items()}
# {1: 'a', 2: 'b'}键、值互换。

核心：key: value 成对出现，用 items() 遍历原字典。

"""

# 类型构造器：set
set('python')
m = set('python')
print(m)  # --->{'p','t','y','n','o'}无序
# print(m[2])  # 报错：TypeError: 'set' object is not subscriptable，集合是无序的，不能用下标索引来定位取得元素。

# 可以用 in 和 not in 来判断元素是否在集合中：
print('p' in m)  # --->True
print('l' not in m)  # --->True

# 可以用迭代的方式来访问集合中的元素：
for x in m:
    print(x)
# --->p
# --->t
# --->y
# --->n
# --->o
# --->h

# 利用集合的元素的唯一性，可以方便的去重：
a = [1, 2, 3, 3, 4, 5, 5, 6]
b = set(a)
print(b)  # --->{1,2,3,4,5,6}

# 不用集合，可以用迭代的方式判断一个元素出现的次数。有了集合就方便了：

s = [1, 1, 2, 3, 5]
print(len(s) == len(set(s)))  # --->False  len(s)=5,len(set(s))=4

# 用迭代方式统计每个元素出现的次数：
s = [1, 1, 2, 3, 5]
count_dict = {}
for item in s:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict)  # --->{1: 2, 2: 1, 3: 1, 5: 1}

# 或者使用列表的count()方法：
s = [1, 1, 2, 3, 5]
for item in set(s):
    print(f"元素 {item} 出现了 {s.count(item)} 次")

# 判断是否有重复元素（不用集合）：
s = [1, 1, 2, 3, 5]
has_duplicate = False
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            has_duplicate = True
            break
    if has_duplicate:
        break
print(f"是否有重复元素: {has_duplicate}")  # --->True

# 集合的浅拷贝:
s = {1, 1, 2, 3, 5, 7}
t = s.copy()
print(t)  # --->{1,1,2,3,5,7}集合是唯一的，不能重复。{1，2，3，5，7}
print(id(s))
print(id(t))
print('-' * 80)
# 用isdisjoint()方法判断两个集合是否相交：是否有共同的元素。有的话是False，没有的话是True。

s = set('hello')
print(s)
print(s.isdisjoint(set('python')))  # --->False:集合s与集合'python'有一个共同的元素"h"。
# 此时传入的是用set()构造的集合，而不是字符串，事实上，直接传入字符串也是可以的：
print(s.isdisjoint('people'))  # --->False:有共同的'o'元素

# 用issubset()方法判断一个集合是否是另一个集合的子集：A有的B全有。
h = set('hello world')
# n = set{'good study','hello world'}# set() 只能接受一个参数，不能这样写。
n = set('good study,hello world,tomorrow is fine')
print(h.issubset(n))  # ---> True h是n 的子集。

# 用issuperset()方法判断A集合是否是B集合的超集？超集是子集的反向关系：
# A 是 B 的子集：A 的所有元素都在 B 中（A ⊆ B）
# B 是 A 的超集：B 包含 A 的所有元素（B ⊇ A）
print(n.issuperset(h))  # --->True n 是 h 的超集。注意不要搞反了。

# 用union()方法把两个集合合并为一个新集合：并集
j = h.union(n)  # 用一个集合取union另外一个集合。
print(j)  # --->{'d', 'l', 'o', 's', ',', 'e', 'm', 'g', 't', 'f', 'n', 'w', 'y', 'h', ' ', 'u', 'I', 'r'}

# 用intersection()方法找到两个集合的交集：也是新的到一个集合.

m = h.intersection(n)
print(m)  # --->{' ', 'o', 'l', 'd', 'r', 'w', 'e', 'h'}

# 用difference()的方法求得两个集合的差集：得到一个新集合。即：A-B,去掉重复的元素后的集合。
l = h.difference(n)
print(l)  # --->set{}空集合
o = n.difference(h)
print(o)  # --->{'s', 'y', ',', 'm', 'g', 't', 'f', 'u', 'I', 'n'}

# 方法union(),intersection()和difference()都可以多参数：
# p = h.union({1, 2, 3}, 'python')  # 报错：union() 的参数必须是可迭代对象，但集合只能合并相同类型的元素。
# 错误原因： h 是字符串集合（元素都是字符串），{1,2,3} 是整数集合，类型不同无法直接合并。
p = h.union({'1', '2', '3'}, 'python')
print(p)

q = h.intersection(h, n, 'python', 'hello world')
print(q)  # --->{'h','o'}

r = h.difference(h, n, 'python')
print(r)  # --->set{}空集合
y = h.difference('hello', 'd')
print(y)  # --->{'r','w',' '}  'hello world'-'hello'-'d'='worl',所有的'o'和'l'重复的都减去了，剩下'd'和一个空格。

# 用symmetric_difference()方法求两个集合的异集：对称差集（异集） = 只在其中一个集合中出现的元素（排除两个集合的交集）。
# 公式：A △ B = (A - B) ∪ (B - A)，去掉两个集合的共同部分，剩下各自独有的元素。
"""
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 对称差集 = 只在 A 或只在 B 的元素
print(A.symmetric_difference(B))  # {1, 2, 5, 6}

# 等价于：
print((A - B) | (B - A))  # {1, 2, 5, 6}
# 或者用 ^ 运算符
print(A ^ B)  # {1, 2, 5, 6}
"""
# python 对于上面的6种方法，可以用运算符计算真假：
# 用<=来验证子集和真子集
print(h <= n)  # --->True
print(h < n)  # --->True  没有=号，叫做真子集。有=号叫子集
# 用>=来验证超集和真超集
print(h >= n)  # --->False
print(h > n)  # --->False

# 并集的验证用那根竖： | 也叫管道符
print(h | n)  # --->{'t', 'm', 'e', 'u', 'n', 'I', 'l', 'g', 'f', ' ', 'w', 's', 'r', 'h', 'd', ',', 'y', 'o'}
print({"1", "2", "3"} | {'python'})  # --->{'1', '2', '3', 'python'}

# 交集用 &符号：
print(h & n)  # --->{'h', 'o', 'l', 'd', 'r', 'w', 'e'}
# 差集用 - 减号：
print(h - n)  # --->set()空
print(n - h)  # --->{'I', 's', 'u', 't', 'm', 'n', 'g', ',', 'f', 'y'}

# 对称差集用脱字符：^
print(n ^ h)  # --->{'I', 's', 'u', 't', 'm', 'n', 'g', ',', 'f', 'y'}

# 使用运算符，符号两边必须都是集合类型的数据才行，方法可以是任何可迭代对象，运算符不行。
# print(s <= 'hello world'),报错因为s是集合，'hello world是字符串'
