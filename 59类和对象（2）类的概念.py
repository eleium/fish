# 类就是一个变量。可以被赋值，可以被覆盖。
# 面向对象编程的三大特征之一：封装:在创建对象之前，通过类 ，把属性和方法打包，封装在一起。通过类，生成相对应的对象。
# 面向对象编程的三大特征之二：继承：子类继承父类的属性和方法，子类可以重写父类的方法，也可以添加新的属性和方法。
# 通过继承产生的类叫 子类。被继承的叫父类、基类或者超类。


class A:
    x = 520

    def hello(self):
        print("hello,I am Jack")
        return "hello,I am Jack"


class B(A):
    pass


# 此时，B类继承了A类的属性和方法，B是子类，A是父类。

# 创建一个实例对象：
b = B()
print(b.hello())
print(b.x)
# --->hello,I am Jack
# --->hello,I am Jack  打印两遍是因为用了print()，打印了返回值。如果没有返回值，就显示None.
# --->520


# 如果B类里面有自己的属性和方法，那么就会覆盖掉A类的属性和方法：
class B(A):
    x = 1314

    def hello(self):
        print("这是 b 实例对象的 hello 方法")


c = B()
print(c.hello())
# --->这是 b 实例对象的 hello 方法
# --->None
print(c.x)
# --->1314

# 用BIF函数 instance()来判断一个实例对象是否属于另一个类：
print(isinstance(b, B))
# --->False  因为B(A)在24行重新定义了。而c是新的B类的实例对象。b的B(A)类已经不见了，被覆盖了。
print(isinstance(c, B))
# --->True

print(isinstance(c, A))  # --->True

# 用issubclass()来判断，一个类是否是另一个类的子类
print(issubclass(B, A))  # --->True


print("-" * 88)
# 多重继承：一个类可以继承多个父类。


# 先重新创建一个B类。
class B:
    x = 888
    y = 999

    def hello(self):
        print("大家好，我是B~")


# 创建一个大C类，继承自A和B。
class C(A, B):
    pass


# 实例化一个对象小c，这个对象来自C类。
c = C()
print(c.x)
# --->520
print(c.hello())
# --->hello,I am Jack
# 呈现的都是A类的属性和方法。没有B啥事。 当调用的是A类中没有的时候，才会去B类中找。
print(c.y)
# --->999

print("-" * 88)


# 组合：先创建三个类：
class Turtle:
    def say(self):
        print("不积跬步，无以至千里")


class Cat:
    def say(self):
        print("喵喵喵")


class Dog:
    def say(self):
        print("汪汪汪")


# 定义一个花园 类
class Garden:
    # 先定义属性：
    t = Turtle()
    c = Cat()
    d = Dog()

    # 定义方法：
    def say(self):
        self.t.say()
        self.c.say()
        self.d.say()

    # 定义方法的时候，一定要加上self.


# 创造一个花园的实例对象：
g = Garden()
print(g.say())
# --->不积跬步，无以至千里
# --->喵喵喵
# --->汪汪汪

# print(g.c)
