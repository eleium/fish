# dir(__builtins__) 显示所有python内置的函数名，在python 的 IDE里

# 变量：variable

x = 3
# x是变量名 。 = 是赋值操作。  3 是变量值。

print(x)  # -->3
# 变量名 不能以数字开头

# python3以后还支持中文当变量名了

记忆 = 887
print(记忆)  # -->887

name = '小甲鱼'  # 变量值为字符串要用括号括起来。否则python会认为 小甲鱼 是字符串。
# 空字符串也要用''包裹，以示与None区别。
print(name)  # -->小甲鱼

name = '大乌龟'
print(name)  # -->大乌龟  # 变量的值可以更改

x = 3;
y = 5  # 要在一行里给两个变量赋值可以用 ; 分开。也可以用更优雅的方法：
x, y = 3, 5
print(x, y)

# 两个变量值互换：
x, y = y, x
print(x, y)  # -->5 3

"""
python 的变量名支持大小写严格区分
不能以数字开头
支持驼峰命名MyName 
支持中文
最后以下划线分隔开
"""
print('I love china')  # 单引号适用于无嵌套的情况。
print("I love china,let's go!")  # 双引号适用于有嵌套的情况。文本两边引号要成对。
# 三引号适用于复杂情况，多行。
print("""I love china.
I'm chinese.
I'm from Dalian.
""")
# 用转义字符 \ 来表示你就是个单独的引号，而非与其他引号配对用的。
print('\"life is short,you need \"python\"\"')  # -->"life is short,you need "python""
print('I like apple,\nshe likes orange.')  # \n是换行转义符。

