# property()函数：
# class property(fget=None,fset=None,fdel=None,doc=NOne)，这三个参数的意思就是 读取，更改和删除。默认是None。
# 说是函数，其实是类，是python 的内置类，例如：int,str,dict,list,都是内置类（class,),
# 不用首字母大写，那是自己定义类时才会用的驼峰命名方法（pep8的规定）

# property()函数，返回一个property的属性对象. property() 是 Python 的一个内置函数，用来把类里的方法“伪装”成属性调用。


class C:
    def __init__(self):
        self._x = 250
        # 把这个变量私有，有意隐藏起来，内部使用

    def getx(self):
        # 定义一个getx函数，返回self._x=250
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    # j将上面的三个函数当作参数，传递到proprety()函数里，当作这个函数的属性，可以调用，拿到它的返回值，给到x属性去

    x = property(getx, setx, delx)


c = C()
# 此时，给对象c写入x的值，就会影响_x
print(c.x)
# --->250
c.setx(520)
# 等价于c.x=520
print(c.__dict__)
# --->{'_x':520}

del c.x
print(c.__dict__)
# --->{}  变成空的属性啦
print("-" * 88)


class D:
    def __init__(self):
        self._x = 250

    def __getattr__(self, name):
        if name == "x":
            return self._x
        else:
            super().__getattr__(name)

    def __setattr__(self, name, value):
        if name == "x":
            super().__setattr__("_x", value)
        else:
            super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == "x":
            super().__delattr__("_x")
        else:
            super().__delattr__(name)


d = D()
print(d.x)
d.x = 520
print(d.__dict__)
# --->{'_x':520}
del d.x
print(d.__dict__)
# ---->{}


# 装饰器的原理，就是传入函数为参数来实现的。这也是property()函数的经典应用。例如：把property()当作装饰器使用，把创建只读属性的工作就变得很简单
class E:
    def __init__(self):
        self._x = 250

    @property
    def x(self):
        return self._x


e = E()
print(e.x)
# --->250

# e.x=520
# print(e.x)
# --->AttributeError: property 'x' of 'E' object has no setter

# 装饰器实际上就是一个语法糖，以下是它的实现原理：


class E:
    def __init__(self):
        self._x = 250

    def x(self):
        return self._x

    x = property(x)


# 只定义了properyt()的第一个参数，即fget参数，另外两个参数fset,fdel都是默认参数None,表示不能改写，不能被删除，只能被读取。

e = E()
print(e.x)
# e.x = 520
# print(e.x)
# ---->AttributeError: property 'x' of 'E' object has no setter
# 不能更改。

# 如果用@property()装饰器，使用多个参数，那么这么写：


class E:
    def __init__(self):
        self._x = 250

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

# @property 本身默认就是 getter,所以第一个不需要写@x.getter

e=E()
print(e.x)
#--->250
e.x=520
print(e.x)
#--->520
print(e.__dict__)
# --->{'._x':520}
del e.x
print(e.x)
#报错：AttributeError:"E" object has no attribute '_x',Did you main 'x'? 应为刚刚e的x属性已经被deleter了，而self._x=x,x属性已经被删除。
    
print(e.__dict__)
#--->{}



#语法糖（Syntactic Sugar）指的是编程语言中为了让你写代码更舒服、更简洁而设计的一种语法。它不会带来新的功能，只是把原本繁琐、复杂的写法变得"甜甜的"、更容易理解。

# 简单说：语法糖 = 一种更甜、更简单的写法，背后还是原来的老味道。

