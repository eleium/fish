class D:
    def __get__(self, instance, owner):
        print("get~~")

        # 什么是描述符（Descriptor）？是一个接口。
        # 描述符是定义了 __get__、__set__、__delete__ 中至少一个方法的类，并且这个类的实例必须赋值给另一个类的类属性。
        # 描述符不是"属性"的概念，而是方法接口约定。
        # 一个类如果实现了 __get__ / __set__ / __delete__ 中的至少一个方法，这个类就是描述符类。
        # 描述符协议："如果一个类有 __get__() 方法，它就是描述符类"

        # D 类有一个方法属性 __get__。 方法也是属性，通常方法是函数，属性是数据。


class C:
    def __init__(self):
        self.x = D()
        # self.x=D()是类C的实例化对象c的属性，而不是类D的属性

        # 类属性：写在 class 下面，所有实例共享同一份数据

        # 实例属性：写在 __init__ 里面用 self.xxx，每个实例独立拥有自己的数据
        # 属于具体的实例对象，每个实例都有自己独立的一份，必须通过实例（self）来定义


c = C()
print(c.x)
# ---> <__main__.D object at 0x000001C64E6A6570>,是描述符对象。并没有打印get~~
# 因为描述符是只能应用与类属性，而不是该类的实例化对象的属性

# 描述符对象是个什么概念？描述符是一个对象，而不是一个属性：
# 描述符对象 = 一个实现了 __get__ / __set__ / __delete__ 中至少一个方法的类的实例。
# 这个实例时类的级别的，而不是实例化对象级别的，，记忆口诀：描述符是"类级别的守卫"，不是"实例级别的数据"。
# 关键点：描述符对象 ≠ 描述符类

class C:
    x=D()
    #这是类的属性了。

c=C()
c.x
#--->get~~
#class C:   x = D() 是把 D 的一个实例（描述符对象）赋值给了类C属性 x。  当通过 c.x 访问时，会调用 D 类的 __get__ 方法。


# 方法也是属性的一种，但通常我们说"属性"指数据，说"方法"指函数


"""
关于数据属性、方法属性、以及描述符的一个例子：

class D:
    # 这是数据属性
    data_attr = 100

    # 这是方法属性（普通方法）
    def normal_method(self):
        return "hello"

    # 这是方法属性（描述符方法）
    def __get__(self, instance, owner):
        return "from __get__"

class C:
    # 普通类属性（数据）
    normal = 42

    # 描述符类属性（对象 + 特殊方法）
    desc = D()
    """
#描述符还可以细分为两类： 数据描述符和 非数据描述符，主要是根据实现的不同魔法方法来划分：
#如果是实现了__set__()和__del__()的方法的，就是数据描述符
#如果只是实现了 __get__()魔法方法，就是非数据描述符

#当发生属性访问的时候，按照如下优先级： 数据描述符> 实例对象的属性> 非数据描述符 >类的属性（类还要根据MRO来确定类的继承的顺序）

#上面的class D: 因为只实现了__get__()方法，所以是非数据描述符。如果给实例对象的 同名属性赋值，将会按照优先级，覆盖掉这个非数据描述符：

c.x='pytohn'

print(c.x)
#--->python 现在不是打印get~~了，原来的__get__()的print('get~~') 被 c.x='python'覆盖了。描述符拦截失败
#如果用类的属性来访问，还是可以拦截的。只不过是实例化对象的属性被覆盖了。
print(C.x)
#--->get~~
#--->None    这是类的属性，还是被拦截到。注意是大写的C，是类。
print('-'*88)
class D:
    def __get__(self,instance,owner):
        print('get~~~')
    def __set__(self,instance,value):
        print('set')


class C:
    x=D()
#给实例对象的同名属性赋值
c=C()
c.x
#--->get~~  现在还没有给实例化对象小c的属性赋值，那么就被__get__()拦截到。

c.x='python'
#--->set   有了赋值这个动作，就触发啦__set__()魔法方法的拦截
c.x
#--->get~~
print(c.__dict__)
#--->{}  c.x='python'并没有传到c的属性里去。因为被数据描述符拦截了，也就是__set__()拦截。数据描述符的优先级最高。
#用间接的方法，把值添加到c的属性里面去：
c.__dict__['x']='python'
print(c.__dict__)
#--->{'x':python} 已经写进去了，然后试一下能不能访问
c.x
#--->get~~~仍然被拦截了，体现访问优先级

#这个优先级是定义在__getattribute_()magic method的默认实现，因为__getattribute__()是管理属性的获取

class C:
    x=D()
    def __getattribute__(self,name):
        print('aha~~~~')

#如果打印出aha~~~,说明优先被__getattribute__()方法拦截：
c=C()
c.x
#--->aha~~~~ 拦截成功。即使是数据描述符__get__(),也不管用啦，说明__getattribute__()是最优先
print('*'*88)

#描述符的魔法方法：__get__(),__set__(), __del__()，这些描述符实现的都是对属性的拦截。
#实际开发工作中，利用描述符拦截实例对象的属性，然后做一些额外的工作，之后还是要完成对属性的获取、赋值、删除的工作，比如：
#通过用描述符拦截了实例对象的x属性，确认了属性的合法性，判断它的值是否>18之类的，之后如果符合要求，就把它写入实例对象的属性当中去。
#也就是说，需要描述符操作对象的__dict__字典，因为instance代表的就是所拦截的属性所在的实例对象。

class D:
    def __init__(self,name):
        self.name=name
        #name的作用：记住描述符拦截的属性的属性名。通过参数传递进去的意思
    def __get__(self,instance,ownen):
            #instance:描述符管理的属性所在的实例化对象
            print('get~~~')
            #如果打印了get~~~，就表示被这个魔法方法__get__()所拦截
            return instance.__dict__.get(self.name)
            #返回这个实例化对象的字典调用get()函数，获取实例化对象本身的名字
    def __set__(self,instance,value):
            print('set~~~')
            instance.__dict__[self.name]=value
            #通过name,把value传进去

#测试：
class C():
    x=D('x')
    #把属性名变成字符串'x'传递进去，给到name
c=C()
c.x
#--->get~~~表示拦截成功，但是x是空的，所以没有return instance.__dict__.get(self.name)
print(c.__dict__)
#--->{}实例化对象的属性字典是空的。

c.x=250
#--->set~~~
print(c.__dict__)
#--->{'x':250}  通过描述符，间接的把赋值写进了属性的字典中
print(c.x)
#--->get~~~
#--->250

#上面的方法可以通过描述符把值写入实例化对象的属性字典里。但是，class C: x=D("x"),但是这种写法很难以接受，所以用到__self_name__()方法：



# 现在是第四个：这个方法，就使得操作很优雅啦
# __set_name__(self,name,owner)

class D:
    def __set_name__(self,owner,name):
         self.name=name
    def __get__(self,instance,owner):
        print('get~~~')
        return instance.__dict__.get(self.name)
    def __set__(self,instance,value):
        print('set~~~~')
        instance.__dict__[self.name]=value


class C:
    x=D()

c=C()
c.x
#--->get~~~
print(c.__dict__)
#--->{} 现在是空的

c.x=280
#--->set~~~
c.x
#--->get~~~
print(c.__dict__)
#--->{'x':280}