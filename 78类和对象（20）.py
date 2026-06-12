# 类装饰器：把类当作参数传入一个函数
# 装饰器：把函数当参数传入另一个函数

# @deco装饰器
# def foo():
# pass
# 等价于：foo = deco(foo)

# @deco类装饰器
# class C:
# pass
# 等价于：C = deco(C)

# 装饰器就是一个函数，它接收一个对象（函数或类），然后返回另一个对象。
# @deco 只是语法糖，自动帮你完成“被装饰的东西 = deco(被装饰的东西)”这个赋值操作。

# 有语法糖的时候，用@表明装饰器的身份；
# @deco
# def foo():
# pass

# 没有语法糖的时候，装饰器就是一个普通函数调用，手动完成“把函数/类传给装饰器，然后把返回值赋值回去”这个操作。
# def foo():
# pass
# foo = deco(foo)

# @ 只是帮你省了一行赋值代码
# @deco 这个写法，本质上就是 Python 替你做了两件事：
# 正常定义后面的函数/类（比如 def foo 或 class C）
# 自动执行 foo = deco(foo) 或 C = deco(C)
# 没有 @，你就自己写这一行赋值。


# 装饰器可以拦截函数的调用，就是装饰。装饰器也可以作用到类上面。：


def report(cls):
    def oncall(*args, **kwargs):
        print("hi,我要开始实例化对象啦。。。")
        _ = cls(*args, **kwargs)
        print("hi，实例化完成了。")
        return _

    return oncall


@report
# 把自定义的函数report()变成装饰器，来装饰下面的类：
# 装饰类的结果通常是：当你用这个类创建实例时，会先经过装饰器的处理。
class C:
    pass


# 经过装饰，其实相当于：
# C = report(C)    把类 C 作为参数传给 report 函数，然后把返回值重新赋值给 C

c = C()
# --->hi,我要开始实例化对象啦。。。
# --->hi，实例化完成了。

# 当执行 c = C() 时：
# C 现在指向 oncall 函数
# 调用 oncall()
# 打印 "hi,我要开始实例化对象啦。。。"
# 执行 _ = cls(*args, **kwargs)，这里的 cls 是原来的类 C（被装饰前那个空的类），所以 cls() 创建了一个实例
# 打印 "hi，实例化完成了。"
# 返回这个实例，赋值给 c

# 如果类C不是空的，有构造函数的话，上面的_=cls(*args,**kwargs):的参数就起作用了：


@report
# 用函数装饰下面的类
class C:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print("构造函数被调用了~~")


c = C(1, 2, 3)
# --->hi,我要开始实例化对象啦。。。
# --->构造函数被调用了~~
# --->hi，实例化完成了。

# 程序执行流程：
# 1，因为有@report,把开始的report()函数装饰化了，也就是语法糖了，所以c=report(C)
# 2,c=C(1,2,3) 实例化对象开始执行，就执行：oncall(),参数*args收集类C的参数，打包成一个元组(1，2，3)，**kwargs不动。
# 3，执行打印   "hi,我要开始实例化啦"
# 4,赋值临时变量_=cls(*args,**kwargs),也就是_=C(1,2,3),把刚才的元组给解包了。用了一个 * 号。

# _=cls(),由于内层的函数oncall使用了外层函数report(cls)的参数cls，并且return _,也就记住了cls，所以这就是一个闭包操作。

# args = (1, 2, 3)           元组
# cls(*args)                 *args 把 (1,2,3) 解包成 1,2,3 三个参数   * 号的作用就是解包
# 闭包的定义：一个函数（内层函数）记住了它外部作用域（外层函数）的变量，即使外层函数已经执行完毕。
#   _ = cls(*args, **kwargs)   # ← oncall 内部使用了外层函数的 cls，外层函数就是report(cls)

# 调用了类C,所以就打印了'构造函数被调用了~~~'.
# 5,接着执行print('hi，实例化完成了。')
# 6,返回临时变量，创建了一个实例化对象： _=C((1,2,3),**kwargs),否则就是None了。
# 7,返回oncall，也就是返回这个实例化对象。这个实例化的对象是谁呢？是c


# // 精确的注释：

## 阶段1：装饰器执行（在定义类时发生，不是在实例化时）
# @report          # 触发：C = report(C)
# class C:         # 先定义原来的类 C（包含 __init__）
# def __init__(self, x, y, z):
# ...

# 步骤1.1： Python 先正常定义类 C（原来的类，有 __init__）
# 步骤1.2： 执行 C = report(C)
# 调用 report 函数，传入原来的类 C 作为参数 cls
# report 内部定义了 oncall 函数（此时 oncall 记住了 cls，形成闭包）
# report 返回 oncall
# 现在名字 C 不再指向原来的类，而是指向 oncall 函数
# # 阶段2：实例化（c = C(1,2,3) 时发生）
# F = C(1, 2, 3)
# 步骤2.1： C(1,2,3) 调用的是 oncall(1,2,3)
# 步骤2.2： 进入 oncall：
# args = (1, 2, 3)（打包）
# kwargs = {}
# 打印 'hi,我要开始实例化对象啦。。。'
# 步骤2.3： 执行 _ = cls(*args, **kwargs)
# cls 是原来的类 C（闭包记住的）
# *args 解包成 1, 2, 3
# 等效于 _ = C(1, 2, 3)
# 调用原来的构造函数，打印 '构造函数被调用了'
# 创建一个实例，赋值给 _
# 步骤2.4： 打印 'hi，实例化完成了。'
# 步骤2.5： return _，把实例返回
# 步骤2.6： 调用方 c 接收到这个实例
# //

# 上面例子是用函数当装饰器，装饰类。下面用类当作装饰器，来装饰函数：

print("%" * 88)

"""
__call__ 的作用是：让实例对象可以像函数一样被调用。
当你写 obj() 时，Python 会自动执行 obj.__call__()。
在 Python 中，() 就是“调用”的语法。只要一个对象后面加上 ()，Python 就会尝试去“执行”它。


不带参数
class Greeting:
    def __call__(self):
        print("Hello!")

g = Greeting()
g()  # Hello!


2. 带固定参数
class Multiplier:
    def __call__(self, x, y):
        return x * y

m = Multiplier()
print(m(3, 5))  # 15


3. 带任意参数（使用 *args, **kwargs）
class Logger:
    def __call__(self, *args, **kwargs):
        print(f"位置参数: {args}")
        print(f"关键字参数: {kwargs}")

log = Logger()
log(1, 2, 3, name="Tom", age=20)

输出：
位置参数: (1, 2, 3)
关键字参数: {'name': 'Tom', 'age': 20}
"""


class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):

        self.count += 1
        print(f"已经被调用了{self.count}次了")


c = Counter()
c()
# --->已经被调用了1次了

c()
# --->已经被调用了2次了


# 下面，实现用类当装饰器，来装饰一个函数：
class Counter:
    def __init__(self, func):
        # 要装饰一个函数，就要先把这个函数当作参数传递进来，使得让装饰器生效的的时候可以获取这个函数
        # 装饰器生效，就是实例化一个对象
        self.count = 0
        self.func = func
        # 传入函数到构造函数的self.func属性里面去。

    def __call__(self, *args, **kwargs):

        self.count += 1
        print(f"say_hi已经被调用了{self.count}次了")
        return self.func(*args, **kwargs)


@Counter
def say_hi():
    print("hi~~~")


# 装饰器的作用:  @counter-->say_hi=Counter(say_hi)
# 此时，创建了类Counter的实例化对象Counter(say_hi),并将这个实例化对象起名叫say_hi.

# 同时，把定义的say_hi()函数，传递给类Counter的构造函数__init__(self,func)，当成构造函数的func参数，变成了类Counter的属性。
print(say_hi)
# ----><__main__.Counter object at 0x000002779CD87560>  类Counter的实例化对象，地址在0x00.......

say_hi()
# --->say_hi已经被调用了一次。 被调用的是刚才的实例化对象say_hi,不是say_hi()函数，因为已经被@Counter转化为实例化对象啦。
# ---hi~~~
# 此时，返回的say_hi=Counter(say_hi),已经变成了类Counter的一个实例化对象，而不是函数say_hi()了。可以被__call__()方法调用了。
# 因为__call__()的作用就是：把实例化对象当作函数一样调用。


print("-" * 88)


class Check:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        self.obj = self.cls(*args, **kwargs)
        return self

    def __getattr__(self, name):
        print(f"正在访问{name}")
        return getattr(self.obj, name)


@Check
class C:    #@CHeck -> say_hi=Check(say_hi)->__init__(say_hi,say_hi)->self.say_hi=say_hi
    def say_hi(self):
        print("hi~~")

    def say_hey(self):
        print("hey!!!!")


c = C()
c.say_hi  # 没有（）,表示只
# --->长在访问say_hi

c.sya_hi()
# --->正在访问say_hi
# --->hi~~~
