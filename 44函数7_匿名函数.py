# 匿名函数 lambda
# 匿名函数：lambda + 参数 + ： + 函数体
# 掌握了lambda表达式就掌握了 一行流 代码的核心：
# lambda语法结构：
# lambda arg1,arg2,arg3,...argN:expression
# 冒号左边是函数传入的参数，冒号右边是函数实现表达式及返回值。
# lambda可以理解为一共极致精简之后的函数。
"""传统定义方式：
 def <lambda>(arg1,arg2,arg3,...argN):
    return expression
    """


# 写个函数：求出传入参数的平方值：
def squareX(x):
    return x ** 2


print(squareX(5))  # --->25

# 用lambda表达式：
squareY = lambda y: y ** 2
print(squareY(4))  # --->16

# 传统定义的函数，函数名就是一个函数的引用，
print(squareX)  # ---><function squareX at 0x0000020EB0EA5EA0>

# 整个lambda表达式就是一个函数的引用。上面的例子，把lambda表达式赋值给squareY变量，squareY变量就是一个函数的引用。
print(squareY)  # ---><function <lambda> at 0x0000020EB0EA5EA0>

# 两种有个重大的区别：lambda是表达式，可以用在传统函数不能使用的地方：比如 列表：
y = [lambda x: x ** 2, 2, 3]
print(y[0](y[1]))  # --->4  [0]是lambda表达式。[1]是列表中的第二个元素：2.
# 用括号把y[1]括起来，表示调用lambda表达式，并且窜入参数是y[1]，即：2.


# 用map()函数举例子：map(function, iterable)，第一个参数是函数，第二个参数是可迭代对象。并返回一个迭代器。
mapped = map(lambda x: ord(x) + 10, 'python')  # ord()函数：返回字符的ASCII码值并加10.返回一个迭代器，不能直接读，要用list列表后读取。
# ord()只接受一个字符。
# map() 的正确作用：将函数应用到序列的每个元素，生成新序列。
print(list(mapped))  # --->[122, 131, 126, 114, 121, 120]

# 用filter()函数举例子：filter(function, iterable)，第一个参数是函数，第二个参数是可迭代对象。并返回一个迭代器。
filtered = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# filtered()函数的作用：过滤序列，保留是函数返回True的元素。
print(list(filtered))  # --->[2, 4, 6, 8, 10]


# map() = 转换每个元素（如加 10、平方），而filter() = 过滤元素（保留符合条件的）

# 用传统的方法：
def myfunc(x):
    return ord(x) + 10


mapped = list(map(myfunc, 'python'))

print(mapped)  # --->[122, 131, 126, 114, 121, 120]

filtered = list(filter(lambda x: x % 2, range(10)))
print(filtered)  # --->[1, 3, 5, 7, 9]

"""
总结：
lambda是一个表达式而非语句，所以它可以出现在python不允许def语句出现的地方，这是它最优势的地方。
但是由于所有的功能代码都局限于一个表达式中去实现，因此lambda表达式也只能实现一些较为简单的需求
python 希望用lambda解决简单需求，用def 解决复杂的需求。
"""
