"""
一个迭代器必然是一个可迭代对象，但是，可迭代对象是可以重复操作，而迭代器只能用一次。
"""

mapped = map(ord, 'fishC')
for each in mapped:
    print(each)

print(list(mapped))
print(mapped)

x = [1, 2, 3, 4, 5]
y = iter(x)
print(y)  # --> <list_iterator object at 0x0000020E0EA0EA90>  列表迭代器，内存地址：0x0000020E0EA0EA90
print(type(x))  # ---> <class 'list'>  类型：列表
print(type(y))  # ---> <class 'list_iterator'>  类型： 列表类的迭代器

# next()函数：把迭代器的内容元素逐个提取出来：运行一次，提取一个元素。
print(next(y))  # ---> 1
print(next(y))  # ---> 2
print(next(y))  # ---> 3
print(next(y))  # ---> 4
print(next(y))  # ---> 5

# 运行一次，没有元素了，报错：这是个异常，异常是可控的，往往是故意做出的。如果是错误，那是不可控的。
# print(next(y))  # ---> Traceback (most recent call last):
#  File "D:/python/python_code/33迭代器与可迭代对象.py", line 27, in <module>
#    print(next(y))
# StopIteration

# 如果不想抛出异常，可以用next()函数的第二个参数：

z = iter(x)  # 因为迭代器 y=iter(x)是一次性的，所以要重新定义一个迭代器。
print(next(z))  # --->1
print(next(z))  # --->2
print(next(z))  # --->3
print(next(z))  # --->4
print(next(z))  # --->5
# 所有元素已经都提取完毕，此时如果不想抛出异常，可以给next()函数加上第二个参数：
print(next(z, '没有元素啦'))  # --->没有元素啦
