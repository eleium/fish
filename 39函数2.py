# 函数的参数：
# 1：位置参数，一般情况下，实参是按照形参的顺序来匹配的
def myfunc(s, vt, o):
    return "".join((o, vt, s))


# 把三个参数颠倒顺序后拼成字符串。


result = myfunc("hello", "world", "python")
print(result)
# --->pythonworldhello

"""
"".join((s, vt, o)) 的意思是：
"" - 空字符串，作为连接符
.join() - 字符串方法，用于将序列中的元素连接成一个字符串
(s, vt, o) - 这是一个元组，包含三个参数
为啥这么写？
join() 方法只接受一个参数（可迭代对象），不能直接传多个参数
所以要把 s, vt, o 打包成元组 (s, vt, o) 传进去
结果："hello" + "" + "world" + "" + "python" = "helloworldpython"
"""


# 使用关键字参数来解决传入多个参数时的位置问题
def myfunc(s, vt, o):
    return "".join((o, vt, s))


result = myfunc(s="python", vt="打了", o="我")
print(result)
# --->我打了python

# 如果混用位置参数和关键字参数，那么位置参数必须要在关键字参数的前面：
# result = myfunc(o='python', '爱', '我')#--->SyntaxError: positional argument follows keyword argument
result = myfunc("我", vt="爱", o="python")
result2 = myfunc("我", o="python", vt="爱")
print(result, result2)


# 默认先传入的参数是位置参数，并与形参匹配。


# python 有默认参数。如果调用参数的时候没有传入实参，就用默认参数
def myfunc(s, vt, o="python"):
    # 给参数o指定了一个默认值：'python'
    return "".join((o, vt, s))


print(myfunc("我", vt="爱"))
# 既然创建参数的时候就指定了默认参数o='python',那么在调用参数的时候就不要再传入参数o了。
# 如果非要传入第三个参数，那么就会覆盖默认参数。
print(myfunc("我", vt="学习", o="java"))
# --->java学习我

# 小知识：在用help()函数的时候，比如：
help(abs)
# --->abs(x, /)
# Return the absolute value of the argument.
help(sum)
# --->sum(iterable, /, start=0)

"""
以上两个例子的运行，都有斜杠/，它的意思就是： 斜杠/前面的参数必须是位置参数"""

abs(-1.5)
# abs(x),而不能写成 abs(x=1.5),即关键参数不能在/的前面。
sum([1, 2, 3], 4)
sum([1, 2, 3], start=4)
"""
start 是 sum() 函数的关键字参数，表示起始值。
默认 start=0，即 sum([1,2,3]) = 0+1+2+3 = 6
指定 start=4，即从4开始累加：4+1+2+3 = 10
两种写法等价：
位置参数：sum([1, 2, 3], 4)
关键字参数：sum([1, 2, 3], start=4) ← 更清晰

而sum()的默认参数是iterable:一定是可迭代对象：list,dict,set，tuple,range,string等等。
不能是sum(1,2,3)这是整数型。
"""


# 斜杠/的作用也可以用在自己定义的函数里：注意，斜杠要加逗号。
# ✅ 斜杠 / 表示它前面的参数只能用位置参数传递，不能用关键字参数。
def abc(a, /, b, c):
    print(a, b, c)


result = abc(2, b=3, c=4)
print(result)


# 因为 abc() 函数没有 return 语句，默认返回 None。
def abc(a, /, b, c):
    return a, b, c


result = abc(2, b=3, c=4)
print(result)
# --->(2,3,4)且斜杠前面是位置参数，斜杠后面是关键字参数。


# 用*号可以指定右侧只能是关键字参数，但是左侧可以是位置参数，也可以是关键字参数。


def myfunc(a, *, b, c):
    return a, b, c


result = myfunc(a=3, b=4, c=5)
# result2=myfunc(3,b=4,5)报错，因为a是位置参数，b是关键字参数，c不是关键字参数。而*后面的必须都是关键字参数。
