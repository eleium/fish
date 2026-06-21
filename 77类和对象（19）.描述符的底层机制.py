# 函数和方法就是同一个东西，实现了实例绑定的函数，就是方法。没有被对象绑定的，就是一个普通的函数


class C:
    def fanc(self, x):
        return x


c = C()
print(C.fanc)
# ---><function C.fanc at 0x000001BA014C9080> 函数function
print(c.fanc)
# ---><bound method C.fanc of <__main__.C object at 0x000001BA014A65D0>> 绑定的方法bound method

# python的底层是怎么知道C是函数，c是方法呢？ 答案是 描述符
# 当我们定义一个函数的时候，其实是定义了一个叫Function的类.


# 为支持方法的自动创建，函数会包括 __get__() 方法以便在属性访问期间绑定方法。
# 这意味着函数就是在通过实例进行点号查找期间返回所绑定方法的非数据描述器。
# 其运作方式是这样的：
"""
class Function:
    ...

    def __get__(self, obj, objtepy=None):
        "Simulate func_descr_get() in Objects/funcobject.c"
        if obj is None:
            return self
        return MethodType(self, obj)
"""

# 在官方文档中，有一个__get__(self,obj,objtype=None)的描述符（跟__get__(self,instance,owner)一样，同样的位置的含义相同）
# 不管叫obj还是instance,或者cls，都是被描述符拦截的属性所在的类的实例化对象。小c=C(),
# 第三个参数，owner，就是这个实例化对象的类。大C.
# 官方文档实现的是：


class D:
    def __get__(self, instance, owner):
        if instance is None:
            print("函数")
        else:
            print("方法")


class C:
    x = D()


c = C()
c.x
# --->方法
C.x
# --->函数


# c.x 触发的是 instance=c（非 None），所以打印"方法"。因为确实定义了一个实例化对象c,所以instance!=None.
# 准确的说法是： c 这个实例本身没有属于自己的 x 属性，但 Python 在查找 c.x 时，向上寻找，成功地在它所属的类 C 中找到了 x，所以访问是成功的。
# c 没有自己的 x 属性，但它继承/访问到了来自类 C 的 x 属性
# c.x 能触发 __get__ 并打印“方法”，不是因为 c 自己有 x，而是因为 c 在它的类 C 中找到了 x，并且这个 C.x 恰好是一个描述符。
# 所以触发__get__,并且因为instance!= None,--->print('方法')

# instance is None 确实表示：描述符是通过类（C.x）而不是通过实例（c.x）访问的。
# C.x 触发的是 instance=None，所以打印"函数"。
# class C:--> x=D() 它的意思是：“把 D() 创建出来的那个描述符对象，赋值给类 C 的属性 x”。

# c.x的意思就是：调用/访问实例 c 的属性 x
# instance： 实例  owner:拥有者


## 文档中 return MethonType(self,obj) MethodType类是啥呢？：

"""
class MethodType:
    "Emulate PyMethon_Type in Objects/classobjict.c"
    def __init__(self,func,obj):
        self.__func__=func
        self.__self__=obj

    def __call__(self,*args,**kwargs):
        func=self.__func__
        obj=self.__self__
        return func(obj,*args,**kwargs)
"""
# 当MethodType类的实例化对象被当作函数调用的时候，__call__(self,*args,**kwargs)魔法方法就被触发。
# __call__(self,*args,**kwargs)的作用：將传递进来的两个参数func 和obj进行整合，并返回：
# 将传递进来的第一个实参变成函数名func,然后第二个传进来的实参当作这个函数的第一个参数obj,最后整合之后就返回。
# 通过描述符，很容易把函数绑定为方法。


# 这个 __call__ 的作用是：
# 当你“调用”一个 MethodType 的实例时（比如 method_obj()），Python 会自动执行 __call__ 里的代码：
# 取出之前存好的函数 func 和实例对象 obj
# 把 obj 作为第一个参数，连同调用时传进来的其他参数 *args 和 **kwargs，一起传给 func
# 返回 func 的执行结果
# 这就是 Python 内部实现“方法绑定”的核心机制。
# 当你写 c.method 时，Python 内部就是创建一个类似 MethodType 的对象，当你写 c.method() 调用它时，触发的是这个 __call__。


# 在 __get__(self, instance, owner) 中：
# 参数	         指向	                      是谁
# self	        描述符对象本身	              类 D 的实例
# instance	    被访问的属性所属的实例	       类 C 的实例（如 c），如果没有则为 None
# owner	        被访问的属性所属的类	       类 C 本身

print("-" * 88)

# 静态方法：可以放到类里面去，不需要绑定类和对象。


class C:
    @staticmethod
    def func():
        print("I love python")


c = C()
c.func()
# -->I love python
C.func()
# --->I love python

# 静态方法是怎么样实现的呢？
"""
class StaticMethod:
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

    def __init__(self,f):
        self.f=f
        functools.update_wrapper(self,f)

    def __get__(self,obj,objtype=None):
        return self.f

    def __call__(self,*args,**kwds):
        return self.f(*args,**kwds)
"""
# 只要被@StaticMethod装饰器装饰的函数，就会变成StaticMethon类的对象。
# 当这个函数被当作对象调用的时候，就直接调用传递进来的函数本身


"""
class ClassMethod:
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self,f):
        self.f=f
        functools.update_wrapper(self,f)

    def __get__(self,obj,cls=None):
        if cls is None:
            cls=type(obj)

        #被__get__()拦截的，传递进来的函数，通过__get__()的cls参数转化为type(obj),是类，是传递进来的属性的所属的类，即那个owner。
        if hasattr(type(self.f),'__get__'): 
            #This code path was added in python 3.9
            #and was deprecated in Python 3.11.
           #hasattr()是为了让类方法和其他装饰器串联起来用，才加入的。先@classmethod,紧接着@property,然后是对应的函数。

            return self.f.__get__(cls,cls)
        #将152行的这个类，调整为新函数的第一个参数.  类函数绑定的是类，而非对象。这是类函数的定义。
        return MethodType(self.f,cls)
        """

# staticmethod静态方法 和 classmethod类方法 都是装饰器，用来定义不需要实例化就能调用的方法。


# 以前用type()函数来判断对象的类型，返回对象所属的类。
# 类函数绑定的是类，而非对象。
class C:
    def func(self, x):
        return x


c = C()
print(c.func)
# ---> <bound method C.func of <__main__.C object at 0x000002C0C3676E70>>
# 这是一个绑定方法，它绑定到了类 C 的一个具体实例（内存地址 0x...）上，调用时会自动把这个实例作为第一个参数（self）传进去。
print(C.func)
# ----><function C.func at 0x0000018AFFB49260>


class C:
    pass


c = C()
print(type(c) is C)
# -->True 说明对象就是类C
# 如果传入一个对象当作参数，那么它得到的就是这个对象所属的类。


# hasattr()的作用是把方法（staticmethon或classmethod)和装饰器（比如@property)串联起来用。
# 那么，什么情况下需要串联使用呢？
class C:
    @classmethod
    # @classmethod 的作用是把方法绑定到类而不是实例，调用时自动把类本身**作为第一个参数（cls）传进去。
    # 类的属性不会自动匹配方法的参数。cls 只是一个“占位符”或“通道”，它让你能在这个方法内部拿到类本身，然后手动去调用这个类（cls(...)）来创建实例。
    # classmethod类方法的作用，把传递进来的属性所在的类，当作方法的第一个参数。
    # 下面实例化了一个类C的对象小c，小c进行c.__doc__操作的时候触发classmethod,就把小c所在的类C当作第一个参数传进__doc__(cls)，也就是cls==C

    # cls 的作用是什么？
    # 它的作用就是：让你可以在这个方法内部使用这个类。
    # 1，创建实例：cls(name, age) → 调用 Person.__init__
    # 2，访问类属性：cls.total_count
    # 3，调用其他类方法：cls.some_other_classmethod()

    def __doc__(cls):
        return f"I love python---from class {cls.__name__}"
        # cls.__name__ 是固定写法，不能用 cls.name 代替。
        # __name__ 是 Python 给每个类自动添加的内置属性，不需要你定义，直接就能用。
        # cls.name 会被 Python 解释为“去类里找一个叫 name 的属性”，这个属性默认不存在，所以报错。
        # 类似的还有： __module__类定义所在的模块名，__base__：父类组成的元组。等等。


c = C()
print(c.__doc__)
# 访问的c的属性，返回的是它所属的类
# ---><bound method C.__doc__ of <class '__main__.C'>>
print(c.__doc__())
# 访问的是c的方法：得到执行的结果：
# -->I love python---from class C

# 没有括号，是查阅类C的属性，看看类C是个啥。有括号，是调用类C的方法，要去执行的。


# 现在希望添加属性访问的方式，即不使用访问函数的形式，__doc__()是个属性的方式，要得到相同的结果，how?
class D:
    @classmethod
    @property
    def __doc__(cls):
        return f"I love python ---from class{cls.__name__}"


d = D()
print(d.__doc__)
# 这是直接访问的d的属性
# --->I love python ---from classD

print(D.__doc__)
# --->I love python ---from classD
# __doc__是python 内置的特殊属性
# Python 的文档字符串机制会主动调用 __doc__ 属性（如果它是一个可调用对象），把返回值作为文档字符串。

# 之前写的 @classmethod @property 配合 __doc__ 确实生效了。
# 它不是传统意义上的文档字符串，而是 Python 在读取 D.__doc__ 时，发现它是一个可调用对象，就自动调用了它来获取文档字符串。

# @property 的本意是：把方法变成实例属性，通过实例访问时触发

# @classmethod 的本意是：把方法变成类方法，通过类访问时触发


# 可以这样理解MethodType：

# MethodType(func, instance)：就像一份“劳动合同”，把 func（员工）和 instance（公司）绑在一起。签了合同后，func 就知道自己是为谁（self）在工作了。
# 如果方法是在类内部定义的，Python 解释器会自动帮你完成这个绑定过程。因此，你平时几乎不需要直接使用 MethodType，但它是理解 Python 动态特性的基石。
print("-" * 88)


class MethodType:
    """MethodType：绑定的“胶水”
    MethodType 是在 types 模块中定义的一个类型，你可以通过 from types import MethodType 来使用它。
    它的核心作用就是创建一个“绑定方法”对象。当你定义一个类和一个实例方法时，Python 内部就是使用 MethodType 来把函数 func 和实例 self 绑定在一起的。"""

    def __init__(self, func, obj):
        self.__func__ = func
        self.__self__ = obj

        # 是 Python 在方法对象（method object） 中定义的标准属性。
        # 当你创建一个绑定方法时，Python 内部会把原始函数和实例分别存在 __func__ 和 __self__ 这两个特殊属性里。

    def __call__(self, *args, **kwargs):
        func = self.__func__
        obj = self.__self__
        print("小白")
        return func(obj, *args, **kwargs)


class ClassMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        if cls is None:
            print("旺财")
            cls = type(obj)
        if hasattr(type(self.f), "__get__"):
            # hasattr 是 Python 的一个内置函数（BIF），用于判断一个对象是否有指定的属性或方法。
            # 调用方法前检查是否存在（避免报错）,判断对象type(self.f),到底有没有__get__()方法。

            print(f"来福，type(self.f)-->{type(self.f)}")
            return self.f.__get__(cls, cls)
        return MethodType(self.f, cls)


class D:
    @ClassMethod
    @property
    def __doc__(cls):
        return f"I love python--->from class {cls.__name__}"


d = D()
print(d.__doc__)
# ---> 来福，type(self.f)--><class 'property'>
# I love python--->from class D

# 如果是多个装饰器串联的情况，type(self.f),也就是传入这个参数的类，就是property

# 当多个装饰器装饰同一个对象的时候，它们的顺序是从下往上执行的
# @property函数先对__doc__(cls)函数进行改造，相当于： __doc__=property(__doc__),变成了一个properyt对象。__doc__就是property的一个实例对象

# 然后到@ClassMethod了：因为ClassMethod有hasattr分支，要进行 判断对象type(self.f),也就是property类,是否有__get__方法。
# property类有__get__方法，并调用这个方法，最后把应该指向instance的位置的参数，改成了cls。


class D:
    @ClassMethod
    # 把@property装饰器去掉，看看是什么效果
    def __doc__(cls):
        return f"I love python--->from class {cls.__name__}"


d = D()
print(d.__doc__)
# --->来福，type(self.f)--><class 'function'>
# <bound method D.__doc__ of <class '__main__.D'>>

# python中，函数也是对象。所以type(self.f),就是<class 'function'>的类。


"""

函数和方法如出一辙，实现对象绑定的函数叫方法，没有实现绑定的是普通的函数。
本节基于对官方文档的解读，探究了函数、方法、静态方法、类方法的底层实现原理，“知其所以然”。
Python底层通过描述符来辨别函数和方法，函数是一个非数据描述符，利用__get__()方法进行鉴别，
instance参数为None的是函数，不为None的是方法。
静态方法是StaticMethod类的对象，作为函数调用时直接调用传递进来的函数自身，故无需绑定类和对象；
类方法是ClassMethod类的对象，将参数klass即owner调整为新函数的第一个参数，以此来绑定类。
Python3.9还引入了串联装饰器的功能，仅通过访问属性便可得到与访问方法相同的结果，由新增的hasattr()条件分支来实现。
"""
