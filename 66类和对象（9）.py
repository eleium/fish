# 与运算相关的魔法方法
# 两个字符串相加，不是拼接，而是统计两者的字符个数之和
class S(str):
    def __add__(self, other):  #
        # self.other=other  强行给self绑定一个other属性在本次执行过程中没有必要。
        return len(self) + len(other)


s1 = S("python")
s2 = S("fishC")
print(s1 + s2)  # --->11

print(s1 + "hello world")
# --->17
print(s2 + "hello world")
# --->16
print("hello world" + s2)
# --->hello worldfishC
# 说明：+ 号左侧操作数调用其 __add__ 方法，右侧作为参数传入。
#      'hello world' 是 str 类型，调用内置 str.__add__ 执行拼接。

# s1+s2==s1__add__(s2)
# 其他运算相关的魔法方法，也是同样的规则
"""
在 Python 的魔法方法 add(self, other) 中：
self：代表调用该方法的对象（即加号 + 左边的对象）。
other：代表传入的参数（即加号 + 右边的对象）。

add 是一个运算符重载方法，它的职责是返回两个对象相加后的结果。
当你执行 s1 + s2 时，Python 期望得到一个返回值（在这个例子中是长度之和）。
self.other = other 只是在 s1 这个对象身上强行绑了一个属性叫 other，但这对于“加法运算”本身没有任何意义。
没有实际用途：

加法运算结束后，你通常只关心结果（即 return 的值）。
除非你在后续代码中专门去访问 s1.other，否则这行赋值操作就是多余的，甚至会污染对象的属性空间。

self 和 other 只是临时参数：它们在方法执行期间代表参与运算的两个对象，方法执行完就“消失”了。
不要随意给 self 加属性：在魔法方法中，除非你的业务逻辑明确要求记录这次运算的参与者，否则不要在 self 上通过 self.xxx = xxx 来存储临时数据。
专注返回值：add 的核心任务是 return 一个合理的结果。
所以，删掉 self.other = other 是完全正确且更专业的做法。
"""

# 只要用__add__()的方法重写加法的用途,就可以实现特定的功能。魔法方法的作用就是拦截。


print("_" * 80)


# 反运算：__radd__(self,other):当两个对象相加的时候，如果两侧的对象类型不同，并且左侧的对象没有定义__add__()方法，
# 或者定义了 __add__()方法，但是返回值是NotImplemented,那么python 就会去右侧找对象是否有__radd__()方法。
class S1(str):
    def __add___(self, other):
        return NotImplemented
        # NotImplenmented:是内置的值。表示这个返回值是未实现的。
