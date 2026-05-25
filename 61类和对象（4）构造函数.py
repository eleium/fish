# 构造函数 __inint__().在定义类的同时定义一个构造函数（也就是定义__init__（self,x,y）的参数。），就可以在实例化对象的同时，实现个性化定制。

"""总结
def __init__(self,x,y) 是必须的吗？	不是绝对必须，但如果需要传参初始化对象，则必须使用
能不能直接写 self.x = x 在类体里？	❌ 不行，self 只能在方法中使用.写道类里，就变成继承了。

__init__() 是 Python 中 最常用的构造函数，用于“个性化定制”每个对象。
它会在创建对象时自动调用，无需手动调用。
如果你不写 __init__()，Python 会提供一个默认的空构造函数。

所有对象的值都一样	❌ 不用构造函数	直接在类里属性定义 x = 0
每个对象的值不一样	✅ 必须用	def __init__(self, x, y)
"""


class C:
    def __init__(self, x, y):
        # 用这个__init__()函数，给随后的实例化对象定义了x,y两个属性。
        # 这是类的构造函数 init，用于初始化对象属性。
        # 当创建类实例时，接收参数 x 和 y，并将它们分别赋值给实例属性 self.x 和 self.y，使每个对象拥有独立的坐标属性。
        self.x = x
        # 此时的self.x和self.y分别标识实例化对象的属性。而x,和y，分别是这个实例化对象的属性的值。

        self.y = y

    def add(self):
        return self.x + self.y

    def mul(self):
        return self.x * self.y


c = C(10, 20)
print(c.add())
# -->30
print(c.mul())
# -->200
# 内省一下：
print(c.__dict__)
# -->{'x':10,'y':20} 说明c.x和c.y分别是10和20。


# 重写：子类用属性和方法来覆盖父类的属性和方法。
class D(C):
    def __init__(self, x, y, z):

        C.__init__(self, x, y)
        # 调用C类的函数。这样就不用写： self.x=x self.y=y了
        self.z = z
        # 添加类D的新的属性

    def add(self):
        return self.x + self.y + self.z
        return self.z + C.add(self)

    def mul(self):
        return C.mul(self) * self.z


# 注意上面的都要用大C,因为调用的是父类的方法，而不是小c,小c是实例化对象。

d = D(10, 20, 30)
print(d.add())
# --->60

print(d.mul())
# -->6000


# 这种直接通过类名来访问类里面的方法的做法，就叫做 调用未绑定的父类的方法
# 这种方法有时候会造成 钻石继承的问题。

# 一个类有多个父类，并且这些父类又继承自另一个类。
# 这种情况就叫做 “钻石继承”。

# 在这种情况下，子类将继承多个父类的属性和方法。
# 如果子类没有定义与这些属性或方法相同的方法，则将从这些父类继承这些属性和方法。
# 如果子类定义了与这些属性或方法相同的方法，则将覆盖这些父类的方法。


print("-" * 100)


# 钻石继承：
class A:
    def __init__(self):
        print("hello ,Im A")


class B1(A):

    def __init__(self):
        A.__init__(self)  # 未绑定的父类的方法。
        # a.__init__       # ✅ 绑定的方法（bound method）— Python 自动把 a 作为 self 传进去
        # A.__init__       # ❌ 未绑定的方法（unbound method）— 没人告诉它 self 是谁
        # 当你写 a.__init__()，Python 自动把 a 塞给 self，这就是绑定。

        # 当你写 A.__init__，它只是一个光秃秃的函数，没有和任何实例绑定，所以叫未绑定。你需要手动把 self 传给它

        print("hello,Im B1")


class B2(A):
    def __init__(self):
        A.__init__(self)
        print("hello,Im B2")


class C(B1, B2):
    """类C继承了类B1和类B2。"""

    def __init__(self):
        """定义了两个父类，就需要调用两个父类的__init__()方法。"""
        B1.__init__(self)
        B2.__init__(self)
        print("hello,Im C!")


c = C()
# print(C.__dict__)# __dict__是属性，不是方法，不需要小括号。

# super()函数：能够在父类中搜索指定的方法，并自动绑定好self参数
print('-'*100)

class B1(A):
    def __init__(self):
        super().__init__()
        print('我是B1啊')
class B2(A):
    def __init__(self):
        super().__init__()
        print('我是B2')
class C(B1,B2):
    def __init__(self):
        super().__init__()
        print('我是C啊')

c=C()

#只要用super()方法，他就会用MRO顺序自动向上寻找父类的方法，并自动绑定self。自动避免重复的调用。
#MRO：  method resolution order 方法解析顺序
#查找一个类的MRO顺序，有两种方法：
#用类名.mro()
print(C.mro())
#-->[<class '__main__.C'>, <class '__main__.B1'>, <class '__main__.B2'>, <class '__main__.A'>, <class 'object'>]一个列表
#<class 'object'>是所有类的基类，所有类都继承自 object,是隐蔽的继承

#第二种查找MRO的办法：
print(C.__mro__)
#-->(<class '__main__.C'>, <class '__main__.B1'>, <class '__main__.B2'>, <class '__main__.A'>, <class 'object'>)

