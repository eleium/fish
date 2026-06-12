# 类是模具，对象是具体的事务。
# tumpl,set,dict 都是对象。
# 静态的属性（静态的特征），和动态的方法（所能做的事），构成了对象。每个具体的对象又有不同的属性和方法。


# 创建类，用关键字class:,类名首字母大写，后面跟冒号。
class Turtle:
    # 先创建静态的属性：
    head = 1
    eyes = 2
    legs = 4
    shell = True

    # 再创建动态的方法：
    def crawl(self):
        print("乌龟爬行")

    def run(self):
        print("乌龟也可以跑起来")

    def bite(self):
        print("乌龟也会咬人")
        return "乌龟也会咬人啊，还死不松口"

    def eat(self):
        print("乌龟也喜欢吃肉")

    def sleep(self):
        print("乌龟最喜欢睡觉")


# 所谓属性，就是类里面的变量：head,eyes,legs,shell。所谓方法，就是类里面的函数:def 的 crawl，run,bite,eat,sleep.
# 以上就是一个turtle的类。在这个基础上，我们可以创建具体的对象：

# 创建一个具体的乌龟对象
my_turtle = Turtle()

# 调用对象的方法
my_turtle.crawl()
my_turtle.run()
my_turtle.bite()
my_turtle.eat()
my_turtle.sleep()

t1 = Turtle()
print(t1.head)
print(t1.legs)
print(t1.crawl())
# --->乌龟爬行
# --->None 因为上面定义crawl方法的时候，没有返回值，所以默认None.用了print()函数输出就会输出None:
# 如果直接用t1.turtle(),就不会输出None.或者定义crawl方法的时候，return '乌龟爬行'.

# 有了Turtle这个类，我们就可以创建很多个乌龟对象，每个对象都有相同的属性和方法，但它们是独立的，可以有不同的状态。
t2 = Turtle()
print(t2.legs)  # --->4
print(t2.bite())
# --->乌龟也会咬人啊，还死不松口。

# 创建出对象后，可以修改对象的属性和方法：
t2.legs = 3
print(t2.legs)  # --->3
t2.bite = "乌龟也会咬人啊，还死不松口，咬死你，除非打雷"
print(t2.bite)
# --->乌龟也会咬人啊，还死不松口，咬死你，除非打雷

print("-" * 88)
# 此时的t1并没有改变：
print(t1.legs)
print(t1.bite())
# --->乌龟也会咬人
# --->乌龟也会咬人啊，还死不松口  打印两次是因为t1.bite()调用了还有一次是print（）打印了 return 的结果。
# 可以给t1重新赋值，也可以添加新的属性和方法：

t1.mouth = 1  # 给t1添加了一个新的属性mouth


"""对比：给类加方法 vs 给对象加方法
方式	影响范围	写法
给类加	所有对象都有	直接在 class 里定义
给对象加	只有这个对象有	对象.方法 = types.MethodType(函数, 对象)
"""


# 封装：是面向对象编程的三大特征之一，指的是把对象的属性和方法封装在一起，对外界隐藏对象的内部实现细节，只暴露必要的接口来访问和操作对象。
# 另外两个是继承和多态。
# 创建一个类的时候，就是把这个类的属性和方法封装在一起了。

# Python 到处都是对象：
x = 50
print(type(x))  # ---><class 'int'>  x是一个整数对象。
y = "Hello"
print(type(y))  # ---><class 'str'>  y是一个字符串对象。

# 其他的list ,tuple ,set , dict ,function, class, module,file ,等等，都是对象。

print("-" * 88)

# 对象的方法里面有一个参数：self,这个参数是指向对象本身的一个引用，在方法内部可以通过self来访问对象的属性和方法。
# 在调用方法的时候，不需要传入self参数，Python会自动把对象本身作为self参数传递给方法。


class C:
    # 给类C定义一个方法叫hello,这个方法有一个参数self,在方法内部打印'hello'.但是现在先不写self参数，看看会发生什么：
    def hello():

        print("hello")


# 创建一个对象c,调用c.hello()方法：
c = C()
# 调用c.hello()方法：
# c.hello()
"""这个方法,但是没有加 self
class C:
    def hello():          # ← 没有 self
        print('你好')
把 hello() 定义成不带参数，但 Python 调用对象方法时，会自动把对象自己传进来作为第一个参数：

c = C()
c.hello()
背后实际执行的是：

C.hello(c)    # ← 把 c 传进去了
hello() 说："我明明没要参数，怎么给我塞了一个？" → 报错。
        """


# 看正确的方法：
class C:
    def get_self(self):
        print(self)


c = C()
print(c.get_self())
# --->  <__main__.C object at 0x0000026B63B3AED0> 打印的其实是类C的实例对象小c的内存地址。
# 因为self就是指向对象本身的一个引用，所以打印self就会显示对象的内存地址。
print(c)
# ---> <__main__.C object at 0x0000026B63B3AED0> 打印的也是类C的实例对象小c的内存地址。

# 因为python的类，有很多对象。调用对象的时候，怎么知道调用的是哪一个呢？这时候就把要调用的对象当作参数传入类的方法里，就可以知道是哪一个对象在调用类了。
