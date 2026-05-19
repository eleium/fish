class S1(str):
    def __add__(self,other):
        return NotImplemented
class S2(str):
    def __radd__(self,other):
        return len(self)+len(Other)
    
s2=S2('banana')

s2+=s2
print(s2)
"""Python 遇到 s2 += s2。
Python 首先尝试调用左侧对象 s2 的 iadd 方法：s2.__iadd__(s2)。
关键点：你的 S2 类中没有定义 iadd。
因为 S2 继承自 str，Python 会去父类 str 中寻找 iadd。
字符串是不可变类型，在 Python底层实现中，str 的 iadd 通常直接回退（fallback）到调用 add。也就是说，对于不可变对象，a += b 等价于 a = a + b。
所以，表达式变成了 s2 = s2 + s2。
Python 尝试调用 s2.__add__(s2)。
关键点：你的 S2 类中也没有定义 add。
Python 再次去父类 str 中寻找 add。
str.__add__ 的功能是字符串拼接。
所以，'banana' + 'banana' 结果是 'bananabanana'。
最后赋值给 s2。"""