# 多态：面向对象编程的第三个特征，指的是对象可以按照相同的接口被各种对象所调用，从而产生不同的结果。
# 同一个运算符、函数或对象，在不同的场景具有不同的功效的技能。比如：len()函数，在字符串和列表中，长度不同。
len("hello")
len([1, 2, 3])
len({"name": "tom", "age": 18})
# 得出的结果分别是 5，5个字符。3，3个元素 ，2，两个键。
# 说明len()函数是个多态的函数。python还有很多多态的函数。接口不变，但是可以根据不同对象进行不同的工作。
# 类继承的多态：如果对父类的方法或属性不满意，可以用子类的方法或属性覆盖父类，这个叫重写，也就是继承的多态性。


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Square(Shape):
    def __init__(self, length):
        super().__init__("正方形")
        self.length = length

    def area(self):
        return self.length * self.length


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("三角形")
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


s = Square(20)
print(s.name)
print(s.area())

c = Circle(40)
print(c.name)
print(c.area())

t = Triangle(3, 4)
print(t.name)
print(t.area())

# 都继承自Shape类。但是又各自重写了构造函数和area()方法。


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我是一只猫咪,我今年{self.age}大了，叫{self.name}")

    def say(self):
        print("喵喵~")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我是一只小狗，我叫{self.name}，我今年{self.age}岁啦")

    def say(self):
        print("汪汪~")


class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我是一只小猪，我叫{self.name}，我今年{self.age}岁啦")

    def say(self):
        print("哼哼~")


cat = Cat("糖宝", 5)
dog = Dog("旺财", 3)
pig = Pig("花花", 7)


def animal(x):
    # 定义一个叫animal的函数，而不是类。注意小写。要传入的参数是x,这个x可以是任意字符，等待调用时传入就可以了。
    x.introduce()
    x.say()


print(animal(cat))
# 调用函数animal，传入的参数是类的对象cat
# --->我是一只猫咪，我今年5大了，叫糖宝
# --->喵喵~
# 以上是调用函数

print(animal(pig))
print(animal(dog))
# 都是调用函数

print(cat.introduce())
print(cat.say())
# 这是 实例化对象，是Cat()类。

# 说明animal()函数是多态的，传入不同的参数，输出不同的内容


class Bicyle:
    def introduce(self):
        print("我曾經跨过山海，也曾經人山人海")

    def say(self):
        print("搏一搏，單車變摩托")


# 因爲上面Bickke類，有introduce()和say()方法，所喲可以被animal()函數調用：

bick = Bicyle()
# 实例化一个对象

print(animal(bick))
# --->我曾经跨过山海，也曾经人山人海
# --->搏一搏，单车变摩托
# 把这个实例化对象bick当作animal()函数的参数传进去，调用这个函数

# 以上的例子表明：animal()函数，不管传入的是啥，只要有 introduce()和say()方法，都可以接受，并执行。
