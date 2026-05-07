# 闭包：closure
def myfunc():
    x = 520
    print(x)


myfunc()  # --->520


# print(x)  # 报错：NameError: name 'x' is not defined
# 内部变量x是局部变量，在函数内部定义，在函数外部无法访问。


def myfunc1():
    x = 520

    def myfunc2():
        print('在myfunc2函数中，x=', x)

    myfunc2()  # 定义完了myfunc2(),立即调用。得到的值是：在myfunc2函数中，x= 520，但是没有return语句，所以返回None。。


myfunc1()  # --->在myfunc2函数中，x= 520，用外部函数调用内部函数。
# 一个细节：变量x=520是在函数myfunc1()中定义的，所以x是myfunc1()的局部变量。但是在内部函数myfunc2()中调用了。
# 即：调用函数myfunc1()之后，内部函数 myfunc2()调用了外部函数的局部变量。
# 上面是嵌套函数。内层的函数不能直接调用，要用外层函数调用内层函数。
print('-' * 88)


# 除了用myfunc1()来调用myfunc2(),还可以把myfunc2()当作myfunc1()的返回值：
def myfunc1():
    x = 520

    def myfunc2():
        print('在myfunc2函数中，x=', x)

    return myfunc2


# myfunc2没有小括号，表示返回的是一个函数，而不是执行一个函数得到函数的值。

# 注意return语句的缩进，是属于myfunc1()的。

myfunc1()  # ---><function myfunc1.<locals>.myfunc2 at 0x0000020E5E5E0E80>


# myfunc1() 没有加括号调用内部函数,只是返回了 myfunc2 这个函数本身,所以显示的是函数对象的地址。
# 函数只有在定义和调用的时候，才使用小括号。

def myfunc1():
    x = 520

    def myfunc2():
        print('在myfunc2函数中，x=', x)

    return myfunc2()


# myfunc2有小括号，表示返回的是函数myfunc2()的值。

myfunc1()  # --->在myfunc2函数中，x= 520

print('~' * 88)


def myfunc1():
    x = 520

    def myfunc2():
        print('在myfunc2函数中，x=', x)

    return myfunc2


# myfunc2没有小括号，表示返回的是一个函数，而不是执行一个函数得到函数的值。

# 注意return语句的缩进，是属于myfunc1()的。

myfunc1()()  # --->在myfunc2函数中，x=520


# 第一个 (): 调用 myfunc1(),返回 myfunc2 函数对象:即函数myfunc2()的内存地址。
# 第二个 (): 调用返回的 myfunc2(),执行打印操作


def myfunc1():
    x = 520

    def myfunc2():
        print('在myfunc2函数中，x=', x)

    return myfunc2()  # --->加了括号，立即执行函数，返回函数的值。


# myfunc1()()  # 报错：TypeError: 'NoneType' object is not callable
# 报错原因：
# 1. myfunc1() 返回的是 None（因为 myfunc2() 没有return，返回None）
# 2. 第二个 () 是【函数调用符号】，试图把前面的结果当成函数调用
# 3. 但 None 不是函数，不能加 () 调用，所以报错
print('-' * 88)


def funA():
    x = 8880

    def funB():
        print('在函数funB中，x=', x)

    return funB


# funA()()
funny = funA()()
# funny()#-->8880

"""
LEGB的E有这样一个特性：对于嵌套函数来说，外层函数的作用域，是会通过某种形式保存下来的。尽管这个函数已经调用完了。
但是外层作用域里面的变量是会保存下来的。不会像局部作用域那样，调用完就消失了。
局部作用域 就是指 非嵌套函数。它的变量叫 局部变量。
"""
print('--_--' * 88)
"""
所谓闭包，也叫 工厂函数
"""


# 定义一个函数power(),函数power()的参数是exp，返回一个函数exp_of()。 power()就是一个工厂。
def power(exp):
    def exp_of(base):
        return base ** exp

    return exp_of


square = power(2)  # 先给参数exp赋值2，那么exp_of(base)的返回值：base**2就是取平方的意思。
cube = power(3)  # 先给参数exp赋值3，那么exp_of(base)的返回值：base**3就是取立方的意思。

square(2)  # --->4 其实是给base赋值2
print(square(5))  # --->25 其实是给base赋值5
cube(3)  # --->27 3次方 其实是给base赋值3
print(cube(3))


def outer():
    x = 0
    y = 0

    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f'现在x={x}，y={y}')

    return inner


move = outer()
move(1, 2)  # --->现在x=1,y=2

move(-2, 2)  # --->现在x=-1,y=4
# 利用内存函数能记住外层函数作用域的变量的特性，并使用nonlocal语句来修改外层作用域的变量。这样就得到一个带记忆功能的函数。


"""
闭包（Closure）定义：
闭包是一个内部函数，它：
引用了外层函数的变量（自由变量）
外层函数返回这个内部函数
即使外层函数执行完毕，内部函数仍能访问外层函数的变量

核心三要素：
嵌套函数结构
内层函数使用外层函数的局部变量
外层函数返回内层函数
本质： 闭包 = 函数 + 它引用的环境变量
关键特性： 外层函数调用结束后，其作用域中的变量不会销毁，而是被闭包"记住"并持续可用。
"""
