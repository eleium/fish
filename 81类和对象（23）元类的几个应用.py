# 元类metaclass在实际开发中，都能做哪些事情：
# 1,操作类，给所有的类添加作者的属性


class MetaC(type):
    def __new__(mcls, name, bases, attrs):
        attrs["author"] = "FishC"
        # 在 attrs 这个字典（它包含了正在被创建的类的所有属性）里，设置一个名为 'author' 的键，其值为 'FishC'。
        # 这样，所有通过 MetaC 创建的类（比如 C 和 D），都会自动拥有一个 author 类属性，值为 'FishC'。
        # 类C和类D创建的实例化对象就可调用这个属性了。
        return type.__new__(mcls, name, bases, attrs)


class C(metaclass=MetaC):
    pass


class D(metaclass=MetaC):
    pass


c = C()
d = D()
print(c.author)
# --->FishC

# __new__()和__init__()都是在类被定义后就实现的，元类创建了类对象。这个时候的类，就相当于元类的'实例化对象'.

# 类（元类）的 __new__ 和 __init__	在类被定义时执行（创建类对象）
# 普通类的 __new__ 和 __init__	在创建实例时执行（创建实例对象）

# __new__ 负责“盖房子”（创建空的实例对象），__init__ 负责“装修”（初始化实例属性）。
# 实例化对象时，永远先调用 __new__，再调用 __init__。你平时写 __init__ 就够了，除非你需要更底层的控制，才会动 __new__。


class MetaC(type):
    def __init__(cls, name, bases, attrs):
        cls.author = "FishC"
        # 给类，而不是元类MetaC，动态的创建一个属性，并赋值'FishC'。
        # __init__ 方法不是“创造”实例的，它是在实例被创造出来之后，负责“初始化”它的。初始化就是给这个实例对象写入属性。
        # __new__ 负责创造，__init__ 负责初始化
        return type.__init__(cls, name, bases, attrs)
        # 没必要用return，因为__init__()只是初始化实例对象，没有执行其他的，其实是None.而且，__init__()也只能返回None.

        # __init__ 的工作是修改 self，而不是创建 self。它已经拿到了一个活生生的实例对象（由 __new__ 造的），它只需要往里面填数据就行。
        # 既然是“装修”而不是“盖房子”，它自然不需要把房子“交出来”（return）。


class C(metaclass=MetaC):
    pass


class D(metaclass=MetaC):
    pass


c = C()
d = D()
print(c.author)
# --->FishC


# 2,元类可以做到事情：可以对类名的定义规范做限制
# 比如，可以让类的名字只支持大写字母开头


class MetaC(type):
    def __init__(cls, name, bases, attrs):
        if not name.istitle():
            raise TypeError("类名必须是大写字母开头!!!")
            type.__init__(cls, name, bases, attrs)
            # type.__init__()的意义是：调用父类（type）的初始化方法，完成“类对象”的基础构建工作。
            # 当你定义一个元类（MetaC）时，你是 type 的子类。当你用 MetaC 创建类（C）时，MetaC.__init__ 会被调用。
            # 但 MetaC.__init__ 只关心自己新增的逻辑（比如检查类名）。至于：这个类的名字是什么？它的父类是谁？它有哪些方法和属性？
            # 这些基础工作，还是需要交给 type.__init__ 去完成的。
            # 如果你不调用它，Python 的内置类初始化逻辑就不会执行，类对象可能会缺失 __module__、__doc__、__dict__ 等基础属性。
            # 类似的，普通类必须要调用super().__init__()一样，元类的 __init__ 里也必须调用 type.__init__()，否则父类（type）的核心初始化就不会执行。


# class d(metaclass=MetaC):
# pass
# --->TypeError: 类名必须是大写字母开头!!! 报错，所以赶紧把类的名字首字母改成大写：
class D(metaclass=MetaC):
    pass


print("- -" * 40)

# 3，元类的第三个重要用法：修改对象的属性值。比如，把对象的所有的字符串属性值修改为大写：


class MetaC(type):
    def __call__(cls, *args, **kwargs):
        new_args = [each.upper() for each in args if isinstance(each, str)]

        """
        这个列表推导式相当于：
        new_args = []                          # 1. 先创建一个空列表
        for each in args:                      # 2. 遍历 args 里的每一个元素
            if isinstance(each, str):          # 3. 如果这个元素是字符串
                new_args.append(each.upper())  # 4. 把它转成大写，放入新列表

            这是一个非常经典的 “过滤 + 转换” 的操作：
                过滤：if isinstance(each, str) 只筛选出字符串类型的元素。
                转换：each.upper() 把选中的字符串全部转为大写。
                收集：把转换后的结果放入新列表 new_args。
                """

        return type.__call__(cls, new_args, **kwargs)


class C(metaclass=MetaC):
    def __init__(self, name):
        self.name = name


c = C("pyhton")
print(c.name)
# --->['PYTHON']
# 这里出现的结果是一个列表，因为元类返回的是type.__call__(cls,new_args,**kwargs),而new_args=[列表推导式]，所以是列表。
# 如果不想出现列表，而要一个字符串，就要给new_args加一个星号*，即*new_args,表示给这个变量解包成位置参数，得到一个字符串

# 4,限制类实例化时传递参数的方式，比如说，可以要求实例化对象创建的时候，只能通过关键字参数传参。如果是位置参数传参，就报错：


class MetaC(type):
    def __call__(cls, *args, **kwargs):
        # 干预类实例化的过程，就定义__call__()magic method
        if args:
            raise TypeError("不能用位置参数传参")
        return type.__call__(cls, *args, **kwargs)
        # 只要一个方法被当成“调用”来使用，它就必须把调用结果返回给调用者。
        # 实例化类（C()）本质上就是一次“调用”，而这个调用的结果应该是一个实例对象，而不是 None。所以必须要有return

        # __new__()和__call__()方法都必须有return,因为这两个方法都必须有执行结果。
        # 而__init__()是初始化对象的属性，可以没有return，即使用了return，返回的也是None.


class C(metaclass=MetaC):
    def __init__(self, name):
        self.name = name


# c=C('jack')
# c.name
# --->TypeError:不能用位置参数传参

c = C(name="jack")
print(c.name)
# --->jack


# 5,禁止类实例化，利用元类，可以禁止类实例化：
class NoInstances(type):  # NOInstances:没有实例
    def __call__(cls, *args, **kwargs):
        raise TypeError("不允许实例化对象")


# class C(metaclass=NoInstances):
# pass


# c = C()
# ---->TypeError: 不允许实例化对象


print("- 0" * 40)
# 没有实例化的对象，怎么访问类呢？用静态方法：


class C(metaclass=NoInstances):
    @staticmethod
    def static_ok():
        print("用静态方法，可以实现类的访问")


print(C.static_ok())
# ---->用静态方法，可以实现类的访问

# 用类方法classmethod的方法也可以访问类：


class D(metaclass=NoInstances):
    @classmethod
    def classmethod_ok(cls):
        # 类方法必须传入一个类，cls
        print("用类方法的方法，也可以访问类，不需要实例化对象")


D.classmethod_ok()
# --->用类方法的方法，也可以访问类，不需要实例化对象


print("-- --" * 40)

# 6,利用元类，只允许类有一个实例化对象


class SimpleInstance(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        # 创建一个类的属性，是私有变量。name margling 技术。用__两个下划线，私有变量，起到隐藏的效果
        # cls.__instance=None就是创建一个属性值是None的属性,
        # 注意，这个属性是SimpleInstance元类创建的类的实例对象的。
        # 如果不用__instance,设置成私有变量，那么类属性 instance 是公开的，外部可以随意修改它，破坏单例模式的约束

        # cls.__instance = None 这行代码，确实就是给 cls 这个类对象添加一个名为 _SimpleInstance__instance 的属性，并将其值设为 None。

        """
        这里的 cls 是元类 SimpleInstance 的 __init__ 方法的参数。
        当 Python 定义一个类（比如 class C(metaclass=SimpleInstance):）时，SimpleInstance.__init__ 会被调用，
        这个 cls 参数指的就是“正在被创建的那个类”（比如类 C）。
        所以，这行代码不是在给元类 SimpleInstance 自己加属性，而是给所有用 SimpleInstance 作为元类的类（比如 C）加一个类属性。

        为什么要在这里初始化为 None？
        这个元类设计的目标是实现单例模式（确保一个类只有一个实例）。
        它需要一个地方来存储“唯一的那个实例”。最合适的地方就是类本身。在类被创建时，先把 __instance 设置为 None（表示“目前还没有实例”），之后在 __call__ 方法中，会检查这个属性：
        如果它是 None，说明还没有实例，就创建一个并保存。
        如果它不是 None，说明已经有实例了，就直接返回它
        """

        # 如果值不是 None，而是 500 或 'python'，那么这个类属性就被赋予了一个固定的初始值，而不是“空”的状态。
        # 但是也可以达到：只允许有一个实例的目的。只是这个实例的属性值被固定为500或'python'。
        # 类 C 一被定义，就有一个类属性 __instance，值为 500。
        # 这个属性不属于任何实例，只属于类本身。
        # 所有通过 C 创建的实例都可以访问到这个类属性（但不能直接访问 __instance，因为名称修饰）。

        type.__init__(cls, *args, **kwargs)
        # 不需要return

    def __call__(cls, *args, **kwargs):
        # 干预类的实例，一般都是在__call__里干预
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class C(metaclass=SimpleInstance):
    pass


c1 = C()
c2 = C()
print(c1 is c2)
# ---->True

print(dir(C))
# ---->['_SimpleInstance__instance', '__class__', '__delattr__', '__dict__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# 说明c1和c2是同一个对象，被保存在： '_SimpleInstance__instance'里面，类的被改变了名字的属性里面。
# 其实就是__instacne,由于name margling,名字改编技术，变成了_SimpleInstance__instance

print(c1.__class__)
# ----><class '__main__C'>
print(c1.__dict__)
# ---->{}  属性是空的
