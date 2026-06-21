# 作用域：一个变量可以被访问的范围。通常的，一个变量的作用域是它被赋值的代码位置来决定的。
# 局部作用域：一个变量的定义位置在一个函数里面，它的作用域就仅限于该函数中，被称为：局部变量
def myfunc():
    x = 520
    print(x)


myfunc()  # --->调用了myfunc()函数。

"""
因为 print(x) 在函数内部直接输出了,不需要 return。
关键区别:
print(): 直接在控制台显示内容
return: 把值返回给调用者,需要接收才能使用
"""


def myfunc2():
    x = 520
    return x


result = myfunc2()  # 不会自动输出
print(result)  # 输出: 520


# 有了return就是有了返回值，但是需要print才能显示输出。没有return就没有返回值，print就是None.
# 如果print(x)在函数内部，那么x是局部变量，会直接输出。如果print(x)在函数外部，那么x是局部变量，不会输出。
def myfunc2():
    x = 520


# print(x)

result = myfunc2()  # 报错：NameError: name 'x' is not defined因为x是局部变量，在函数内部定义，在函数外部无法访问。

# 如果是在任何一个函数的外部定义的一个变量，它就是全局变量。

x = 88


def myfunc3():
    print(x)


myfunc3()  # --->88


# 具有全局作用域的变量，可以在任何地方访问。
# 如果局部变量与全局变量同名，那么局部变量会在作用域里面覆盖全局变量，即在局部变量的函数里，访问的是局部变量。外部还是全局变量。
def myfunc5():
    x = 520
    print(x)  # 内部的局部变量会覆盖外面的全局变量


myfunc5()  # --->520，内部访问的是520，局部变量。
print(x)  # --->88，外部的全局变量不受影响。

print('-' * 88)
# 如果函数调用使用了全局变量，那么函数就会访问全局变量。
x = 99
print(id(x))  # --->140717333673464


def myfunc6():
    print(id(x))


myfunc6()  # -->140717333673464与全局变量的id一样。

# 用global()来声明全局变量：强制函数访问并改变全局变量。非常不提倡！！！！！
x = 999


def myfunc7():
    global x  # 声明这是全局变量
    x = 520  # 改变全局变量的值
    print(x)


myfunc7()  # --->520
print(x)  # --->520全局变量被函数内部的global()强制改变了。会造成混乱。


# 嵌套函数：
def funcA():
    x = 520

    def funcB():
        x = 880
        print('在funcB函数中，x=', x)

    print('在funcA函数中，x=', x)


# funcB()  # 报错：NameError:name 'funcB' is not defined.被嵌套的函数不能直接调用。
funcA()  # --->520
print('-' * 88)


# 要调用被嵌套的函数funcB(),就要在函数funcA()里面调用funcB():
def funcA():
    x = 520

    def funcB():
        x = 880
        print('在函数funcB中，x=', x)

    funcB()
    print('在函数funcA中，x=', x)


funcA()  # --->在函数funcB中，x= 880


# --->在函数funcA中，x= 520

# 内部函数可以访问外部函数的变量，但却不能修改它。
# 要想内部函数访问并修改外部函数的变量，用nonlocal来声明：
def funcA():
    x = 520

    def funcB():
        nonlocal x  # 声明：内部函数调用并修改了外部函数的变量x
        x = 880
        print('在函数funcB中，x=', x)

    funcB()
    print('在函数funcA中，x=', x)


funcA()  # --->在函数funcB中，x= 880
# --->在函数funcA中，x= 880 ,外部变量x的值被内部函数修改了，也变成了880


# LEGB规则：掌握了LEGB规则，就可以理解变量作用域了。相当于掌握了python的变量的解析机制
# L:local 局部作用域  E:enclosed 嵌套函数的外层函数的作用域  G:global 全局作用域  B:built-in 内置作用域

# 当局部作用域与全局作用域冲突时，python会用局部作用域覆盖全局作用域，除非你用global来声明，就是用的时全局作用域。
# 当函数嵌套时，局部作用域又会覆盖外层函数的作用域，除非你用nonlocal来声明，就是用的时外层函数的作用域。

# B built-in. python内置的变量名，很容易被覆盖：
str = '轻易的改变了str的性质：现在是一个变量名了'
str(520)  # --->>TypeError: 'str' object is not callable, 因为str被定义为变量名，而不是函数了。str原来的作用是把数值转换成字符串，现在被定义为变量名，所以不能再调用它。
