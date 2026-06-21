#元类（metaclass)

#类class 就是创建对象的模板,而元类是创建类的模板。
# 定义的每一个类，都是由 type 这个元类创建的，包括object，也包括type自身也是typep()创建的。
#所有的元类都继承自type类。（python中还有其他的元类，甚至可以自己创建元类）
# 即每一个类都是type类的实例对象。是工厂。
# 所有的类的基类是object。即每一个类都是object的子类。是老祖宗。


# object 是 type 的实例（因为 type(object) 返回 <class 'type'>）
# type 是 object 的子类（因为 type.__base__ 返回 <class 'object'>）
# object 是“父辈”关系（继承），type 是“造物主”关系（实例化）。
# 所有类都继承 object，所有类也都是 type 的实例。
# object 是继承链的终点，type 是创建链的起点。
# 它们互相依赖，一起构成了 Python 的类型系统基石。

#想要自己创建一个元类，让它继承自type就可以了：
class MetaC(type):
    #创建MetaC,继承自type元类，type类是所有元类的父类。这时，MetaC就是一个新的元类。
    pass

#通过新创建的元类来创建类,需要在类的小括号里使用metaclass关键字,并引入刚才创建好的元类：
class C(metaclass=MetaC):
    #metaclass=MetaC只表明了由MetaC创建了类C的创建关系，而不是继承的子类父类关系！！！
    pass

c=C()
print(type(C))
#---><class '__main__.MetaC'> 类C属于元类MetaC
#type(c) 是一个函数调用：这是获取一个对象类型最通用、最标准的方式。我们通常推荐使用 type(obj) 来检查对象类型。
print(C.__class__)
#---><class '__main__.MetaC'>

print(type(c))
#---><class '__main__.C'>,  type(c)等价于c.__class__，都是询问对象c的所属类。
print(c.__class__)
#---><class '__main__.C'>
#c.__class__ 是一个属性访问：它直接从对象实例的 __class__ 属性中读取其所属的类。这种方式更“底层”，更直接。

print(type(MetaC))
#---><class 'type'>

#对象被创建的时候，会调用__init__()魔法方法，所以__init__()方法又叫做构造函数。
# 但是它并不是实例化对象调用的第一个魔法方法，第一个是__new__()魔法方法

#现在，同时定义元类和类里面的__init__()和__new__()方法，看看它们的执行逻辑：

class MetaC(type):
    def __new__(mcls,name,bases,attrs):
        print('__new__() in MetaC~~~')
        return type.__new__(mcls,name,bases,attrs)
    def __init__(cls,name,bases,attrs):
        print('__init__() in MetaC!!!')
        type.__init__(cls,name,bases,attrs)


class C(metaclass=MetaC):
    #metaclass=MetaC 表示类C是由MetaC创建，但不是表示类C是MetaC的子类！！！
    def __new__(cls):
        print('__new__() in C!!~~')
        return super().__new__(cls)
    def __init__(self):
        print('__init__() in C~~~')

#---->__new__() in MetaC~~~
#----> __init__() in MetaC!!!
#当创建类C刚刚完成的时候，就执行调用了__new__()和__init__()

c=C()
#---->__new__() in C!!~~
#--->__init__() in C~~~
# 刚刚创建实例化对象，就立即调用了类C的__new__()方法和__init__()方法

#两个__new__()被调用的时机不同，一个是创建类C就调用，另一个是创建类C的实例化对象时调用，所以类C的super().__new__调用的并不是元类MetaC的__new__()方法。
#那么，类C的super().__new__,调用的是谁的呢？是object的。当一个类没有指定的父类的时候，就去找object

print('- -'*40)
#打印看看MetaC的__new__()的参数都是啥：

class MetaC(type):
    def __new__(mcls,name,bases,attrs):
        print(f'mcls={mcls},name={name},bases={bases},attrs={attrs}')
        #其实就是用type创建类时，传进去的参数（name,base,dict,和**kwds)
        print('__new__() in MetaC~~~')
        return type.__new__(mcls,name,bases,attrs)
    def __init__(cls,name,bases,attrs):
        print(f'cls={cls},name={name},bases={bases},attrs={attrs}')
        print('__init__() in MetaC!!!')
        type.__init__(cls,name,bases,attrs)

class C(metaclass=MetaC):
    #metaclass=MetaC 表示类C是由MetaC创建，但不是表示类C是MetaC的子类！！！
    def __new__(cls):
        print('__new__() in C!!~~')
        return super().__new__(cls)
    def __init__(self):
        print('__init__() in C~~~')

#--->mcls=<class '__main__.MetaC'>,name=C,bases=(),
# attrs={'__module__': '__main__', '__qualname__': 'C', '__new__': <function C.__new__ at 0x0000021FF6D09440>,
# '__init__': <function C.__init__ at 0x0000021FF6D094E0>, '__classcell__': <cell at 0x0000021FF6D1C400: empty>}
#name对应类名，bases对应的时父类，attrs对应的是属性和方法

# --->__new__() in MetaC~~~

# cls=<class '__main__.C'>,name=C,bases=(),attrs={'__module__': '__main__', '__qualname__': 'C',
# '__new__': <function C.__new__ at 0x0000021FF6D09440>, '__init__': <function C.__init__ at 0x0000021FF6D094E0>,
# '__classcell__': <cell at 0x0000021FF6D1C400: MetaC object at 0x0000021FF6C0E5C0>}
# name对应类名，bases对应的时父类，attrs对应的是属性和方法

# ---->__init__() in MetaC!!!




#__call__()方法，就是拦截对象被当作函数调用时的操作，就是把对象当作函数使用
#__call__() 方法的核心作用，就是让一个实例对象可以被当作函数一样来“调用”。
# 当作函数来操作”指的就是：你可以在一个对象后面直接加上括号 () 来执行它。

#如果把__call__()方法定义到元类中，应该拦截的是 类实例化对象的操作。等级升高了一级。

class MetaC(type):
    def __call__(cls,*args,**kwargs):
        print('__call__() in MetaC lalala ')

class C(metaclass=MetaC):  #由MetaC创造，而不是继承于MetaC
    pass
c=C()
#--->__call__ in MetaC lalala  当创建了类C的实例化对象c时，触发了元类MetaC的__call__()方法


#元类的地位非常高级，绝大多数时通过 __new__(),__init__()和__call__()方法来实现
