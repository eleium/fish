"""
闭包的核心：
1，利用外层函数作用域有记忆的特性，让数据保存在外层函数的参数或变量中。
2.将内层函数作为返回值给它返回了。这样就可以在外部间接的访问调用内层函数。

那么，能不能把一个函数当作参数给传递给另一个函数呢？有的：装饰器：decorator
"""


def myfunc():
    print('正在调用myfunc函数。。。')


def report(func):
    print('我要开始调用函数啦。。')
    # 只写函数名称，不带括号，是引用函数。带上小括号，是调用函数。
    func()
    print('函数已经调用完毕。')


report(myfunc)
# 输出结果：我要开始调用函数啦。。
#          正在调用myfunc函数。。。
#          函数已经调用完毕。
"""
函数作为参数传递给另一个函数，这个函数被称之为高阶函数。

def report(func):
func 是形参，只是一个名字
当你调用 report(myfunc)
myfunc 是实参，而它本身是函数
所以 func = myfunc
所以 func 变成了函数引用
所以 func() 可以执行

如果你后来report('水壶'),那么func=='水壶',就是一个字符串。

🔥 真正的执行顺序（按数字走）
1. 定义函数 myfunc（不执行里面的代码）
2. 定义函数 report（不执行里面的代码）
3. 执行 report(myfunc) → 进入 report 函数
4. 执行 print('我要开始调用函数啦。。')
5. 执行 func() → 这里 func = myfunc，所以跳去执行 myfunc()
6. 执行 myfunc 里的 print('正在调用myfunc函数。。。')
7. myfunc 执行完，回到 report 继续
8. 执行 print('函数已经调用完毕。')
9. report 执行完毕，程序结束
"""
print(
    '-----------------------------------------------------------------------------------------------------------------')
# 统计函数运行时间（时间管理大师）
import time


def time_master(func):
    print('程序开始运行...')
    start = time.time()
    func()
    stop = time.time()
    print('程序结束...')
    print(f'本程序一个运行了{(stop - start):.5f}秒。')


def myfunc():
    time.sleep(2)
    print('hello python')


time_master(myfunc)
"""
程序开始运行...
hello python
程序结束...
本程序一个运行了2.01秒。
"""

# 看看使用了装饰器的情况：
import time


def time_master(func):
    def call_func():
        print('开始运行程序...')
        start = time.time()
        func()
        stop = time.time()
        print('程序结束')
        print(f'一共消耗{(stop - start):5f}秒。')

    return call_func


@time_master
def myfunc():
    time.sleep(2)
    print('I love python')


myfunc()

# 输出结果：
# 开始运行程序...
# I love python
# 程序结束
# 一共消耗2.01秒。

"""装饰器：可以不更改原来的代码（函数）的情况下，调用函数。
装饰器可以在不修改原函数代码的情况下，扩展或增强函数的功能。
核心要点：
不改动原函数 - 保持原函数代码不变
添加额外功能 - 如日志、计时、权限检查等
透明调用 - 调用方式不变，但执行了增强后的逻辑
典型应用场景：
性能监控（如你文件中的计时）
日志记录
权限验证
缓存机制
异常处理
本质： 装饰器 = 高阶函数(用函数当参数） + 闭包，用 @ 语法糖简化调用
"""


# 装饰器的语法糖
def time_master(func):
    def call_func():
        print('开始运行程序...')
        start = time.time()
        func()
        stop = time.time()
        print('程序结束')
        print(f'一共消耗{(stop - start):5f}秒。')

    return call_func


def myfunc():
    time.sleep(2)
    print('I love python')


myfunc = time_master(myfunc)  # --> 返回内部的 call_func，把call_func赋值给了myfunc.
myfunc()

"""
语法糖（Syntactic Sugar）：
让代码更易读、更简洁的语法特性，底层功能不变。

以装饰器为例：
不用语法糖（繁琐）：
myfunc = time_master(myfunc)
myfunc()

用语法糖 @（简洁）：
@time_master
def myfunc():
    ...
    
myfunc()


本质： @time_master = myfunc = time_master(myfunc) 的简写
其他语法糖例子：
a += 1 是 a = a + 1 的语法糖
列表推导式 [x for x in range(10)] 是 for 循环的语法糖
作用：
减少样板代码
提高可读性
不改变程序逻辑

易用，简洁，可读，便捷
"""


# 多个装饰器用在同一个函数上
def add(func):
    def inner():
        x = func()
        return x + 1

    return inner


def cube(func):
    def inner():
        x = func()
        return x * x * x

    return inner


def square(func):
    def inner():
        x = func()
        return x * x

    return inner


@add
@cube
@square
def test():
    return 2


print(test())  # --->65
# 调用顺序：square-->cube-->add  2 --> 2*2=4 --> 4的立方=64 --> 64+1=65


# 如何给装饰器传递参数？
import time


def logger(msg):
    def time_master(func):
        def call_func():
            start = time.time()
            func()
            stop = time.time()
            print(f"[{msg}]一共耗费了{(stop - start):5f}")

        return call_func

    return time_master


@logger(msg="A")
def funA():
    time.sleep(1)
    print('正在调用funA....')


@logger(msg="B")
def funB():
    time.sleep(1)
    print('正在调用funB....')


funA()
funB()
"""
正在调用funA....
[A]一共耗费了1.000932
正在调用funB....
[B]一共耗费了1.000967

这是用了语法糖的代码
"""


# 不使用语法糖，原本的样子：
def logger(msg):
    def time_master(func):
        def call_func():
            start = time.time()
            func()
            stop = time.time()
            print(f"[{msg}]一共耗费了{(stop - start):5f}")

        return call_func

    return time_master


def funA():
    time.sleep(1)
    print('正在调用funA....')


def funB():
    time.sleep(1)
    print('正在调用funB....')


funA = logger(msg="A")(funA)  # 第一次调用，把参数扔进去，第二次调用把函数扔进去。
funB = logger(msg="B")(funB)

# 添加了一次调用，把参数扔进去，把函数扔进去。

funA()
funB()
# 输出结果：正在调用funA....
# [A]一共耗费了1.000292
# 正在调用funB....
# [B]一共耗费了1.000935
