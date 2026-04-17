"""
一般的函数被调用后，从第一行代码执行，一直到函数执行完毕，或return 返回值。这个函数就结束了。下次要用，就再次调用
那么，有啥办法让这个函数执行完之后，还保留他的状态呢？有个方法：闭包。使用全局变量也可以实现。
不过，过多的使用全局变量，会污染命名空间。闭包的定义又相对复杂。所以，用一种既简单又安全的方法： 生成器 generator
"""


# 定义一个生成器：在函数中用yield表达式来代替return语句
def conter():
    i = 0
    while i <= 5:
        yield i
        i += 1


# 定义了一个叫做conter的生成器。返回的是一个生成器对象：generator object。
print(conter())  # --><generator object conter at 0x000002B8E471C640>
# 在for语句中，像调用函数一样调用生成器。：
for i in conter():
    print(i)
# --->0
# --->1
# --->2
# --->3
# --->4
# --->5
# for语句：每次从生成器中取出一个元素，并赋给变量i，然后执行for语句的代码块。当for语句执行完毕时，生成器就结束了。
# 生成器像是一个制作机器，每次从里面制作出一个元素，然后返回给调用者。
# 而列表，集合，元组等，是一个容器，每次从里面取一个元素。
# 生成器可以看作为一个特殊的迭代器。1，不走回头路，即只运行一次。2，可以用next()函数获取生成器的下一个元素。
c = conter()
print(c)  # ---><generator object conter at 0x000002B8E471C640> 把生成器赋值给一个变量。
print(next(c))  # --->0
print(next(c))  # --->1
print(next(c))  # --->2
print(next(c))  # --->3
print(next(c))  # --->4
print(next(c))  # --->5
# 结束。


# 生成器因为每次调用一次生成一个结果的原因，不能用下标的方式随机访问元素
c = conter()

# c[2]  # --->TypeError: 'generator' object is not subscriptable

print('-' * 88)


# 用生成器求斐波那契数列：每个数字是前面两个数字的和
def fib():
    back1, back2 = 0, 1
    while True:
        yield back1
        back1, back2 = back2, back1 + back2


f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13


# 此时的fib()生成器并没有设置结束符，所以如果用for语句调用的话，会一直运行下去。
# for i in fib():
#     print(i)
#
# 如果要限制生成器的运行次数，可以用for语句配合if 语句：
for i in fib():
    if i > 100:
        break
print('--' * 89)
# 生成器推导式：用生成器推导式来创建生成器。以前有列表推导式，而没有元组推导式
m = [x ** 2 for x in range(10)],  # 把列表转为元组：
print(m)  # --->([0, 1, 4, 9, 16, 25, 36, 49, 64, 81],)
n = (x ** 2 for x in range(10))
print(n)  # ---><generator object <genexpr> at 0x000002B8E471C640>
print(next(n))  # --->0
print(next(n))  # --->1
print(next(n))  # --->4
print(next(n))  # --->9 从0到10的平方数
for i in n:
    print(i)

# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81


# 用推导的方法得到生成器的方法，叫生成器表达式
# 生成器表达式 和列表推导式最大的不同就是，列表推导是返回的是一个包含众多元素的列表，而生成器表达式是一次只生成一个值。

# 创建生成器的两种方法：
# 1，用yield代替return.
# 2,用生成器表达式生成。
