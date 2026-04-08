# 序列的函数all()，any():   all()判断可迭代对象中的元素是否都为真值，any()判断可迭代对象中的元素是否至少有一个真值。
x = [1, 2, 3, 0]
y = [1, 2, 3, 4]
print(all(x))  # ---->False 0的值不是真值。
print(all(y))  # ---->True
print(any(x))  # ---->True
print(any(y))  # ---->TRue

# enumrate():返回的是一个枚举对象。枚举对象是一个迭代器，返回的是一个列表，列表的第一个元素是索引，第二个元素是元素本身。
# 即将一个可迭代对象的每一个元素，与从0开始的序号，组成一个二元组的列表。
season = ["春", "夏", "秋", "冬"]
print(
    enumerate(season)
)  # ----><enumerate object at 0x00000171964D9760>得到一个枚举对象。
print(list(enumerate(season)))  # ---->[(0, '春'), (1, '夏'), (2, '秋'), (3, '冬')]
print(
    list(enumerate(season, 10))
)  # ---->[(10, '春'), (11 '夏'), (12, '秋'), (13 '冬')] 有个start参数，指定从哪个数开。

print("*" * 88)
"""
zip()函数：返回一个聚合多个可迭代对象的迭代器，可以用list把它转为列表查看。。它会将 作为参数传入的每个可迭代对象的每个元素，依次组合成元组，
即：第i个元组 包含来自每个参数的第i个元素
以最短的可迭代对象为准：如果输入的可迭代对象长度不同，zip 会以最短的那个为准
可以解压：使用 * 操作符可以解包 zip 对象
"""
h = ["小王", "小李", "小张", "老孙"]
g = [10, 20, 30, 40]
k = ["a", "b", "c", "d"]
zip(
    h, g, k
)  # zip()函数可以接受任意数量的参数（包括 0 个），但通常我们使用它时传入 2 个或更多的可迭代对象来进行聚合。
print(
    list(zip(h, g, k))
)  # -->[('小王', 10, 'a'), ('小李', 20, 'b'), ('小张', 30, 'c'), ('老孙', 40, 'd')]

print(list(zip()))  # ---->[]空列表

l = [1, 2, 3]
print(list(zip(l)))  # ---->[(1,), (2,), (3,)]把每一个元素当成一个元组。

x = [1, 2, 3]
y = [4, 5, 6]
zip(x, y)
print(list(zip(x, y)))

z = [7, 8, 9]
zipped = zip(x, y)
print(list(zip(z, zipped)))  # -->[(7,(1,4)),(8,(2,5)),(9,(3,6))]
# 变量z 在zipped 前面，注意顺序： zip(z,zipped)

print(list(zip(x, y, z)))  # --->[(1,4,7),(2,5,8),(3,6,9)]

x = "heloo"
print(
    list(zip(x, y, z))
)  # --->[('h',4,7),('e',5,8),('l',6,9)] 以元素少的可迭代对象为准。

import itertools

print(
    list(itertools.zip_longest(x, y, z))
)  # --->[('h',4,7),('e',5,8),('l',6,9),('o',None,None),('o',None,None]
# itertools.zip_longest() 函数的参数与 zip() 函数一样，但会以 None 填充空缺的位置。
