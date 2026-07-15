"""


LEGB 变量作用域规则定义：
Python 变量作用域查找顺序，按优先级从高到低：
L - Local（局部作用域）
函数内部定义的变量
E - Enclosing（嵌套/外层函数作用域）
外层函数的局部变量（闭包的核心）
G - Global（全局作用域）
模块级别定义的变量
B - Built-in（内置作用域）
Python 内置的函数和异常（如 print、len、Exception）
查找机制： Python 按 L → E → G → B 顺序查找变量，找到即停止，找不到则报 NameError。

"""

# 全局作用域 G
x = "全局变量"


def outer():
    # 外层函数作用域 E
    x = "外层变量"

    def inner():
        # 局部作用域 L
        print(x)
        # 会先找 L，再找 E，再找 G，最后找 B

    inner()


outer()
# --->外层变量
# 解释：inner() 里没有定义 x，所以它会去外层的 outer() 里找，找到就停止，不会再去全局找。


"""
⚠️ 几个关键注意点
作用域只在函数 / 类里划分：Python 里，只有函数、类会创建新的作用域，if/for/while 等代码块不会创建新作用域。
global 和 nonlocal 关键字
global：在函数内声明要使用 / 修改全局作用域的变量
nonlocal：在嵌套函数内声明要使用 / 修改外层函数作用域的变量
内置作用域的优先级最低：如果你自己定义了一个和内置函数同名的变量（比如 len = 10），就会覆盖掉内置的 len() 函数，导致后续无法正常使用。"""
