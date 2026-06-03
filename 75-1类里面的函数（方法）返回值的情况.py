
#在创建了一个类之后，要定义一些函数当作实例化的对象的方法，这些方法的返回值的情况如下：


'''方法的返回值规则
1. 有明确的 return
python
def add(a, b):
    return a + b  # 显式返回
2. 没有 return 语句 → 返回 None
python
def increment(a):
    a += 1  # 只是执行操作，没有return
    # 隐式返回 None

result = increment(5)
print(result)  # None
3. 只有 return（没有值）→ 也返回 None
python
def do_something():
    # 一些操作
    return  # 相当于 return None

result = do_something()  # None
4. 执行表达式 + 返回值可以同时存在
python
def process(x):
    x += 1  # 执行表达式
    return x  # 返回值
更完整的情况
方法实际上可以做的事情远不止这两种：

1. 修改对象状态（无返回值）
python
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1  # 修改状态，无返回值（返回None）
2. 抛出异常（可能无返回值）
python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")  # 异常，不返回值
    return a / b
3. 生成器函数（返回生成器对象）
python
def count_up_to(n):
    i = 0
    while i < n:
        yield i  # 不是return，而是yield
        i += 1
# 调用返回生成器对象，不是None也不是具体值
4. 执行 I/O 操作
python
def log_message(msg):
    with open('log.txt', 'a') as f:
        f.write(msg)  # 执行I/O，无返回值
5. 调用其他函数（可能没有显式返回）
python
def wrapper(x):
    print(f"Processing {x}")  # 执行操作
    # 没有return，返回None
'''


class MyClass:
    def method_with_return(self):
        return 42  # 返回整数

    def method_side_effect(self):
        self.data = 100  # 修改属性，返回None

    def method_expression(self):
        x = 5
        x += 1  # 执行表达式，返回None

    def method_both(self):
        x = 5
        x += 1  # 执行表达式
        return x  # 返回值
    def method_empty_return(self):
        print("Doing something")
        return  # 返回None

obj = MyClass()
print(obj.method_with_return())  # 42
print(obj.method_side_effect())  # None
print(obj.method_expression())   # None
print(obj.method_both())         # 6
print(obj.method_empty_return()) # None

"""
核心要点
Python 中所有函数/方法都有返回值 - 如果没有显式 return，默认返回 None
return 不是必需的 - 但理解隐式返回 None 很重要

方法可以：
只计算并返回值（纯函数）
只修改状态（副作用）
两者都做
抛出异常
是生成器（用 yield）
与其他系统交互（I/O、网络等）
所以你的理解基本正确，但记住：没有 return 时返回 None，而不仅仅是"执行表达式"。
"""
