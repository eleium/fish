"""
用函数把代码打包起来,实现重复的功能，1，最大程度的实现代码的重用，减少代码冗余。
2，将不同功能的代码进行封装，分解，从而降低结构的复杂度，提高代码的可读性。
python 有BIF 内置的函数，比如print(),sorted()排序函数，input()接收输入的函数
还可以自己创建和调用函数"""

s = {1, 2, 3}
s.update("python")  # 添加元素。
print(s)  # --->{'p','y','t','h','o','n',1,2,3}


# 用def语句来定义函数
def myfunc():
    pass  # 代码块，占位符。函数体，函数的主体，函数的实现。每次调用函数都会执行的代码


# 调用函数的方法非常简单：直接输入函数名，然后加括号，就可以了：
# myfunc()


def myfunc_1():
    for i in range(3):
        print("I love python")


myfunc_1()  # --->调用myfunc()函数


# --->I love python
# --->I love python
# --->I love python    执行结果：打印3遍 I love python


# 通过函数的参数，来实现函数的功能的定制：函数的参数，就是函数的输入
def myfunc_2(name):
    for i in range(3):
        print(f"I love {name}")


myfunc_2("chinese")  # 传入参数：chinese


# --->I love chinese
# --->I love chinese
# --->I love chinese


# 函数可以多参数：
def myfunc_3(name, times):
    for i in range(times):
        print(f"I love {name}")


myfunc_3("python", 2)  # 传入参数'python',并设置参数times为2


# --->I love python
# --->I love python

# 参数分为形式参数和实际参数两种。形式参数：定义函数时定义的参数。 实际参数：调用函数时传递给函数的参数。
# 上面例子中定义myfunc()时的参数 name 和 times,就是形参。而调用函数时传入的参数"python'和2 就是实参。


# 函数的返回值：函数的返回值，就是函数执行完毕之后，返回给调用它的代码的值。用return语句来实现自定义的函数的返回值。
def div(x, y):
    z = x / y
    return z


result = div(10, 2)
print(result)


def div(x, y):
    return x / y
    # print(x / y)


result = div(8, 4)
# return 后面的代码不会执行：第72行 print(x / y) 永远不会运行
# 没有打印返回值：第75行调用 div(8, 4)，但没有用 print() 显示结果
print(result)
# --->2.0


# 或者用print()直接包裹调用的函数： print(div(8, 4))


def div(x, y):
    if y == 0:
        return "除数不能为零!"
    else:
        return x / y


print(div(9, 3))
# --->3.0
print(div(9, 0))
# --->除数不能为零!


def div(x, y):
    if y == 0:
        return "除数不能是0！！"
    return x / y


print(div(9, 3))
# 传入的是非0的除数，所以if y ==0不成立，直接return x/y,即没有else语句也成立。


# 如果一个函数没有通过return语句返回显示内容值，那么这个函数在执行完代码后会返回None。
def myfunc_4():
    pass


print(myfunc_4())
# 函数myfunc()执行完毕，没有显示返回值，所以返回None
# ---->None
"""
函数就像一台机器：
有 return：机器加工完，给你返回一个结果
没 return：机器干完活，啥也不给，返回 None（空值）
你去餐厅点菜（调用函数）
厨师做完给你端上来（return 返回值）
如果厨师啥也不给（没 return），你就拿到空气（None）
"""
