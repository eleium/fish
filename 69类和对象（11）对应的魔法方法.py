# 跟属性访问相关的函数和魔法方法
# 对象可以通过(.)来进行属性访问，可以访问一个已有属性，还可以创建一个新属性

# python有几个BIF()函数:
# hasattr()判断是否有这个属性,
# getattr(),获取这个对象的属性，包括私有属性
# setattr()，增加这个对象的属性
# delattr()删除这个对象的属性
# 专门为对象的属性访问服务的。


class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


c = C("小甲鱼", 18)
print(hasattr(c, "name"))
# --->True   判断对象是否有name属性。

print(getattr(c, "name"))
# --->小甲鱼   获取对象的name属性值是 小甲鱼
print(getattr(c, "_C__age"))
# --->18    获取对象c的age属性值是18

setattr(c, "_C__age", 20)
#更改c对象的age属性值，原来是18，改为20
print(getattr(c, "_C__age"))
# -->20    获取更改后的c对象的age属性值：20


# getattr(obj, "name") 不是错
# 但如果属性名是固定的字符串，就和 obj.name 完全一样
# 所以没有必要用 getattr，直接用 obj.name 更清晰  直接用print(c.name),或者：print(c._C__age)

# delattr的用法与del()的用法一样。
delattr(c, "_C__age")
#删除对象c的age属性
print(hasattr(c, "_C__age"))
# --->false  对象c的age属性没有了。

# 这几个函数都有对应的魔法方法函数：
# getattr()的对应魔法方法是：__getattibute__()


class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        # 这是对象的私有属性。

        # __age=age
        # 这是局部变量，不是属性。
        # 记住：只有用 self.xxx 定义的才是实例属性，光写 xxx 只是局部变量。

    def __getattribute__(self, attrname):
        #给类C定义这么一个方法：__getattribute__()，用来获取对象的attrname属性。
        #此时的attrname是参数的名字，是形参，可以随便写，它对应的name，是实参，就是 '小甲鱼'.
        print("拿来吧你！")
        # 拦截到了，就会打印：拿来吧你。所谓拦截就是先运行，先执行，把后面的代码拦住了。
        return super().__getattribute__(attrname)
        # 把attrname当作实参传递进去。super()的作用是根据MRO规则，向父类寻找。找啥呢？找真正的父类的属性。
         #而__getattribute__()的上级是类C,类C的没有attrname属性，那就返回类C的哪一个属性？
        # __getattribute__ 是实例方法（第一个参数是 self）
        # 调用 super() 时，找的是当前类 C 的父类
        # 类 C 没有显式继承，默认父类是 object
        # 所以 super().__getattribute__ 就是 object.__getattribute__
        # 结论：父类是 object（所有类的最终基类）

        #  object 基类里有 attrname 属性吗？
        # 没有！ object 类本身不存储任何属性，但它提供了属性查找机制。
        #    object.__getattribute__ 是一个方法，不是属性
        # 这个方法的功能是在实例对象中查找属性
        # 它接收参数 name（属性名），然后去实例的 __dict__ 中找
        #找到具体是name,还是_C__age,由对象c调用方法时决定:
        # 对象c调用的是c.naem,那么attrnmae==name  ==小甲鱼
        #对象c调用的是c._C__age,那么 attrname == _C__age, ==18


c = C("小甲鱼", 18)
print(getattr(c, "name"))
# --->拿来吧你
# --->小甲鱼
# 所谓被拦截就是，访问到了一个特定的方法，并返回了方法的值。

# 也可以用改编名称的方法访问：
print(c._C__age)




# 方法	                触发时机	                                主要作用	         默认行为
# __getattribute__	每次访问属性时都优先调用（无论属性是否存在）	控制所有属性读取过程	如果属性存在则返回，不存在则抛出 AttributeError
# __getattr__	仅在正常属性查找失败（即属性不存在）且 __getattribute__ 抛出 AttributeError 之后调用	提供兜底或动态属性	不存在（默认对象没有这个方法）
# 直观理解：
# __getattribute__ 是“看门人”，每次访问都先经过它。(不管有没有那个属性，先print再说（上例中有print(拿来吧你))
# __getattr__ 是“备胎”，只在看门人说“没有这个属性”时才上场。

# 二、调用流程（关键）
# 当执行 obj.attr 时：
# Python 自动调用 obj.__getattribute__('attr')（实际是 object.__getattribute__(obj, 'attr')）。
# 如果 __getattribute__ 找到了 attr（通过常规方式，如实例字典、类字典、父类等），则返回其值。
# 如果 __getattribute__ 抛出 AttributeError，Python 会接着检查对象是否定义了 __getattr__：
# 如果定义了，则调用 obj.__getattr__('attr') 并返回其结果。
# 如果没有定义 __getattr__，则直接向调用者抛出 AttributeError。
# 注意：__getattribute__ 内部抛出 AttributeError 是触发 __getattr__ 的唯一途径
# 3. ⚠️ 无限递归陷阱
# 在 __getattribute__ 内部禁止直接使用 self.xxx 访问属性，否则会再次调用 __getattribute__ 形成无限递归。

# 七、总结速记表
# 特性	        __getattribute__	                           __getattr__
# 是否总是调用	✅ 是	                                      ❌ 仅当属性缺失且 __getattribute__ 抛异常
# 内置默认行为	有（从实例/类字典查找属性）	                      无（默认对象没有此方法）
# 内部访问自身属性	必须用 super().__getattribute__，否则递归	 可直接用 self.xxx（因为只会在缺失时调用，不会递归）
# 常见错误	无限递归	                                        忘记属性存在时不会触发
# 性能影响	每个属性访问都经过，开销大	                          仅缺失属性时触发，开销小



"""
. __age = age — 局部变量
python
class C:
    def __init__(self, name, age):
        self.name = name
        __age = age          # 局部变量，不是属性
        print(__age)         # ✅ 在这个方法内部可以访问
    def show(self):
        print(__age)         # ❌ 报错！其他方法访问不到
        print(self.__age)    # ❌ 也会报错，因为根本没有这个属性

c = C("小甲鱼", 18)
# print(c.__age)            # ❌ 报错
# print(c._C__age)          # ❌ 也会报错，因为根本没有这个属性
特点：

只在 __init__ 方法内部有效

方法执行完就销毁

不是对象的属性，实例访问不到任何形式

2. self.__age = age — 私有实例属性
python
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age     # 私有实例属性
        print(self.__age)    # ✅ 在这个方法内部可以访问
    def show(self):
        print(self.__age)    # ✅ 其他方法也能通过 self.__age 访问

c = C("小甲鱼", 18)
# print(c.__age)            # ❌ 直接访问报错
print(c._C__age)            # ✅ 通过改名后的名字可以访问（18）
特点：

是对象的实例属性，一直存在

类内部通过 self.__age 访问

外部通过 _C__age（名称改写）可以访问（但不推荐）

不是局部变量，不会被销毁

"""

# 如果访问一个根本不存在的属性，也会先启动拦截，然后才报错：

# print(c.fishC)

# --->拿来吧你。先打印这个，即先拦截了，
# AttributeError: 'C' object has no attribute 'fishC'

# getattr()是获取属性的内容，那么__getattribute__()是有啥作用呢？
# 是 对象去访问一个不存在的属性时才会被触发的魔法方法

# __getattribute__() 是“拦截器”，getattr() 是“调用器”。

# __getattribute__()：只要有人访问属性（无论用 . 还是 getattr()），它都会先被触发，可以在这里做“日志、权限检查、修改返回值”等操作。

# getattr()：只是一个手动获取属性的函数，和直接写 obj.name 几乎一样。必须由程序员手动调用，而__getattribute__()是python自动调用

# 1. 两者都是魔法方法
# __getattr__() 和 __getattribute__() 都是 Python 的魔法方法（也称为特殊方法、双下方法）。
#它们俩的作用都是 获取对象的属性。区别是一个手动获取__getattr__(),另外一个是自动获取__getattribute__().
# 魔法方法的特征：
# 名称前后都有双下划线 __（比如 __init__、__str__、__getattr__）
# Python 在特定场景自动调用，不需要手动调用
# 用于实现 Python 的内置行为或运算符重载

#总结
# 问题	                            答案
# 两者都是魔法方法？	             ✅ 是
# 魔法方法和普通方法区别？	         自动调用 vs 手动调用；      双下划线 vs 普通命名
# 两者作用都是获取属性？	         ✅ 是，但触发时机不同
# 何时用 __getattribute__？	        需要拦截所有属性访问（如日志、权限）
# 何时用 __getattr__？	           只需要处理缺失属性（如默认值、动态属性）
# 一句话记忆：
# __getattribute__ 是全部拦截（每个属性都经过）
# __getattr__ 是兜底处理（只有缺失才触发）




class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __getattribute__(self, attrname):
        print("拿来吧你！")
        return super().__getattribute__(attrname)

    def __getattr__(self, attrname):
        if attrname == "fishC":
            print("I love fishC")
        else:
            raise AttributeError(attrname)


c = C("小甲鱼", 18)
print(c.fishC)
#---->拿来吧你
#--->I love fishC
#--->Nove  这个None是由于print(c.fishC)的存在。返回值是None.
# print 是给人看的，return 是给程序用的。没有 return 的函数，统一返回 None。

# 当 Python 执行 c.fishC 时：
# 触发 __getattr__
# 执行 print("I love fishC")（屏幕上显示文字）
# 函数结束，没有 return → 默认返回 None
# 这个 None 被作为 c.fishC 的值
# 外层的 print(c.fishC) 打印这个 None

# __init__ 如果没有 return，也默认返回 None。而且 __init__ 不允许返回 None 以外的任何东西。
# Python 中每一个函数/方法，如果没有显式 return，都默认返回 None。
# print() 只是往屏幕上输出内容，和函数的返回值是两码事。

#赋值属性对应的是__setattr__()方法

"""
class D:
     def __setattr__(self,name,value):
         self.name=value
         这么些会造成无限递归，造成死循环，所以先注释掉
d=D()
d.name='小甲鱼'
print(d.name)
#---->报错：无限递归，死循环。
"""

# 1. d.name = '小甲鱼'                                 当对象的name属性被赋值为 '小甲鱼'的时候：
#    → 调用 D.__setattr__(d, "name", "小甲鱼")，        其中的d就是self。name是d的属性，'小甲鱼'是属性name的值。
# 2. 在 __setattr__ 内部执行 self.name = value
#    → self 是 d，name="name"，value="小甲鱼"
#    → 这又是一个赋值操作！
#    → 再次调用 D.__setattr__(d, "name", "小甲鱼")
# 3. 再次进入 __setattr__，再次执行 self.name = value
#    → 再次调用 D.__setattr__(d, "name", "小甲鱼")
# 4. 无限循环... 直到 RecursionError

# 为什么直接操作 __dict__ 不会递归？
# 因为：
# self.name = value → 属性赋值语法 → 触发 __setattr__
# self.__dict__[name] = value → 字典赋值语法 → 不触发 __setattr__

#总结表
# 魔法方法	             内部禁止写法	             内部正确写法
# __setattr__	        self.attr = value	       super().__setattr__(name, value) 或 self.__dict__[name] = value直接操作对象的属性字典
# __getattribute__	    self.attr	               super().__getattribute__(name)
# __getattr__	        self.attr（如果属性存在）	super().__getattr__(name) 或直接返回值

print('#'*88)
class D:
    def __setattr__(self,name,value):
        #__setattr__() 是一个拦截器，当尝试给实例的属性赋值时自动调用。在这个方法内部，你需要手动实现真正的赋值（否则属性不会被设置）。

        #形参和实参的关系
        #形参和实参：是接收/传递关系（实参的值传递给形参）
        #name 和 value：是两个独立的形参，没有直接赋值关系
        self.__dict__[name]=value
        #用直接操作对象的属性字典的方式，直接给键name 赋值


d=D()
d.name='小甲鱼'
print(d.name)
#--->小甲鱼

#del也同样使用：
class D:
    def __setattr__(self,name,value):
        self.__dict__[name]=value
    def __delattr__(self,name):
        del self.__dict__[name]
d=D()
d.name='小甲鱼'
print(d.__dict__)
#--->{name:'小甲鱼'}  查看当前的对象的属性
del d.name
print(d.__dict__)
#---->{}  属性被删除后，变成了空的字典
