# 收集参数：用*号加在args前面，表示可以一个或者多个参数：
def print_args(*args):
    print("有{}个参数".format(len(args)))
    # --->(1,2,3)传入的参数数量随意。
    print(f"第{2}个参数是{args[1]}")
    return args


result = print_args(1, 2, 3, 4)
print(result)

"""
含义： 格式化字符串，显示参数数量。
拆解：
'有{}个参数' - 模板字符串，{} 是占位符
.format(len(args)) - 用 len(args) 的值替换 {}
len(args) - 计算元组 args 的元素个数
示例：
args = (1, 2, 3)
print('有{}个参数'.format(len(args)))
输出：有3个参数

等价于：
print(f'有{len(args)}个参数')

参见：格式化字符串
"""
"""--->有4个参数
    第2个参数是2
    (1,2,3,4)
python 函数return的是一个元组。"""

print("-" * 88)


# 拿到一个解包的元组：
def print_args1(*args):
    return args


# print_args1(1, 2, 3)

x, y, z = print_args1(1, 2, 3)
print(x, y, z)


# 用*号加在kwargs前面，表示可以一个或者多个参数：其实就是把参数打包成元组：
def myfunc(*args):
    print(type(args))
    # return args


print(myfunc(1, 2, 3, "hello"))


# <class 'tuple'>
# ---->None 因为函数没有return语句，没有返回值，所以返回None.如果有，就返回return的值-->(1,2,3,'hello')


# 函数的搜集参数（*args)是一个元组，里面的元素是函数的参数。还可以有另外的参数，但是必须是关键字参数：
def myfunc(*args, a, b):
    print(args, a, b)
    return (
        args,
        a,
        b,
    )  # --->((1,2,3),22,33)返回的参数组成一个元组。可以return args,也可以return args,a,b


result = myfunc(1, 2, 3, a=22, b=33)
print(result)  # --->(1,2,3,) 4 5


# 用*星号限制*号后面的必须使用关键字参数。*星号本身是语法分隔符，类似/的作用，/前面的必须是位置参数，
def myfunc(a, *, b, c):  # 其中的*是个语法分隔符。
    print(
        a,
        b,
        c,
    )


result = myfunc(
    a=5, b=77, c=88
)  # 也可以写： result=myfunc(5,b=77,c=88),因为a是位置参数。
print(result)


# 收集参数可以将多个参数打包为元组，还可以打包成字典：通过两个相连的**号实现：
def myfunc(**kwargs):
    print(kwargs)
    return kwargs


result = myfunc(a=2, b=5, c=8)  # 传入的必须是关键字参数
print(result)


# --->{'a':2,'b':5,'c':8}


def myfunc(a, *args, **kwargs):
    print(a, args, kwargs)
    return a, args, kwargs


result = myfunc(1, (2, 3, 4), c=22, d=33)
print(result)
# --->(1 ((2,3,4),) {'c':22,'d':33})这是打印print的结果，1与((2,3,4),)和{'c':22,'d'：33}之间都没有逗号，所以打印的时候没有打印出来。
# return的返回值是(1,((2,3,4),),{'c':22,'d':33}）,这个就是三个元素组成的元组，中间有逗号。
"""
调用 myfunc(1, (2, 3, 4), c=22, d=33)
a = 1 - 位置参数
args = ((2, 3, 4, 5),) - 收集多余的位置参数（注意：这里传入的是一个元组，所以 args 是包含这个元组的元组）
kwargs = {'c': 22, 'd': 33} - 收集关键字参数字典
"""

result = myfunc(1, 2, 3, 4, c=22, d=33)  # args=(2,3,4)是一个元组，不是元组的元组
print(result)  # --->(1 (2,3,4) {'c':22,'d':33})
# return:---->(1,(2,3,4),{'c':22,'d':33})


# format()方法可以同时用*，和**作为收集参数
help(str.format)
"""
Help on method_descriptor:

format(...) unbound builtins.str method
    S.format(*args, **kwargs) -> str

    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').
    
第一个就是元组形式的收集参数*args，第二个就是字典形式的收集参数**kwargs
"""

# 解包参数：一个星号*，和两个星号**，在用定义函数，当作形参的时候，是打包参数，在调用参数的时候，是解包参数
args = (1, 2, 3)  # 一个变量args，里面有3个元素


def myfunc(a, b, c):
    print(a, b, c)  # ---> 1 2 3
    return a, b, c


result = myfunc(
    *args
)  # 实际参数传入带*号的元组，结果解包参数。前提是先有一个变量args,是一个元组
print(result)  # --->(1,2,3)

# 两个**对应的时关键字参数，也就是键值对，即字典：

kwargs = {"a": 1, "b": 2, "c": 3}


# 字典键是字符串时必须加引号，否则Python会把它当变量。


def myfunc(a, b, c):
    print(a, b, c)  # --->1 2 3
    return a, b, c


result = myfunc(**kwargs)
print(result)  # --->(1,2,3)
