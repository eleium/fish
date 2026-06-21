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

"""这体现了"组合"的概念
这就是面向对象编程中的组合（Composition）：

Garden 类"拥有"了 Turtle、Cat、Dog 的实例
Garden 通过组合其他类的对象来构建自己的功能
这是一种"has-a"（有一个）的关系：花园有乌龟、有猫、有狗

 在你的代码中的作用
python
def say(self):
    self.t.say()  # 调用 t 属性（Turtle实例）的 say 方法
    self.c.say()  # 调用 c 属性（Cat实例）的 say 方法
    self.d.say()  # 调用 d 属性（Dog实例）的 say 方法
        """


# 验证self的方法：
class C:
    def get_self(self):
        print(self)


c = C()
print(c.get_self())
# --->__main__.C object at 0x0000020EA0E0EA90>

print(c)
# --->__main__.C object at 0x0000020EA0E0EA90>
# 两者完全一样，说明实例化对象小c就是类C 的实例对象的一个方法。
# self的作用，就是让实例化对象绑定类的方法。因为类的对象有多个，用self来区分到底是哪一个来调用了类的方法。
# 等同于：将实例化对象c，当作参数传入类的方法中。
print(C.get_self(c))
# --->__main__.C object at 0x0000020EA0E0EA90>

# 不同的实例对象可以有不同的属性。可以有不同的方法,但是要用types.MethodTyupe绑定
"""import types

class Turtle:
    head = 1
    def crawl(self):
        print('乌龟爬行')

t1 = Turtle()
t2 = Turtle()

# 给 t1 单独加一个 t2 没有的方法
def sing(self):
    print(f'我有{self.head}个头，我会唱歌')

t1.sing = types.MethodType(sing, t1)

t1.sing()   # ✅ 输出：我有1个头，我会唱歌
t2.sing()   # ❌ AttributeError: 'Turtle' object has no attribute 'sing'
"""

d = C()
d.x = 100
c.x = 200
# 用 __dict__属性可以查看实例对象绑定的属性和方法:用字典的方式保存属性和值
print(d.__dict__)
# --->{'x': 100} 即实例对象d的属性x绑定了值100
d.y = 300
print(d.__dict__)
# -->{'x':100,'y':300}


# 绑定：通过类里面的方法，设置对象自己的属性，方法是大家的，属性是自己的。用self来建立绑定：
class C:
    def set_x(self, v):  # 定义方法 set_x，接收两个参数
        self.x = v  # 给对象添加一个属性 x，值设为 v

        """self.x = v 到底是什么？
拆开看：

部分	 意思
self	当前调用这个方法的对象（比如 c）
.x	    给这个对象创建（或修改）一个叫 x 的属性
= v	    把参数 v 的值赋给 x
所以 self.x = v 就是：给当前对象添加一个属性叫 x，值为 v。

self.x 是一个属性，= 是赋值操作，整行是在创建一个实例属性。

        """


c = C()
# c.set_x()#-->{}空的。
c.set_x(400)
print(c.__dict__)
# -->{'x':400}

print(c.x)
# --->400
# 说明了 self.x=v==c.x=400  方法set_x绑定了属性x .self==c.
# 结果：c 这个对象现在有一个属性 x，值是 400。


"""
代码	含义
self.x	属性，当前对象的 x 属性
= v	赋值操作
self.x = v	给当前对象添加/修改属性，不是方法，也不是操作符号
set_x 这个方法的作用就是：给对象添加一个属性。你每调一次 c.set_x(某个值)，就给 c 设置了一个新的 x 值。
"""


# 类与字典的转化：
class C:
    pass


C.x = 100
C.y = "小甲鱼"
C.z = [1, 2, 4]
print(C.x)  # -->100
print(C.y)  # -->小甲鱼
print(C.z)  # -->[1,2,4]
# 以上都是用类的属性。

# 换成字典的方式：
d = {}
d["x"] = 100
d["y"] = "小甲鱼"
d["z"] = [1, 2, 4]
print(d["x"])  # -->100
print(d["y"])  # -->小甲鱼
print(d["z"])  # -->[1,2,4]
# 没有用类的方法简单。

# 其实应该用类的实例对象来演示：
c = C()
c.x = 100
c.y = "小甲鱼"
c.z = [1, 2, 4]
print(c.x)  # -->100
print(c.y)  # -->小甲鱼
print(c.z)  # -->[1,2,4]
