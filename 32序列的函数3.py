# map()函数：会根据提供的函数对指定的可迭代对象的每个元素进行运算，并将返回运算结果的迭代器。

x = [1, 2, 3]
y = [4, 5, 6]
z = ['how']
zip(x, y, z)
print(list(zip(x, y, z)))  # ---->[(1,2,'how')] 没有（2，5，'how'),也没有（3，6，'how'),
# 因为zip()函数针对的是所给对象的元素，而z=['how']只有一个元素：'how'.
# 要呈现多的元素的迭代器的结果，需要使用itertools.zip_longest()函数。首先要import itertools:
import itertools

print(list(itertools.zip_longest(x, y, z)))  # --->[(1,4,'how'),(2,5,None),(3,6,None)],2、5和3、6都出来了。缺少的用None填充。

print(list(map(ord, 'fishC')))  # ord:求出一个字符的unicode编码---->[102, 105, 115, 104, 67]:fishC的每一个编码，返回列表。

mapped = map(pow, [2, 3, 10], [5, 2, 3])  # pow(x,y)函数是求x的y次方。
print(list(mapped))
# map()函数与zip()函数一样，按传入的可迭代对象的元素最少的 来执行，其他的用None填充。
print(list(map(max, [1, 2, 3], [4, 6], [0, 7, 8, 9])))  # --->[4，7]max:返回可迭代对象中的最大值。0就不管了.

print('-' * 80)

# filter()过滤器   函数会根据提供的函数对指定的迭代器对象的每个元素进行运算，并将运算结果为真的元素，以迭代器的形式返回。
# 跟map()函数一样，filter()函数也是先传入一个函数当参数，然后对后面传入的可迭代对象操作。
# 但是map()函数是用计算结果返回迭代器，
# 而filter()函数是用计算结果为真的原迭代器的元素来返回一个迭代器。

print(list(filter(str.islower, 'FishiC')))  # --->['i','s','h','i']islower:判读哪一个是小写，为True，两个i都列出了。

# zip()聚合打包函数将多个序列打包成元
# map()映射函数将函数映射到每个元素
# filter()过滤函数根据条件过滤元素
