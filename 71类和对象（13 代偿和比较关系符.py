# __contains__(self,item): 判断成员关系的检测.对应的运算符是in 和 not in
# contains: 包含的意思。对象c包含3   c.__contains__(3)

# Parameter 是参数（形式参数，简称形参），指函数定义中声明的变量。
# Argument 是实参（实际参数，简称实参），指调用函数时实际传递给参数的值或表达式。

# 简单区分：
# Parameter 是“占位符”（定义时）
# Argument 是“具体值”（调用时）


class C:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        self.item = item
        print("hi~~")
        return item in self.data


c = C([1, 2, 3, 4, 5])
print(3 in c)
# 3就是item
# --->True

# 当执行 print(3 in c) 时：
# 触发 c.__contains__(3)
# 执行 3 in [1,2,3,4,5] → 结果是 True
# return True 返回给调用方
# 最终打印 True


"""
return 可以返回 Python 中的任何对象，因为 Python 中一切皆对象。

常见返回类型：
分类	                 示例
基本数据类型	         int, float, bool, str, None
容器类型	             list, tuple, dict, set
函数/方法	             函数本身可以作为返回值（闭包）
类/实例	                 返回对象实例
表达式结果	              a + b, x > y, item in data 等
任意自定义对象	          自己定义的类的实例
None	                没有显式 return 时，默认返回 None

代码示例：
python
def f1(): return 42                # int
def f2(): return 3.14              # float
def f3(): return True              # bool
def f4(): return "hello"           # str
def f5(): return [1, 2, 3]         # list
def f6(): return {'a': 1}          # dict
def f7(): return None              # None
def f8(): return f1                # 返回函数本身
def f9(): return C([1, 2])         # 返回类的实例
def f10(): return 3 > 5            # 表达式结果 → False

关键点：
return 不限制类型，同一函数可以返回不同类型的值（虽然不推荐）
没有 return 语句的函数，默认返回 None
return 可以不带值（单独写 return），效果也是返回 None
"""


# 代偿：当把对象放到for等迭代环境中时，python就会去寻找__iter__()、__next__()迭代工具。
# 如果没有找到，python就会去寻找__getiter__()魔法方法，来替代__iter__()和__next__()方法，进行迭代，这就是代偿。
# 如果没有__contains__(),但是又使用了in 或者 not in 来进行成员判断，那么python就会寻找__iter__()和__next__()magic method来代偿：

print("-" * 88)


class C:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        print("Iter", end=" ->")
        self.i = 0
        return self

    def __next__(self):
        print("Next", end=" ->")
        if self.i == len(self.data):
            raise StopIteration
        item = self.data[self.i]
        self.i += 1
        return item


c = C([1, 2, 3, 4, 5])
print(3 in c)
# --->hi~~
# --->Iter->Next->Next->Next->True
# --->True

# 如果结果是False,将出现6次的Next:
# 列表有 5 个元素（索引 0,1,2,3,4）
# 需要 5 次 __next__() 取出这 5 个元素
# 第 6 次 调用 __next__() 时，self.i == 5 == len(self.data)，触发 StopIteration,这也算一次。
# in 运算符收到 StopIteration 后才知道"遍历完了，没找到"

# self.i 是索引（下标）
# item 是通过索引取出的值
# __next__() 返回的是 item（值）

# in 运算符会主动调用 iter() 和 next(),并且在背后驱动着迭代
# 不需要你写 for 循环，in 替你做了循环的工作

# __next__() 的作用
# 每次被调用，返回下一个元素
# 它通过 self.i 记住"当前走到哪个位置了"
# 它不自己循环，而是每次只返回一个元素，然后等待下一次被调用


# //@#￥￥￥%%……&*&**（（（写一段代码，一定要先明确这段代码要实现的什么功能，什么目的，然后才能在写代码的时候，调用不同的工具。
# 不知道代码要实现的功能，就没法写，没法用。这是一个现有果，后有因的过程。


# 如果连__iter__()和__next__()魔法方法都没有，那么也可以用__getattr__()方法（获取对象的属性）：

# __getattr__()与__getiter__()魔术方法	触发时机	            参数含义	                   用途
# __getattr__(self, name)	          访问不存在的属性时	    name = 属性名（字符串）	        动态处理属性
# 是针对属性名（attribute name)  只有当正常属性查找失败时才被调用

# __getitem__(self, key)	          使用索引访问时 obj[3]	    key = 索引值（整数/切片等）	    实现下标访问
# 针对索引/键（index/key）使用 obj[3] 或 obj["name"] 时触发


class C:
    def __init__(self, data):
        self.data = data

    # def __getiter__(self,index):
    # in 运算符需要对象可迭代（有 __iter__ 方法）或支持索引（有 __getitem__ 方法）
    # 你的类既没有 __iter__，也没有 __getitem__
    # 只有 Python 不认识的 __getiter__。只有iter()函数和__iter__()魔术方法，没有__getiter__()方法。

    def __getitem__(self, index):

        print("Getitem", end="->")
        return self.data[index]


c = C([1, 2, 3, 4, 5])
print(3 in c)
# --->Getitem->Getitem->Getitem->True

# bool测试：如果碰到了bool()函数，python 将去寻找__bool__()魔法方法来做判断：


class D:
    def __bool__(self):
        print("BOOL")
        return True


d = D()
print(bool(d))
# --->BOOL 表示调用bool()函数后，被__bool__()给拦截啦
# --->True

# 如果没有__bool__()这个魔法方法，python 就会去寻找 __len__()这个魔法方法
# 如果有的话，这个方法返回的值是非零的，表示True,否则表示False。这是__bool__()方法的代偿


class D:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        print("LEN")
        return len(self.data)


d = D("python")
# 因为构造函数的形参parameter 有data这一项，所以实例对象必须传入实参argument ,也就是data
print(bool(d))
# --->LEN
# --->6因为len(self.data)=6,是非零的。所以是True.如果对象传入的是空，d=D(" "),长度是零，bool的判断就是false
# --->True
d = D(" ")
# 空格也是len(空格)=0
print(bool(d))


# 跟比较运算相关的魔法方法：<,>,<=, >=
# <  __lt__(self,other)
# <= __le__(self,other)
# >  __gt__(self,other)
# >= __ge__(self,other)
# == __eq__(self,other)
# != __ne__(self,other)

print("-" * 88)


class S(str):
    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __eq__(self, other):
        return len(self) == len(other)


s1 = S("PythoN")
s2 = S("python")
print(s1 < s2)
# --->False
print(s1 > s2)
# --->False
print(s1 == s2)
# --->True
# 以上判断的都是字符串的长度是否一样len(self)和len(other)

print(s1 != s2)
# --->True
# 注意，虽然__eq__()magic method拦截了 == 的判断，但是并不等于 不等值的结果自动取得等值的相反结果
# 因为类S里面没有__ne__()魔法方法，所以类S去向上找基类，那就是传统的比较结果。
# 而传统的字符串，比较的是字符串的编码值。所以PythoN != python, 结果是True.
print(s1 <= s2)
print(s1 >= s2)
# 同样的，这两个也是需要到基类里面，比较编码值。

# 如果不想比较某一个比较运算符，不想让某个魔法方法生效，可以直接在代码中写写上： None：


class S(str):
    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __eq__(self, other):
        return len(self) == len(other)

    __le__ = None
    __ge__ = None
    __ne__ = None


s1 = S("Python")
s2 = S("pycharm")
# print(s1 <= s2)
# --->TypeError: 'NoneType' object is not callable
# 就是不想让魔法方法__le__()实现操作，直接定义为：None:

#同样适用于上面的代偿实现：
class C:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        print("Iter", end=" ->")
        self.i = 0
        return self

    def __next__(self):
        print("Next", end=" ->")
        if self.i == len(self.data):
            raise StopIteration
        item = self.data[self.i]
        self.i += 1
        return item
    __contains__=None

c=C([1,2,3,4,5])
print(3 in c)
#--->TypeError: 'C' object is not a container
#因为有__contains_=None,就是告知，不希望有关系判断的操作存在。
# 同样也影响到 not in.

