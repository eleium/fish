# 描述符：前面讲过的property()，静态方法，类方法，它们背后的实现技术都是依赖于 描述符
# 描述符协议：只要是实现了 __get__(),__set__(),__del__()三个方法的一个或多个的类，都叫做描述符
# 这三个方法都是用来拦截对象的 读取、写入和删除操作，但是它们管的不是自己属性，而是别人的属性


class D:
    def __get__(self, instance, owner):
        print(f"get~\nself->{self}\ninstance->{instance}\nowner->{owner}")

    def __set__(self, instance, value):
        print(f"set~\nself->{self}\ninstance->{instance}\nvalue->{value}")

    def __delete__(self, instance):
        print(f"delete~\nself->{self}\ninstance->{instance}")


# 这个类D就是描述符
# 在另一个类中，将类Ｄ的实例化对象赋值给要管理的类的属性就可以使用这个类Ｄ（描述符）啦。

# 为什么大家都用 instance 和 owner？
# 这是约定俗成的命名规范，不是语法强制要求。实际上可以是任意字符串：hello,python ,a,b等等。

# 就像 Python 社区约定用 self 作为实例方法的第一个参数一样，用 instance 和 owner 能让代码：
# 更易读：任何人看到代码立即明白参数的含义
# 更易维护：团队协作时不需要猜测参数用途
# 符合 PEP 8：Python 官方风格指南推荐有意义的参数名


class C:
    x = D()
    # 类C里面的属性，是类D的实例化对象


c = C()
c.x = 250
# set~
# self->    <__main__.D object at 0x000002A975FF6A80>
# instance-><__main__.C object at 0x000002A975FF6A20>
# value->250
# 就是__set__()方法被调用啦，就是赋值，就是写入。

# 当我们要读取的时候：
print(c.x)
# get~
# self->    <__main__.D object at 0x000001F3ABE36AB0>
# instance-><__main__.C object at 0x000001F3ABE36A50>
# owner->   <class '__main__.C'>
# None

del c.x
# delete~
# self-><__main__.D object at 0x00000249A0F56AE0>
# instance-><__main__.C object at 0x00000249A0F56A80>

# self参数对应的是描述符D对应的实例对象，也就是x的属性值：x=D()
# instance参数对应的是被描述符拦截的属性所在的类的实例对象，也就是类C的对象c
# owner参数对应的是被描述符拦截的属性所在的类<class '__main__.C'>

#  __get__(self, instance, owner)
# 这是最复杂也是参数最多的。三个参数含义固定：
# self：描述符实例本身。
# instance：拥有该描述符的那个类的实例。
# owner：拥有该描述符的那个类本身。
# 但有一个重要细节： 当你通过类而不是实例来访问属性时，instance 参数会是 None。


# 将下面的代码改成用描述符的方式：
class C:
    def __init__(self):
        self._x = 250

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx)


# __init__ 构造函数不是必需的。
# 什么时候可以不用 __init__？
# 1. 类不需要维护状态，不需要初始化任何属性
# 2. 使用类变量而非实例变量
# 3. 仅作为命名空间或工具类

# 什么时候必须使用 __init__？
# 当类需要初始化实例特有的属性时：

# 关于 __get__
# __get__ 是描述符协议的一部分，通常不需要 __init__


# __init__ 不是必需的 - 只有当实例需要个性化状态时才需要
# 描述符（__get__）可以独立存在
# 简单的工具类、混入类（Mixin）、抽象基类可能不需要 __init__

# 如果需要为每个实例设置不同的属性值，就必须使用 __init__
print("-" * 88)


class D:
    def __get__(self, instance, owner):
        return instance._x
        # instance:被描述符拦截的属性所在的类的实例化对象

    def __set__(self, instance, value):
        instance._x = value

    def __delete__(self, instance):
        del instance._x


class C:
    def __init__(self, x=250):
        # 通过一个属性 x 来间接的管理私有变量_x，那么默认的话可以写成： x=250
        self._x = x
        # 也就是：def __init__(self,x):--->self._x=250

    x = D()
    # 实例化一个对象x。这就是描述符。


c = C()
print(c.x)
# --->250
c.x = 520
print(c.__dict__)
# --->{'_x':520}
del c.x
print(c.__dict__)
# --->{}

# 跟用property()的效果一样。但是property()方法明显浅显易懂。
# 这种方法，在类D中访问类C的内部私有属性，显然不合理。为啥还用描述符呢？因为是现有描述符，再有property()属性的

# 这节课目的：如何用描述符造出自己的properyt()函数


class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class C:
    def __init__(self):
        self._x = 250

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = MyProperty(getx, setx, delx)
    # 这是用property()方法。


c = C()
print(c.x)
# --->250
c.x = 520
print(c.__dict__)
# --->{'_x':520}
del c.x
print(c.__dict__)
# --->{}


# 用装饰器的方法实现
class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)

    def getter(self, func):
        self.fget = func
        return self

    def setter(self, func):
        self.fset = func
        return self

    def deleter(self, func):
        self.fdel = func
        return self


class D:
    def __init__(self):
        self._x = 250

    @MyProperty
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


d = D()
print(d.x)
# --->250
d.x = 520
print(d.__dict__)
# --->{'_x':520}
del d.x
print(d.__dict__)
# --->{}


# 直接用property()的方法：


class E:
    def __init__(self):
        self._x = 250

    x = MyProperty()

    @x.getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


e = E()
print(e.x)
# --->250
e.x = 520
print(e.__dict__)
# --->{'_x':520}
del e.x
print(e.__dict__)
# --->{}
