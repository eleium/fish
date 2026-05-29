# __call__()magic method.  调用对象魔法方法
# 对象里既可以有属性，也可以有方法。python可以像调用函数一样，调用对象，要求这个对象的类，定义一个 __call__()magic method.


class C:
    def __call__(self):
        print("Hi~~")


c = C()
c()
# --->Hi~~~

# __call__()支持位置参数和关键字参数


class C:
    def __call__(self, *arg, **kwarg):
        # 单星arg是位置参数，双星arg是关键字参数
        print(f"位置参数是->{arg}\n关键字参数是->{kwarg}")


c = C()
c(1, 2, 3, x=250, y=520)
# --->位置参数是->(1, 2, 3)
# --->关键字参数是->{'x': 250, 'y': 520}

# *arg位置参数是元组，而**kwarg关键字参数是字典
# 参数的固定位置：普通参数, *args, 默认参数(x=100), **kwargs
# 作用：让一个函数接收"不确定数量"的参数，
# 不需要预先知道有多少个参数
# 函数转发（A函数原样调用B函数，自己什么都不改）
# 场景：你写了一个包装函数，要把所有参数原封不动传给另一个函数


# 用__call__()的魔法方法，同样可以实现闭包的效果：


class Power:
    def __init__(self, exp):
        self.exp = exp
        # 定义指数

    def __call__(self, base):
        return base**self.exp
        # 没有self.base=base 将对象的属性保存，而直接用base,那么就只能用一次。而且也不能更改对象的self.base属性。


square = Power(2)
# 传入的是exp=3
print(square(3))
# --->9
# 传入的是base=3

cube = Power(3)
print(cube(3))
# --->27

# 上面的例子分两次传入了两个实参：一个在创建对象时传入，另一个在调用对象时传入，好处是：固定一个参数，灵活改变另一个


# __str__(sele)和__repr__(self) 跟字符串相关的魔法方法
# 与__str__(self)魔法方法有对用的str()函数一样，__repe__(self)魔法方法也有对应的repr()函数
# srt()和repr()函数的结果相同，都是一个字符串，但是设计的初衷不同：
# str()是将参数转化为字符串对象，是给人看的。
# repr()是将对象转换为程序可以执行的字符串，是给程序看的。


print(str(123))
# --->123
print(repr(123))
# --->123
# str() 和 repr() 永远返回字符串，你看到的"整数"只是 print() 去掉了引号，是visaulstudiocode 的显示策略。而在Idle中就会是： '123'.
# IDLE 和 VS Code 的显示差异不影响实际类型，都是字符串。
# 可以用type来验证：
print(type(str(123)))
# --->class 'str'

# 当输入的是字符串时：
print(str("hello"))
# --->hello
print(repr("hello"))
# --->'hello' 多了一对引号

# eval()函数的作用：将参数的引号去掉之后执行,eval() 不是"去掉引号"，而是"把字符串内容当作代码执行"
eval("1+2")
# --->3
# 字符串'1+2' 的内容1+2被当作代码执行了，1+2=3


# eval(str('hello'))
# --->NameError:name 'hello' is not defined.因为eval把'hello'的引号去掉了，变成了hello
# str('hello')--->'hello',eval('hello')--->eavl(hello),python找不到变量名hello,没有被命名过，所以报错。
# 但是如果把str换成repr，就是正确的了：

print(eval(repr("hello")))
# --->hello
# 因为repr（）多了一层引号，脱了一层，还有一层。 所以，可以说，eval()是repr()的反函数
# __repr__()可以对__str__()魔法方法代偿: 如果只定义了__repr__()方法，那么调用函数str()也是可以被响应到的


class C:
    def __repr__(self):
        return "I love Python"


c = C()
print(repr(c))
# --->I love Python
print(str(c))
# --->I love Python  类C里面并没有定义__str__()魔法方法，str()就去找__repr__()magic methon进行代偿
# 但是这是单方向的，如果反过来就不行啦：


class C:
    def __str__(self):
        return "I love Python,love visaulstudio code"


c = C()
print(str(c))
# --->I love Python,love visaulstudio code

print(repr(c))
# ---><__main__.C object at 0x0000020D65787830>

# __str__()魔法方法定义的，只能应用于 对象出现在打印操作的顶层，
# 如果把多个对象放在一个列表中，然后把该列表打印出来，就没办法访问到这个字符串啦。
cs = [C(), C(), C()]
# 多个实例化的对象，放到了一个列表中
for each in cs:
    print(each)
# --->I love Python,love visaulstudio code
#    I love Python,love visaulstudio code
#    I love Python,love visaulstudio code
# 单独迭代访问每一个单独的对象实例，都可以得到return的值：I love Python,love visaulstudio code
print(cs)  # 但是，当试图打印整个列表时：得到每个元素的地址，而不是return的值
# --->[<__main__.C object at 0x000002640A3F7A70>, <__main__.C object at 0x000002640A3F7EF0>, <__main__.C object at 0x000002640A3F7EC0>]


# 这是定义的__str__()魔法方法，如果定义的是__repr__()magic method，就没有这个困扰啦：
class C:
    def __repr__(self):
        return "I love Python"


cs = [C(), C(), C()]
for each in cs:
    print(each)
# --->I love Python
#    I love Python
#    I love Python

print(cs)
# --->[I love Python, I love Python, I love Python]

# __repr__()magic method 的适用场景更多，用起来也更稳。
# 不过，在同时定义__repr__()和__str__()方法的时候，可以让对象在不同的场景下，实现不同的显示效果

class C:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"data={self.data}"

    def __repr__(self):
        return f"c({self.data})"

    def __add__(self, other):
        self.data += other


c = C(250)
print(c)
# --->data=250  这是直接打印的场景，得到data=250，调用的是__str__()，得到return :data={self.data}
c
#--->C(250)    这是直接访问的方式，得到C(250),调用的是__repr__(),得到是 return : c({self.data})

c + 250
print(c)    #用两种魔法方法做加法，打印的效果依然会遵循每一种魔法方法定义的返回值
# --->data=500
c
#--->C(500)


"""
重要结论
情况	                     print(obj)	         str(obj)	           repr(obj)	    交互式直接输入 obj
有 __str__ 和 __repr__	    __str__           	__str__	               __repr__	        __repr__
只有 __str__	            __str__	            __str__	              默认 __repr__   	默认 __repr__
只有 __repr__	           __repr__（备选）    	__repr__（备选）	    __repr__	      __repr__
都没有	                    默认 __repr__	    默认 __repr__	       默认 __repr__	    默认 __repr__
可以看出，__repr__()是兜底方案。
而容器显示总是用 __repr__。比如上面的多个对象的例子： cs=[C(),C(),C()]--->[__main__.C object at ... , __main__.C object at ...,__main.C object at ...]
"""
