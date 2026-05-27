# 当对象被索引的时候，python到底怎么做？
# python会调用一个叫： __getitem__(self,index)的魔法方法
# 这个魔法方法既可以操作单个的索引下标，也可以支持切片的索引范围


class C:
    def __getitem__(self, index):
        print(index)


c = C()
print(c[2])  # ---->2  这个2 是函数__getitem__(self,index)执行print(index)而得到的。
# 然后因为__getitem__()没有返回值，或者说返回值是None，所以会打印None

c[2]
# 对象c的第二个索引，被当作实参传给了形参index
# --->2

c[2:8]
# c[2:8]   # 自动变成 c.__getitem__(slice(2, 8, None)),然后slice的属性被当作实参，传入形参index,然后被print(index)打印出来。

"""
c[2:8] 当实例c被实例化为[2:8]的时候
    ↓
Python 自动转换为 c.__getitem__(slice(2, 8, None))
    ↓
在 __getitem__ 内部，可以通过 index.start、index.stop、index.step 拿到这三个值
"""

"""
对应规则：

切片语法	     slice() 调用	             含义
[2:8:2]	        slice(2, 8, 2)	            从2到8，步长2
[2:8]	        slice(2, 8, None)	        从2到8，步长默认1
[:8]	        slice(None, 8, None)	    从头到8，步长默认1
[2:]	        slice(2, None, None)	    从2到尾
[::2]	        slice(None, None, 2)	    从头到尾，步长2
[:]	            slice(None, None, None)	    全部元素
关键点：省略的参数用 None 代替。
"""
# 你可以把它们看作 Python 的“原住民”或“关键字级别的类型”。
# 总结：
# 我们自己写的类：用大写开头（class MyClass:）。
# Python 内置的基础类型：通常是小写（list、dict、str、int、float、slice 等）。

# --->slice(2:8,None)
# slice 是 Python 的一个 内置类（built-in type），专门用来表示切片。
# 你可以直接使用 slice() 构造函数创建它：

"""
slice(None, 5, 2) 括号里面的参数叫什么？
slice(None, 5, 2) 里面的参数 None、5、2 有统一的名称：
实参 (arguments)。
更具体地，它们是 位置实参 (positional arguments)，因为它们是按照 slice 构造函数的参数定义顺序 (start, stop, step) 来传递的。
这里容易混淆的一个点是：
当我们写 a[1:5:2] 时，1、5、2 叫做 切片索引 (slice indices)。
当我们写 slice(1, 5, 2) 时，1、5、2 叫做 传递给 slice 构造函数的参数。
"""
print("-" * 88)


class C:
    def __getitem__(self, index):
        print(index)


c = C()
s = "I love python"
s[2:6]
# --->love 字符串从2到6-1=5位的元素

s[slice(2, 6, None)]  # --->love
# s.xxx() 这种写法，是在调用字符串对象的实例方法，比如 s.upper()、s.find()。slice 不是字符串的方法,不能这么写：s.slice(2,6,None)
s[7:]
# --->python
s[slice(None, 7, None)]
# --->python

s[::4]
print(s[slice(None, None, 4)])
# --->Ivyn


# 为索引或切片赋值的操作的时候，就相反，会被__getitem__(self,index)magic method 方法所拦截


class D:
    """创建一个类似列表的容器类"""

    def __init__(self, data):
        # 构造函数，将传入的 data 保存为实例属性
        self.data = data

    def __getitem__(self, index):
        # 实现索引读取：d[3] 会调用这个方法,将得到索引下标的元素的值
        return self.data[index]

    def __setitem__(self, index, value):
        # 实现索引赋值：d[3] = 'x' 会调用这个方法，把传入的value值，赋值给列表d的下标为3的元素。
        self.data[index] = value


d = D(["a", "b", "c", "d", "e"])
print(d[3])  # 输出: d
# 类D的3个核心意义 ，与直接操作列表切片的区别：
# 1️⃣ 添加业务规则（拦截/校验）
# 你可以轻松地在存取时加入逻辑，而普通列表做不到：可以在代码中if index < 3，等规则。
# 2️⃣ 数据转换/副作用
# 可以在读写时自动转换格式，列表做不到：
# return self.data[index].upper()，直接得到大写后的元素
# 3️⃣ 改变底层存储（不暴露实现）
# 你今天用列表，明天想改成数据库、文件、网络API，使用类D的代码一行都不用改

# 以上就是类D封装的意义：要想访问对象列表，必须通过__getitem__()或者__setitem__()方法这两个入口。
# 并且通过这两个入口，可以增加规则，增加功能，方便使用等等。

d = D([1, 2, 3, 4, 5])
d[1]
# --->2
d[1] = 1
# 把下标为1的元素值改为1，原来的列表变为：[1，1，3，4，5]
d[1]
# --->1

d[2:4] = [2, 3]
print(d[::])
# --->[1,1,2,3,5]


class D:
    def __init__(self, data):
        # 将传入的 data 参数保存到实例的属性 self.data 中。
        self.data = data

    def __getitem__(self, index):
        # "索引访问方法"、"下标访问方法"
        return self.data[index] * 2
        # "实现 [] 操作符的方法"


d = D([1, 2, 3, 4, 5])
print(d[::])
# --->[1,2,3,4,5,1,2,3,4,5]
for i in d:
    print(i, end=" ")
# ---->2,4,6,8,10
"""
上面的代码的执行逻辑：
1. 获取 d 对象
2. 尝试调用 d.__iter__()
   ├─ 如果有 → 拿到迭代器，开始迭代
   └─ 如果没有 → 进入备用方案
3. 备用方案：尝试使用 __getitem__ 迭代
   ├─ index = 0
   ├─ 调用 d.__getitem__(0) → 成功则继续
   ├─ 调用 d.__getitem__(1) → 成功则继续
   └─ 直到捕获 IndexError → 停止
   """


# 使用for语句，针对可迭代对象的魔法方法：__iter__(self)和__next__(self)方法
# 这两个方法对应的BIF函数就是iter()和next()函数。（可迭代对象和迭代器的相关内容）
# 根据python的迭代协议：
# 如果一个对象定义了__iter__(self)魔法方法，那么它就是一个可迭代对象
# 如果一个可迭代对象定义了__next__(self)魔法方法，那么它就是一个迭代器
# 列表是一个可迭代对象，不是迭代器。因为它没有__next__()魔法方法。

x = [1, 2, 3, 4, 5]
print(dir(x))
# ---> ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__',
# '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
#  '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# next(x) 用next()函数直接调用列表x的
# TypeError: 'list' object is not an iterator 列表不是一个迭代器

# 可迭代对象定义了__iter__()魔法方法，只要调用这个方法，就会得到一个迭代器：
# 当使用迭代工具，比如for语句，对一个可迭代对象操作的时候

for i in x:
    print(i, end="-")
# for 语句执行的第一项工作，必然是把对象传入内置函数iter()中，并由此拿到一个相应的迭代器
# 只有拿到了这个迭代器，才拥有了所需要的__next__()魔法方法
# 然后再利用这个__next__()方法，进行真正的迭代操作

# 名称	        中文俗称	                别名
# iter()	    迭代器获取函数	        可迭代对象转换函数    将可迭代对象转为迭代器
# next()	    下一个元素获取函数	     迭代器取值函数        从迭代器取值（实际执行）
# __iter__()	迭代器方法	            获取迭代器魔法方法    返回自己
# __next__()	下一个元素方法	        迭代取值魔法方法      返回下一个元素，没有元素时抛出 StopIteration

# 用魔法方法__next__()得到迭代结果
_ = iter(x)
# 下划线表示临时变量，用完即毁。
while True:
    try:
        i = _.__next__()
    except StopIteration:
        break
    print(i, end=" ")
print()
"""
print() 的 end 参数详解
end 参数	 效果	例子
end='\n'	 换行（默认）	       print("A") → A\n
end='-'	    用短横线连接不换行  	print("A", end='-') → A-
end=' '	    用空格连接不换行       print("A", end=' ') → A
end=''	    无分隔，直接连	       print("A", end='') → A
"""
# 因为end=(' ')不换行，所以上面的代码执行后，结果在缓冲区，没有在终端里显示。只能在末尾加上一行：print()，才能显示，默认\n。直接回车没用，没有\n
# 因为for语句的print(i,end='-'),以-结尾但是不换行，所以与while语句的结果在终端里的同一行以前显示。

print("-" * 88)

# 创造一个迭代器对象：


class Double:
    def __init__(self, start, stop):
        self.value = start - 1
        # 从零开始。然后执行到对象的闭合值5-1=4
        #这一句的意义是：让后面的self.value+=1,让value开始递增，能 动起来。否则就死在那里了。
        self.stop = stop

    def __iter__(self):
        # 定义一个迭代器转换器，得到一个迭代器
        # 拥有了__iter__（）方法，Double的实例才会是一个可迭代对象
        return self

    def __next__(self):
        # 定义 从迭代器里取值，实现迭代操作
        if self.value == self.stop:
            raise StopIteration
            # 如果从迭代器里取得值与对象的结束下标相等，就抛出停止迭代。
        self.value += 1
        # 迭代对象的值递增
        return self.value * 2


d = Double(1, 5)
#(1,5)=slice(1,5,None) 从第1到第5的范围。
for i in d:
    print(i, end=" ")

#实例化对象d传入的value是start=1,stop=5，构造函数使得对象d的value属性是从0-5   这么些有些会误导是一个范围，实际是迭代5次，从0开始。
# "构造函数将 value 初始化为 start-1 = 0，迭代时会逐渐增加到 stop"  这一句更准确。
#定义一个__iter__()方法，使得d成为一个迭代器，并返回d本身。
#用__next__()魔法方法，开始从迭代器里取值
#如果取得的值==对象的stop，就停止迭代。
#每取得一个值，就递增一下
#返回递增后的值的两倍。

#实例化对象d的取值范围是从1-5
#fon语句从d中依次取出1，2，3，4，5，调用构造函数self.value=start-1,依次得到0，1，2，3，4
#依次从0开始，递增1，到5结束得到1，2，3，4，5
#返回乘以2的结果：2，4，6，8，10，以空格结尾打印出来。

# 注释说"从0开始"正确，但说"取值范围是从1-5"不太准确，实际是 start 到 stop 的闭区间。
# 注释说"每取得一个值，就递增一下"——实际是先递增再返回，不是取得后再递增。
