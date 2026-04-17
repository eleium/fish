# python 把集合分为set()可变的和frozenset()不可变的两种。前面学习的方法都是不改变集合的。现在学习一些改变集合的方法。
# update(*others)方法：用others指定的值来跟新集合。
t = frozenset('FishC')
print(t)  # --->frozenset({'F','I','s','h','C'})
"""
这是因为 frozenset 的字符串表示形式就是 frozenset({...})，这是 Python 的设计。
核心原因：
区分类型：{} 表示普通字典或集合，而 frozenset({...}) 明确表示这是一个不可变集合
可读性：让你一眼就能看出这是 frozenset 类型，而不是普通的 set
"""
s = set('abc')
print(s)

# s=set{'abc'}报错。
# set() 是函数调用，必须用圆括号 ()
# {} 是集合字面量语法，用于直接创建集合
# {'abc'} ✅ 创建一个包含单个字符串的集合

s = {'abc'}
print(s)  # --->{'abc'}而非{'a','b','c'},注意与set('abc')的区别。

s = set('FishC')
s.update([1, 1], '23')  # 在集合s里添加1和1和2和3，因为1重复了，只添加一个1.
print(s)  # --->{'F',1,'s','h','C','2','3','I'}
# print(t.update(frozenset(t)))  # AttributeError: 'frozenset' object has no attribute 'update'.frozenset()集合没有update()方法。

# 用差集/并集/合集等来更新集合：
print(s.intersection_update('python'))  # --->None  intersection_update():并集
print(s)  # --->{'h'}
"""
核心结论（超级重要）
所有带 _update 的集合方法：
intersection_update、difference_update、update
它们都【不返回任何东西】，所以打印它 == 打印 None
它们直接修改原集合本身，而不是返回新集合。
集合方法分两类：
返回新集合（有返回值，可以 print）
intersection()
union()
difference()
symmetric_difference()

直接修改原集合，无返回值 → print 就是 None
intersection_update()
update()
difference_update()
symmetric_difference_update()
凡是名字带 _update 的，都不要直接 print！
终极一句话
intersection_update 不返回东西，所以 print 它 = None。
要想看结果，必须执行后 print 原集合 s。
"""
s.difference_update('python')  # 差集
print(s)  # --->{'h'-('p','y','t','h','o','n')}={} 空集

s.symmetric_difference_update('python')  # 对称差集：保留只在其中一个集合中的元素：对称差集 = 排除共同拥有的，留下各自独有的。
print(s)  # --->{'h','p','y','t','o','n')#刚刚经过difference_update()已经变成了空集，所以现在s
print(s.symmetric_difference_update('hello world'))  # --->None
print(s)  # --->{'p','y','t','n','e','l','r','w','d',' '}
# None = 函数没返回东西，而set() = 集合存在但里面没元素，完全不是一回事。
# 另外，集合用set()表示，而不是set{}。你可以直接用{},前面不加set.

# union()方法==union_update()方法。对or错？union()方法返回一个新集合，而union_update()返回None.这两句最终效果相同，但执行方式完全不同。

# 在集合里面添加新元素，用add()方法：
t = {'a', 'b', 'c'}
t.add('hello')
print(t)  # --->{'a','b','c','hello'}

# 注意：add('string')是把string'作为一个字符串插入集合。update('string')把字符串的每一个元素拆开，插入集合。
print('-' * 88)
# 用remove()和discard()方法去除集合中的元素。如果集合中没有要去除掉的元素，remove()会报错，而discard()会保持静默。
print(t.remove('hello'))  # 因为 remove() 方法不返回任何东西（返回 None），它只是直接修改集合。这和之前讲的 _update 方法一样：
# print(t.remove('w'))#报错
print(t.discard('w'))  # --->None  修改了原集合，但是就完事了，就返回None
print(t)  # --->{'a','b','c'}

"""
集合方法的规律：
返回 None 的方法（修改原集合）：
add()、remove()、discard()、pop()
update()、intersection_update()、difference_update()、symmetric_difference_update()

返回新集合的方法（不修改原集合）：
union()、intersection()、difference()、symmetric_difference()
记住：凡是直接修改原集合的方法，都返回 None！
"""

# 用pop()方法随机弹出一个元素：其实也不知道怎么随机的，因为集合是无序的。
print(t.pop())  # --->c用pop()方法随机弹出了一个元素： c .
print(t)  # --->{'a','b'}

# 用clear()方法清空集合？
print(t.clear())  # --->None 也是改变了集合，但是就完事了，就返回None
print(t)  # --->set()

# 可哈希：想要正确地创建一个集合和字典，有一个刚性要求：集合的元素和字典的键都必须是可哈希的。
# 一个对象是可哈希的，意味着这个对象的哈希值在程序的生命周期里不会改变。集合的元素和字典的键必须可哈希，否则会报错。
# 可哈希 = 对象的"身份证号码"永远不变

# 想象每个对象都有一个唯一的身份证号（哈希值），可哈希就是这个身份证号从出生到死亡都不会变。
# 通过hash()函数可以获取对象的哈希值
print(hash('hello'))  # 字符串的哈希值每次都变化
print(hash('hello'))  # 哈希值与上面一样，因为这两行代码算是同一次计算。所以相同。
print(hash(5))  # 整数的哈希值是整数本身。
print(hash(5.0))  # 如果两个数相等，那么它们的哈希值也相等。

print(hash(5.001))
print('-' * 88)
# 字符串和元组是可哈希的。字典/列表和集合是可变的，不可哈希。
# print(hash([1, 2, 4]))
# print(hash({1, 2, 4}))
# print(hash({1: 2, 3: 4}))


# 只有不可变的，可哈希的对象，才能当作字典的key:
t = {'python': 52, 'java': 50}  # 没问题
k = {'python': [1, 2, 3], 'java': ['a', 'b', 'c']}
print(k)

# j = {[1, 2, 3]: 'pyton'}  # 报错，因为不能用可变对象当字典的key.

# 集合里面有列表可以吗？不可以。集合的元素必须可哈希。
# n = {'python', [1, 2, 3]}#--->报错。因为list是不可哈希的，集合不能有不可哈希元素。
# print(n)

# 嵌套集合？
# j = {'python', {1, 2, 3}}  # 报错
# print(j)

o = {'python', frozenset({1, 2, 3})}  # 成立
print(o)  # --->{'frozenset({1,2,3}),'python}不可变的集合就可以嵌套啦。

# frozenset({1,2,33})==frozenset([1,2,3])==frozenset({[1,2,3]}) 前两个对，后一个集合里面不能有列表。
# frozenset({1,2,3})直接创建frozenset集合。frozenset([1,2,3])把一个列表，转化为一个frozenset集合。

# 集合的背后有散列表支持，而列表没有。所以集合的查询效率比列表高很多。数目越大，效率越高。代价是海量的存储空间：以空间换时间
