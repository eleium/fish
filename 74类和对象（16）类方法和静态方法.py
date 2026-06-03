#
#类方法 @classmethon  类里面定义的函数，被称为方法。但是类本身通常没办法调用这些方法，需要实例对象来调用
#方法需要对象来绑定。
#类方法 就是需要类来绑定的方法

class C:
    #定义一个类C
    def fanA(self):
        print(self)
        #定义了类C的实例化对象的方法，即打印自己
    @classmethod
    #这样写就是类方法了
    def fanB(cls):
        print(cls)
        #定义了类C的方法是打印类自己

c=C()
print(c.fanA())
#<__main__.C object at 0x0000022A8B4A66F0>
#--->None

c.fanA='python'
print(c.fanA)
#--->pyhton
#方法fanA()绑定的是实例化对象c

c.fanB()
#---><class '__main__.C>
#这是因为fanB()方法绑定的是类C

# print(c.fanB('pycharm'))
#--->TypeError: C.fanB() takes 1 positional argument but 2 were given,因为类C定义时候没有参数： class C: 没有定义参数

#上面的self 和 cls 都是一种约定成俗的写法，可以互换，可以任意改写，代表的都分别是实例化的对象本身 和 类本身。

#类方法的作用： 1，统计类里面对象的数量：


class C:
    count=0
    def __init__(self):
        C.count+=1
    @classmethod
    def get_count(cls):
        print(f'类C一共创建类的{cls.count}个实例化的对象。')

c1=C()
c2=C()
c3=C()
c3.get_count()
#--->类C一共创建类的3个实例化的对象。

#如果在对象中创建一个跟类的属性同名的属性，将会覆盖掉类的属性，但是不影响类的方法。
c3.count=1
#把类的属性count=0覆盖成count=1
c3.get_count()
#--->类C一共创建类的3个实例化的对象。


#静态方法：staticmethod:放在类里面的函数，而不需要被绑定的函数。（通常类里面的函数是要被实例化对象绑定的，叫做实例化对象的方法。）

class C:
    @staticmethod
    def fanA(self):
        #定义这个函数的时候，有一个(self)参数，以后不论是实例化对象，还是类C本身调用的时候，都要增加一个参数。
        #实际上，静态方法是不需要参数的，因为它不需要被绑定
        print('I love python')

c=C()
c.fanA('a')
#定义类C的静态方法的时候，有一个(self)参数，所以创建实例化对象的时候，调用这个方法，必须加上一个参数。
#其实可以在创建类C的方法的时候，不指定参数，这样实例化对象调用类发方法的时候就不必要传参数啦，直接调用，就可以得到该方法的返回值。
C.fanA('self')
#(self)的道理同上。


#可以效仿刚才的类方法，统计实例化对象的个数：
class C:
    count=0
    def __init__(self):
        C.count+=1

    @staticmethod
    def get_count():
        print(f'类C一共有{C.count}个实例化对象')

c1=C()
c2=C()
c3=C()
c3.get_count()
#--->类C一共有3个实例化对象
#使用静态方法的时候，因为是直接调用了类C的方法：C.count(),所以不用担心实例化对象那个的属性覆盖类的属性的问题啦。

c1.get_count()
#不管用哪一个实例化对象调用get.count()方法，答案都是C.count(),都是3.

#当操作不涉及类属性或者对象属性引用的时候，静态方法更合适。
#但是像统计实例对象数量这样的任务呢，交由类方法可能会更好

class C:
    count=0
    @classmethod
    def add(cla):
        cla.count+=1
    def __init__(self):
        self.add()
    @classmethod
    def get_count(cls):
        print(f'该类一共实例化了{cls.count}个对象')

class D(C):
    count=0

class E(C):
    count=0

c1=C()
c1.get_count()
#--->该类一共实例化了1个对象

d1,d2=D(),D()
d2.get_count()
#--->该类一共实例化了2个对象
e1,e2,e3=E(),E(),E()
e3.get_count()
#--->该类一共实例化了3个对象

#为啥定义类C的时候，要独立的定义一个 def add(cls)方法？就是为了自动化计算类的对象，让构造函数去调用add()方法，就不用去管是子类还是父类。
#谁去调用add()方法，谁就自动把对应的类给传递进去，那么对应的就是该类的count类属性