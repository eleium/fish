# 多继承里面的Mixin概念：混入  面向对象编程时反复出现的问题而设计出来的解决方案。既：把前面所学语法组合使用，达到完整的程序功能。


class Animal:
    def __init__(self, name, age):
        # 构造函数定义的是类的属性。
        self.name = name
        self.age = age

    def say(self):
        print(f"我是{self.name},我今年{self.age}岁了。")


class FlyMixin:
    # 追加了一个Mixin类，这个类的命名不用小括号？
    # 是因为 FlyMixin 本身是一个基础的功能模块类，它不需要继承其他自定义类，直接继承默认的 object 即可。
    # 当其他类（如 Bird 或 SuperHero）需要飞行能力时，会把 FlyMixin 放在它们的小括号里进行继承。
    def fly(self):
        print("I can fly!")


class Pig(FlyMixin, Animal):
    def special(self):
        # 给自己添加一个特殊的方法。
        print("我是猪，爱吃大白菜。")


p = Pig("花花", 5)
# 实例化对象的时候就要把父类的属性填写进去。
p.say()
p.special()
p.fly()

print("-" * 100)


class Displayer:
    # 为何没有小括号？有没有都一样(python3以上)，都表示这个类继承于基类object.是隐性继承。
    def display(self, message):
        # 定义类Displayer的方法：display。其中这个方法的参数是要传入的message.
        print(message)


class LoggerMixin:
    # 定义一个混入的类LoggerMixin。这个LoggerMixin类，将把自己的属性和方法，都添加到下面要创建的子类将要继承的父类的功能里。
    def log(self, message, filename="logfile.txt"):
        # 定义了一个叫log的方法，方法的参数是：message,和 filename='loglfile.txt'.
        with open(filename, "a") as f:
            # 用with语句，用追加内容的方式打开文件filename .(这个filename到底是哪个文件，是logfile.txt?为啥不用f'{filename'}来引用？)
            f.write(message)
            # 写入message。这个message,是当实例化对象时才会创建的。现在还没有。

    def display(self, message):
        # 定义第二个方法：display,这个方法也有一个叫message的参数。
        super().display(message)
        # 这个message参数，需要向上寻找。去LoggerMIxin寻找，如果没有父类里寻找。按照NRO顺序，去上级父类里寻找。

        # 这是上面的display方法实现的第一步要执行的。下面的self.log(message)是第二部要执行的。都是为了上面方法的实现。

        self.log(message)
        # 调用LoggerMixin的Log方法，并传入message参数。


class MySubClass(LoggerMixin, Displayer):
    # 定义一个子类:MySubClass。继承自 LoggerMixin和Displayer.
    def log(self, message):
        # 定义自己的方法：log,并传入参数message.
        super().log(message, filename="subclasslog.txt")
        # 引用log方法的父类，并传入参数message,filename='subclasslog.txt'。


subclass = MySubClass()
# 创建实例化对象：subclass
subclass.display("This is a test!")
# 实例化对象subclass调用display方法，并传入参数message="This is a test!"


# 本脚本将在当前目录下创建一个叫subclasslog.txt的文件，并写入： This is a test!
# 程序执行的顺序：
# 18 → 19 → 9 → 11 → 2 → 3(打印) → 返回11 → 11调用self.log(message)→ 14 → 6 → 7(写入文件) → 返回

# 继承顺序：
# 1.先从最左边的父类开始，继承。
# 2.继承的父类，如果有多个，按照从左到右的顺序，依次  继承 、调用、执行、返回。。

print(
    MySubClass.mro()
)  # --->[<class '__main__.MySubClass'>, <class '__main__.LoggerMixin'>, <class '__main__.Displayer'>, <class 'object'>]
print(
    MySubClass.__mro__
)  # --->(<class '__main__.MySubClass'>, <class '__main__.LoggerMixin'>, <class '__main__.Displayer'>, <class 'object'>)
