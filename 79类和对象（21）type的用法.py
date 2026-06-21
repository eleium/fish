# python 中的type()函数
# 当不知道一个对象的类型的时候，可以直接丢给typt()函数
print(type(250))
# ---><class 'int'>

print(type(4.34))
# ---><class 'float'>

print(int)
# ---><class 'int'>

print(type("python") is str)
# --->True

print(type(250)("520"))
# --->520  type(250)-->int,得到一个int类型。然后 int('520')-->520
print(type("hello")(3.14))
# --->'3.14'

print(type([])("pyhton"))
# --->['p','y','t','h','o','n']

print(type(())([1, 2, 3]))
# --->(1,2,3)

print(({}).fromkeys("pyhton"))
# --->{'p': None, 'y': None, 'h': None, 't': None, 'o': None, 'n': None}
# fromkeys 是 Python 字典（dict）的一个类方法，用于创建一个新字典，其中包含指定的键，并且所有键对应的初始值都相同。默认是None
# type对类也同样适用：


class C:
    def __init__(self, x):
        self.x = x


c = C(250)
print(type(c))
# ---><class '__main__.C> type(c)告诉你c是属于哪个类型，是哪个类创造的。返回的是那个类，即类C.
print(c)
# ----><__main__.C object at 0x00000....> 说明c就是类C的一个实例化对象

d = type(c)(520)
print(d)
# ---><__main__.C object at 0x0000....> type(c)--->C,返回的是类C,把C(520)赋值给变量d，d就变成了类C的一个实例了：d=C(520)

# 看一个对象的类型，也可以用class属性：
print(c.__class__)
# ---><class '__main__.C'>

# 以上说明，type能返回对象的类型。

print(type(C))
# ---><class 'type'>
print(type(type(C)))
# ---><class 'type'>

print("- -" * 88)

# type是python的奇点，python中万物皆对象。类也是对象，是type()生成的。
# type()根据函数的参数不同，有两种使用方法：
# 1，根据object的参数类型，返回值是一个type对象，此时相当于object.__class__返回的值
# 2，根据传入的三个参数，创建一个新的类型，也就是返回一个新的type对象,如下：

# type(name,base,dict,**kwargs)

# name:指定将要创造的类的名字，base:指定将要创造的类的父类，dict:指定将要创造的类的属性和方法，

# **kwargs:可选的收集参数。当且仅当被需要时，收集参数会被传递给适当的元类机制，通常是__init_subclass__().


# type(name, bases, dict) 的三个参数类型是固定的：
# 名字必须是字符串，标明是字符串，就要加上引号，否则就是一个变量。
# 父类必须是元组，单元素元组里面必须加上一个逗号，否则就是一个变量。
# 属性必须是字典。
# 这是 type() 函数的定义决定的，不是通用规则。普通函数传参没有这种限制。


class C:
    pass


C = type("C", (), {})
# 这两个C是等价的

c = C()
print(c.__class__)
# ---><class '__main__.C'>

print(C.__base__)
# ---><class 'object'>
# 用base属性查看类C的父类是类class

D = type("D", (C,), ({}))
# 直接实现了类的继承，因为第二个属性是元组，所以必须要有逗号
print(D.__class__)
print(type(D))
# ---><class 'type'> 上面两个写法都一样，表明D是type类
print(D.__base__)
# ---><class '__main__.C'>,表明D的父类是类C

# 第三个参数是字典，也就是键值对：

E = type("E", (), dict(x=250, y=500))
print(E.__base__)
# ---><class,'object'>，因为没有指定继承，默认为继承自object
print(E.__dict__)
# --->{'x': 250, 'y': 500,   自己设置的两个属性。
# 下面的都是python自带的，自动加载的属性，不可更改：
# '__module__': '__main__', 表明这个类来自哪里，如果你在交互式环境（REPL）里定义，就是 '__main__'；
# 如果你在某个 .py 文件里定义，比如 my_module.py，它就是 'my_module'，也就是文件名；
# 如果你把类定义在 utils.py 里，然后在 main.py 里导入它，__module__ 就是 'utils'，找到它的源头文件

# '__dict__': <attribute '__dict__' of 'E' objects>,
#  '__weakref__': <attribute '__weakref__' of 'E' objects>, '__doc__': None}

print("- -" * 40)

# 如何把函数放到第三个参数里。（先定义好函数，然后可以把函数名放到一个列表里.)


def funC(self, name="python"):
    # 因为是一个类的函数，准确的说是类的方法，最后要绑定对象的，所以要有self参数，
    # 所有定义在类里面的【实例方法】，都必须显式声明 self 作为第一个参数。
    # 但是，如果类没有实例化对象，就可以不要self参数。如果只有类的方法，第一个参数就是cls。
    print(f"hello!{name}")


F = type("F", (), dict(say_hi=funC))
f = F()

f.say_hi()
# --->hello!python
f.say_hi("二亮")
# --->hello!二亮
# 修正： f.say_hi('二亮') 是调用方法并传参，不是“给属性赋值”。把'二亮'传给funC,从而覆盖原来的name='python'为name='二亮'

# 执行f.say_hi('二亮')时，
# 1 Python 在 f 里找 say_hi	f 本身没有，向上找    因为 f=F()，里面没有say_hi方法
# 2	在 F 里找到 say_hi，指向 funC	找到了
# 3	Python 自动把 f 作为第一个参数（self）传进去	self = f
# 4	把 '二亮' 作为第二个参数传给 name	name = '二亮'

print(f.__dict__)
# --->{}  对象实例f，没有属性。所以那个'二亮'是传参,是调用say_hi方法后，给funC传参。如果是属性赋值应该这样：f.say_hi='二亮'
print(F.__dict__)

print("- -" * 40)

# __init_subclass__(),python3.6新添加的一个类方法。作用是加强父类对子类的管理


class C:
    def __init_subclass__(cls):
        # 这是一个类方法，必须绑定一个类。因此第一个参数是用来绑定类的
        print("你好世界")
        cls.x = 520
        # 类的x属性把它赋值为520


class D(C):
    x = 250


# --->你好世界  当定义完这个子类后，父类__init_subclass__()会立即被触发
print(D.x)
# --->520  虽然访问的是类D的x属性，但是返回的还是父类C的x属性值

# __init_subclass__()跟type()的第四个参数的关系：
# **kwargs:可选的收集参数。当且仅当被需要时，收集参数会被传递给适当的元类机制，通常是__init_subclass__().


# __init_subclass__()方法，除了第一个参数需要传递类之外，还可以传入其他的参数：
class C:
    def __init_subclass__(cls, value):
        print("我喜欢python")
        cls.x = value


class D(C, value=520):
    # 子类在继承父类的时候，写完父类，紧跟着就要写关键字参数
    x = 250


# --->我喜欢python  同样的被父类的__init_subclass__()拦截了
print(D.x)
# --->520

# 当用type()函数来构造，像类D这种继承了定义过__init_subclass__()的父类时，
# 如果需要给__init_sbuclass__()传递参数，比如需要传递value参数时，就可以通过第四个参数进行接力了。
D=type('D',(C,),dict(x=250),value=520)
#--->我喜欢python 立即触发了父类C的__init_subclass__()
print(D.x)
#--->520 虽然访问的是类D的x属性，但是还是优先返回的是父类C的x的属性。


# 关键点： __init_subclass__ 是在子类被定义时触发的，在子类的内容（x=250）被处理之后，但在子类被完全创建之前。
# 所以： 子类 D 里的 x=250 先被设置，然后被父类的 __init_subclass__ 覆盖成了 520。
# 这不是"返回父类的值"，而是子类自己的 x 属性被重新赋值了。

# __init_subclass__ 是 Python 官方提供的类钩子，在子类定义时自动触发，并且优先于子类内部的属性赋值。
# 所以 D.x = 250 先执行，然后被 cls.x = 520 覆盖了。这不是"返回父类的值"，而是"子类自己的属性被父类钩子覆盖了"。
# 实例的属性需要通过 __init__ 去定义，不会受到 __init_subclass__ 的影响。

# 官方文档规定：__init_subclass__ 是一个钩子方法，会在子类被定义时自动调用。
# 它的设计目的就是让父类在子类创建时有机会修改子类的行为（比如加属性、加装饰器、做校验等）。



#因为type(name,base,dict,**kwds)是收集参数，所以可以定义子类的时候，用多个参数

class C:
    def __init_subclass__(cls,value1,value2):
        print('我喜欢python啊~~~')
        cls.x=value1
        cls.y=value2

D=type('D',(C,),dict(x=250),value1=500,value2=800)
#--->我喜欢python啊~~~

print(D.x)
#--->500
print(D.y)
#--->800
