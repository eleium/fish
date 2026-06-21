# 函数就是一段代码的封装，是结构组件。函数外部不需要关系函数内部的执行细节，只关心函数的接口及执行后的结果。
# 如何快速融入开发？要会查询、阅读开发手册和函数文档。python 用help()函数来阅读函数文档。
help(print)
"""
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)    #函数的原型
    Prints the values to a stream, or to sys.stdout by default. #函数的功能介绍
    
    #一下是个参数的类型及作用
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream."""


def exchange(dollars, rate=7.0):
    """
    功能：货币转换  把dollars --> RMB
    参数：
    -dollars 美元数量
    -rate    当前汇率（2026-04-20）
    返回值：
    -人民币数量"""
    return dollars * rate


result = exchange(100)
print(result)  # -->700.0
# 现在可以用help()函数来查看自己编写的文档了：
help(exchange)
"""
Help on function exchange in module __main__:

exchange(dollars, rate=7.0)
    功能：货币转换  把dollars --> RMB
    参数：
    -dollars 美元数量
    -rate    当前汇率（2026-04-20）
    返回值：
    -人民币数量
    """


# 类型注释
def times(s: str, n: int) -> str:
    # 类型注释 str 和 int是作者期望的，但是 Python 不强制检查类型,
    """
    代码作者期望：s参数要传入str型，n参数要传入int型。
                函数会返回一个str型的结果"""
    return s * n


result1 = times('python', 3)
print(result1)  # -->pythonpythonpython

result2 = times(3, 5)
print(result2)  # --->15

result3 = times(2, 'python')
print(result3)  # pythonpython


# 如果希望有默认参数，直接在定义函数的时候规定就好了额。不需要调用的时候再传参。
def times(s: str = 'hello', n: int = 3) -> str:
    return s * n


result4 = times()
print(result4)  # -->hellohellohello


# 参数也可以是列表：
def times(s: list, n: int = 3) -> str:
    return s * n


result5 = times(['伊朗', '船员'])
print(result5)  # -->['伊朗','船员','伊朗','船员','伊朗','船员']


# 参数是字典
def times(s: dict, n: int = 3) -> str:
    # return s*n

    # 参数 s 标注为 dict，但函数体执行的是 s * n（乘法操作）
    # 字典不支持乘法运算，运行时会抛出 TypeError
    # 所以要改成如下的返回值：
    return {k: v * n for k, v in s.items()}


result6 = times({'name': 'python', 'age': 18})
print(result6)  # -->{'name': 'pythonpythonpython', 'age': 18}


# 或者在定义函数的时候，这么写：
def times(s: dict[str, int], n: int = 3) -> list:
    return list(s.keys()) * n  # 返回值为list.注意只是key经过乘法，而value没有经过乘法重复。


# 注释类型，为啥dict[]，字典不是{}吗？你看到的 dict[] 其实是类型提示（Type Hint）的语法，而不是字典本身。
# {} 是字典的字面量：用来创建具体的字典数据。dict[...] 是类型注解：用来告诉别人“这个字典里装的是什么”。


"""
为什么用 [] 而不是 {}？
在 Python 的类型系统（typing 模块）中，方括号 [] 表示泛型（Generic），即“容器里的元素类型”。
list[int]：表示一个列表，里面装的是整数。
dict[str, int]：表示一个字典，键是字符串，值是整数。
总结
写代码逻辑时：用 {} 创建字典。
写类型注释时：用 dict[key_type, value_type] 描述字典的结构。
注意： 在较新的 Python (3.9+) 中，你也可以直接用内置类型加方括号，比如 dict[str, int]；
在旧版本中则需要从 typing 导入 Dict，写成 Dict[str, int]。"""

result7 = times({'name': 'python', 'age': 18})
print(result7)

# 内省：最开始是心理学范畴，描述发生在自我内部，能够自己意识到的主管现象。
# 在计算机领域是指： 程序运行的时候能够自我检测的机制，称之为内省，或自省。pyhton通过特殊的属性来实现内省。用__name__看函数名：
print.__name__
print(print.__name__)  # --->print

times.__name__
print(times.__name__)  # --->times
times.__annotations__
print(times.__annotations__)  # -->{'s': <class 'str'>, 'n': <class 'int'>, 'return': <class 'str'>}

# 查看函数的doc文档：
print(exchange.__doc__)  # 自己定义的的exchange()函数的文档：
"""
Help on function exchange in module __main__:

exchange(dollars, rate=7.0)
    功能：货币转换  把dollars --> RMB
    参数：
    -dollars 美元数量
    -rate    当前汇率（2026-04-20）
    返回值：
    -人民币数量
    """

print(times.__doc__)  # -->None 我自己定义的times()函数没有编写说明文档
