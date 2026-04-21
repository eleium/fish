# 像 map,filter,reduce,min,max,salty 都是高阶函数,有一个key参数，接收的是函数。
# 高阶函数是函数式编程的灵魂。python专门搞了一个模块：functools。
"""高阶函数：能接收函数当参数 / 能返回函数的函数
高阶函数（Higher-order Function）
特征：函数接收另一个函数作为参数，或返回一个函数
例子：time_master(func) 接收 func 参数 → 高阶函数

# 闭包：内层函数记住外层函数变量的一种现象 / 特性
闭包（Closure）
特征：内函数引用了外函数的变量，外函数返回内函数
例子：call_func() 引用了外层的 func，time_master 返回 call_func → 闭包


# 装饰器：专门用来给函数 “加功能” 的语法糖，本质 = 高阶函数 + 闭包
装饰器（Decorator）
特征：用闭包+高阶函数来"包装"原函数，不修改原代码的情况下增加功能
例子：myfunc = time_master(myfunc) 给 myfunc 加了计时功能 → 装饰器
"""

# reduce()：从左到右，每次拿两个数做运算，结果再和下一个数运算，直到只剩一个值。可以加减乘除，所有运算都可以。
import functools
# 导入整个模块。使用时模块名.方法名。


from functools import reduce


# 只导入模块中的reduce一共函数。直接用，不用加前缀模块名。

# 推荐第22行：代码更简洁，不用写 functools. 前缀
# 第21行适用场景：要用 functools 里多个函数时（比如 reduce、partial、wraps 等）


def add(a, b):
    return a + b


result = functools.reduce(add, [1, 2, 3, 4, 5])
print(result)
# reduce 的作用：将一个可迭代的对象，依次传入前面的add函数，最终得到15=1+2+3+4+5.
# 如果函数add的返回值是 retrur a*b,结果是：1*2*3*4*5=120
# reduce() 函数的参数是interable对象：元组，列表，字符串。


# 相当于下面的算式：
print(add(add(add(add(1, 2), 3), 4), 5))  # -->15

# 用lambda函数当第一个参数：
print(reduce(lambda a, b: a * b, [1, 2, 3, 4, 5]))  # --120
print(reduce(lambda a, b: a * b, range(1, 11)))  # -->3628800
"""reduce 的内部机制就是：
取前两个数运算
结果和下一个数运算
重复直到结束
你只负责定义"怎么算"（lambda），reduce 负责"怎么遍历和累积"。"""

# 偏函数：对指定的函数进行二次包装，通常是将现有函数的部分参数预先绑定，从而得到一共新的函数。新函数就叫偏函数。
# 就是将一共函数的多个参数拆分，多次传递：
#  partial（偏函数）来自 functools 模块。 作用：把原函数的某些参数"固定"，生成新函数
square = functools.partial(pow, exp=2)
# pow（幂运算函数）Python 内置函数，用法：pow(x, y) 计算 x 的 y 次方，等同于 x ** y
# exp（exponent，指数）pow 函数的参数名，pow(base, exp) → base 的 exp 次方。如果exp=3,就是求立方。4就是4次幂。
print(square(5))
"""
提问：
偏函数partial怎么绑定参数了？绑定的是pow函数的exp参数吗？
poe(exp)函数，调用时把exp固定为2？
回答：
对，**你理解完全正确**，我用最直白的话给你钉死这个概念：

# 一句话结论
```python
square = functools.partial(pow, exp=2)
```

意思就是：
**给 pow 函数预先绑定死 `exp=2`，
以后调用 square(x)，就等价于调用 pow(x, exp=2)**

也就是你说的：
**把参数固定成 2，以后不用再传。**

---

# 一步步拆开

## 1. 先看原函数 pow
Python 里的 `pow` 长这样：
```python
pow(base, exp)   # 计算 base^exp，也就是base的exp次幂。
```

比如：
```
pow(3, 2) → 9
pow(5, 2) → 25
```

## 2. partial 做了什么？
```python
square = partial(pow, exp=2)
```

它干了两件事：
1. 记住要调用的函数：**pow**
2. 预先把参数 **exp=2 固定死**

## 3. 所以现在 square 变成了一个“新函数”
只需要传**底数**就行：
```python
square(3)  # 等价 pow(3, exp=2) → 9
square(5)  # 等价 pow(5, exp=2) →25
```

完全就是你说的：
**把 exp 固定为 2，以后调用不用再写 exp=2**

---

# 用生活例子讲
- `pow` = 一台**次方计算器**
- `partial(pow, exp=2)` = 把机器上的**次方旋钮拧死在 2**
- `square` = 一台**专用平方机**

你只需要扔进去数字，它自动算平方。

---

# 超简总结
`functools.partial(函数, 参数=值)`
= **给函数预设参数，生成一个简化版新函数**

`square = partial(pow, exp=2)`
= **生成一个专门算平方的函数**
"""

"""
@warps:
`@functools.wraps` 就是**给装饰器“整容”用的**，一句话：
**让被装饰过的函数，还能保留自己原来的名字、文档、注释，不被内层函数覆盖。**

---

## 1. 先讲：不用 wraps 会出什么问题？
你写个普通装饰器：

def decorator(func):
    def wrapper():
        return func()
    return wrapper

@decorator
def f():
     我是函数f
    pass

然后你打印看看：

print(f.__name__)  # 输出：wrapper
print(f.__doc__)   # 输出：None

明明是 `f()`，结果**名字变成 wrapper**，**文档没了**。
这就叫**函数身份被偷换了**。



## 2. 加上 @wraps 就恢复正常

from functools import wraps

def decorator(func):
    @wraps(func)   # 就加这一行
    def wrapper():
        return func()
    return wrapper

@decorator
def f():
    我是函数f
    pass

print(f.__name__)  # f
print(f.__doc__)   # 我是函数f
```

作用：
- 保留原函数的 **__name__**
- 保留原函数的 **__doc__**（文档字符串）
- 保留原函数的 **参数签名、模块信息**
- 让别人调用、调试、序列化时，认得出这是谁

---

## 3. 超通俗理解
- 装饰器 = 给函数**穿外套**
- `wrapper` = 外套本身
- `@wraps(func)` = **在外套上贴原来的身份证**

不加 wraps：
别人一看：这是 `wrapper`，不知道原来是谁。

加了 wraps：
别人一看：虽然穿了外套，但**还是原来那个函数**。

---

## 4. 标准用法（固定模板）
所有写装饰器都建议这么写，**万能模板**：

from functools import wraps

def 装饰器名(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 做点额外事
        result = func(*args, **kwargs)
        # 再做点额外事
        return result
    return wrapper


---

## 5. 总结三句
1. @wraps 是装饰装饰器的装饰器
2. 作用：还原被装饰函数的真实身份
3. 只要写装饰器，建议都加上，避免调试、日志、框架报错"""

import time


def time_master(func):
    def call_func():
        print('start run program')
        start = time.time()
        func()
        stop = time.time()
        print('stop the program')
        print(f'耗时{(stop - start):.5f}秒')

    return call_func


@time_master
# 用了装饰器
def myfunc():
    time.sleep(2)


# myfunc = time_master(myfunc)
# 如果不用@time_master,就要这么写。
myfunc()

print(myfunc.__name__)  # --->call_func
# 调用myfunc()就是调用time_master()函数，就是调用call_func()函数。这就是闭包的作用。
"""
满足闭包三要素：
有外层函数 time_master
有内层函数 call_func
内层 call_func 用到了外层的 func，并且被返回出去
所以：
call_func 就是闭包函数
最终精炼成一句你能记住的
调用 myfunc () = 调用闭包 call_func ()

time_master(myfunc) 执行后，返回了 call_func 函数对象
myfunc 现在指向 call_func
调用 myfunc() 就是调用 call_func()
time_master 只在一开始执行一次（用来生成新函数），后面再也不参与了。

闭包的作用
让 call_func 能记住并使用外层的 func 变量（也就是原始的 myfunc）。
即使 time_master 已经执行完毕，call_func 依然能访问到它内部的 func。
总结：闭包 = 内函数"打包带走"了外函数的变量。
"""

# 用@wraps的情况：
import time
import functools


def time_master(func):
    @functools.wraps(func)
    # 在这里加上@functools.wraps(func)，来装饰装饰器，负负得正，得到原来的函数名。
    def call_func():
        print('start run program')
        start = time.time()
        func()
        stop = time.time()
        print('stop the program')
        print(f'耗时{(stop - start):.5f}秒')

    return call_func


# @time_master
# 用了装饰器
def myfunc():
    time.sleep(2)


myfunc = time_master(myfunc)
# 如果不用@time_master,就要这么写。
myfunc()

print(myfunc.__name__)  # --->myfunc  由于加了@functools.wraps(func), 所以被还原成原来的函数名。
