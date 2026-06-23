

#Mixin类，为一些不相关的子类提供一些额外的功能，类似插件或外挂，
# 所以对于Mixin类，就不需要有实例化。只是把它内部提供的方法，作为父类，直接插入子类，实现额外的功能就够了。

#另外一种不能够被实例化的类： 抽象基类
#1，python的抽象基类 不能够被直接实例化，只能够被继承使用
#2，子类必须实现抽象基类里面定义的抽象方法，否则无法被实例化
#python 里，用ABC模块来定义抽象基类： AbstractBaseClass模块。最有代表的是ABCMeta 和 abstractmethod

from abc import ABCMeta, abstractmethod


class Fruit(metaclass=ABCMeta):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    #把后导入的abstractmethod当作装饰器来指定抽象方法。如果装饰器制定了抽象方法，那么继承了抽象基类的子类，必须实现这个装饰器指定的方法
    def good_for_health(self):
        pass

# fruit=Fruit('水果') 

#这是在直接实例化一个对象fruit,但是报错了。
#--->TypeError: Can't instantiate abstract class Fruit without an implementation for abstract method 'good_for_health'
#错误：Fruit 是一个抽象类，缺少 good_for_health 方法的具体实现，因此无法创建它的实例。

# instantiate:实例化，根据类创建具体的对象（实例）的动作。比如 c = C()
#abstract: 抽象的  只有定义（方法名），没有具体实现（没有代码体）的概念。比如 @abstractmethod 标记的方法
# implementation 实现	具体写出来的代码逻辑，也就是方法里面真正执行的语句


# class Banana(Fruit):
    # pass

# b=Banana('水果')

#----> Can't instantiate abstract class Banana without an implementation for abstract method 'good_for_health'
#虽然继承了抽象基类，但是没有实现抽象方法。因为@stractmethod装饰的 goog_for_health还没有定义抽象方法

class Banana(Fruit):
    def good_for_health(self):
        print('水果对身体有好处，尤其是香蕉')
        #此时，定义了这个由元类Fruit创建的类Banana的具体的抽象方法：good_for_health，并print('水果.....')

banana=Banana('水果')
banana.good_for_health()
#---->水果对身体有好处，尤其是香蕉

"""
class Banana(Fruit):
    def funcA(self):
        print("我喜欢苹果")
banana=Banana('黄瓜')
banana.funcA()
"""

#---> Can't instantiate abstract class Banana without an implementation for abstract method 'good_for_health'
#因为元类创建的类，没有实现抽象基类的抽象方法：good_fof_health,所以实例不能成立
print('-- -'*40)

#python官方文档，把这个叫做鸭子类型：如果一个鸟，走路像鸭子，游泳像鸭子，叫声像鸭子，那么它就是鸭子。是一种编程风格。

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'我是一只猫，叫{self.name},今年{self.age}岁')

    def say(self):
        print('miaomiao')

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'我是一只狗，叫{self.name},今年{self.age}岁')

    def say(self):
        print('wangwang')

class Pig:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'我是一只猪，叫{self.name},今年{self.age}岁')

    def say(self):
        print('呵呵呵呵')


c=Cat('四月',3)
d=Dog('旺财',4)
p=Pig('花花',5)

def Animal(x):
    x.intro()
    x.say()

Animal(c)


#上面的例子，如果Dog里面，把say写成say_hi,就会报错：
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'我是一只猫，叫{self.name},今年{self.age}岁')

    def say(self):
        print('miaomiao')

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'我是一只狗，叫{self.name},今年{self.age}岁')

    def say_hi(self):
        print('wangwang')

class Pig:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'我是一只猪，叫{self.name},今年{self.age}岁')

    def say(self):
        print('呵呵呵呵')


c=Cat('四月',3)
d=Dog('旺财',4)
p=Pig('花花',5)

def animal(x):
    x.intro()
    x.say()

animal(d)
#---->我是一只狗，叫旺财,今年4岁
# AttributeError: 'Dog' object has no attribute 'say' ,意思是Dog对象没有say属性。


#下面用抽象基类，抽象方法演示：

class Animal(metaclass=ABCMeta):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def intro(self):
        pass

    @abstractmethod
    def say(self):
        pass

    #其中ABCMeta是抽象基类，abstractmethod是抽象方法。抽象方法可以是多个。
    #注意：抽象发方法一定要在抽象基类内部，即缩进要正确。
    #@abstractmethod是方法装饰器

    # ABCMeta 让类变成“抽象基类”，@abstractmethod 标记的方法就是“抽象方法”。


    #Animal 是一个抽象基类，是由ABCMeta创建（metaclass=ABCMeta),不能被直接实例化。
    # 任何继承 Animal 的子类，必须同时实现 intro 和 say 两个抽象方法，否则无法实例化。
    # 普通方法（如 __init__）可以被子类直接继承使用，不需要重写。

class Cat(Animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'我是一只猫，叫{self.name},今年{self.age}岁')

    def say(self):
        print('miaomiao')

class Dog(Animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'我是一只狗，叫{self.name},今年{self.age}岁')

    def say_hi(self):
        print('wangwang')

class Pig(Animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'我是一只猪，叫{self.name},今年{self.age}岁')

    def say(self):
        print('呵呵呵呵')


c=Cat('四月',3)
d=Dog('旺财',4)
p=Pig('花花',5)

def animal(x):
    x.intro()
    x.say()

animal(d)
#---->TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'say'
#直接报错，根本不运行.这也是抽象基类的一个优势。更快的发现bug.

#抽象基类也是一种规范编程的手段