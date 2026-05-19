# 与运算相关的魔法方法
# 两个字符串相加，不是拼接，而是统计两者的字符个数之和
class S(str):
    def __add__(self, other):
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
当你执行 s1 + s2 时，Python期望的返回值是两个对象相加的值（在这个例子中是长度之和）。
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
    def __add__(self, other):
        return NotImplemented
        # NotImplenmented:是内置的值。表示这个返回值是未实现的。
        # s1 返回 NotImplemented 的核心作用是**“主动放弃处理权，请求 Python 尝试另一种运算方式”**。
        # 具体来说，它在运算符重载机制中扮演了**“交通指挥员”**的角色，告诉 Python：“我（左边的对象）不知道该怎么和右边的对象相加，请你去问问右边的对象有没有办法。”


class S2(str):
    def __radd__(self, other):
        return len(self) + len(other)


s1 = S1("Apple")
s2 = S2("orange")
print(s1 + s2)
# --->11   Apple 和 orrange的字符个数之和，即（len(self)+len(other)

# 第一点： s2实现了__radd__()方法。
# 第二点：s1和s2的类型不同（类的来源）
# 第三点：s1不能实现__add__()方法。否则会优先执行s1的__add__()方法。

print(type(s1), type(s2))
# ---><class '__main__.S1'>  <class '__main__.S2'>，这是两个不同的类的实例。

# 为什么需要“类型不同”这个条件？这与 Python 的运算符重载机制有关：
# 如果类型不同：
# Python 先尝试调用左侧对象（s1）的 add 方法。
# 如果 s1.__add__ 返回 NotImplemented（表示“我不知道怎么和你加”），
# Python 才会去尝试调用右侧对象（s2）的 radd 方法。

# 如果 s2 定义了 radd，就会执行它。
# 关键点：radd（反向加法）的设计初衷就是为了处理不同类型之间的运算，
# 或者当左侧对象无法处理右侧对象时的一种“补救措施”。


# 以 i 开头的 增强赋值运算，进行的是 运算兼赋值的操作：跟算术运算符是对应的：
# s1 += s2 就等于 s1 = s1.__iadd__(s2) ,参数是s2, 即修改自身，自我赋值


class S1(str):
    def __iadd__(self, other):
        # 这个魔法方法就是 重写iadd方法，然后下一行返回一个值。
        return len(self) + len(other)


s1 = S1("apple")
s2 = S2("orange")

s1 += s2
# s1++s2，其实就是s1.__iadd__(s2),而这个方法执行的结果是：len(s1) + len(other),即：len('applei') + len('orrange')=12,
# 最后，这个12被赋值给s1。就是s1=s1.__iadd__(s2)
print(s1)
# ---->11
print(type(s1))
# ---><class 'int'> 变成了int类型

# 如果左侧的对象没有__iadd__()方法，那么python就会寻找__add__()或者__radd__()方法
s2 += s2
print(s2)
# --->orangeorange
print(type(s2))
# ---><class 'str'>

# Python 遇到 s2 += s2, 首先尝试调用左侧对象 s2 的 iadd 方法：s2.__iadd__(s2)。
# 关键点：你的 S2 类中没有定义 iadd。
# 又因为s2和s2都是用一个类S2的实例，所以python不会去运行s2的方法：__radd__().

# 因为 S2 继承自 str，Python 会去父类 str 中寻找 iadd。
# 字符串是不可变类型，在 Python底层实现中，str 的 iadd 通常直接回退（fallback）到调用 add。也就是说，对于不可变对象，a += b 等价于 a = a + b。
# 所以，表达式变成了 s2 = s2 + s2。

# Python 尝试调用 s2.__add__(s2)。
# 关键点：你的 S2 类中也没有定义 add。

# Python 再次去父类 str 中寻找 add。
# str.__add__ 的功能是字符串拼接。

# 所以，'banana' + 'banana' 结果是 'bananabanana'。
# 最后赋值给 s2。

print("-" * 88)


class ZH_INT:
    def __init__(self, num):
        self.num = num

    def __int__(self):
        try:
            return int(self.num)
        except ValueError:
            #fmt:off
            zh = {"零": 0,"一": 1,"二": 2,"三": 3,"四": 4,"五": 5,"六": 6,"七": 7,"八": 8,"九": 9,
                "壹": 1,"贰": 2,"叁": 3,"肆": 4,"伍": 5,"陆": 6,"柒": 7,"捌": 8,"玖": 9,
            }
            #fmt:on
            result = 0
            for each in self.num:
                if each in zh:
                    result += zh[each]
                else:
                    result += int(each)
                result *= 10
            return result // 10


n = ZH_INT("五二零")

print(int(n))
#--->520

