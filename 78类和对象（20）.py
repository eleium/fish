# 类装饰器：把类当作参数传入一个函数
#装饰器：把函数当参数传入另一个函数

#@deco装饰器
# def foo(): 
# pass
# 等价于：foo = deco(foo)

# @deco类装饰器
# class C:
# pass
# 等价于：C = deco(C)

#装饰器就是一个函数，它接收一个对象（函数或类），然后返回另一个对象。
# @deco 只是语法糖，自动帮你完成“被装饰的东西 = deco(被装饰的东西)”这个赋值操作。

#有语法糖的时候，用@表明装饰器的身份；
# @deco
# def foo():
    # pass

# 没有语法糖的时候，装饰器就是一个普通函数调用，手动完成“把函数/类传给装饰器，然后把返回值赋值回去”这个操作。
#def foo():
    # pass
# foo = deco(foo)

#@ 只是帮你省了一行赋值代码
# @deco 这个写法，本质上就是 Python 替你做了两件事：
# 正常定义后面的函数/类（比如 def foo 或 class C）
# 自动执行 foo = deco(foo) 或 C = deco(C)
# 没有 @，你就自己写这一行赋值。


# 装饰器可以拦截函数的调用，就是装饰。装饰器也可以作用到类上面。：


def report(cls):
    def oncall(*args, **kwargs):
        print("hi,我要开始实例化对象啦。。。")
        _ = cls(*args, **kwargs)
        print("hi，实例化完成了。")
        return _

    return oncall


@report
#把自定义的函数report()变成装饰器
#装饰类的结果通常是：当你用这个类创建实例时，会先经过装饰器的处理。
class C:
    pass
#经过装饰，其实相当于：
# C = report(C)    把类 C 作为参数传给 report 函数，然后把返回值重新赋值给 C

c=C()
#--->hi,我要开始实例化对象啦。。。
    #--->hi，实例化完成了。

#当执行 c = C() 时：
# C 现在指向 oncall 函数
# 调用 oncall()
# 打印 "hi,我要开始实例化对象啦。。。"
# 执行 _ = cls(*args, **kwargs)，这里的 cls 是原来的类 C（被装饰前那个空的类），所以 cls() 创建了一个实例
# 打印 "hi，实例化完成了。"
# 返回这个实例，赋值给 c

#如果类C不是空的，有构造函数的话，上面的_=cls(*args,**kwargs):的参数就起作用了：

@report
class C:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        print('构造函数被调用了~~')

c=C(1,2,3)
#--->hi,我要开始实例化对象啦。。。
#--->构造函数被调用了~~
#--->hi，实例化完成了。