# 来自 Thonny的文件
# x是变量名
# 可以直接调用 print(x)
520
baby = 520  # 报错：invalid syntax 语法错误

# variable 变量

# 变量的值取决于最后一次赋值。
name = '小甲鱼'
print(name)
name = '老大鱼'
print(name)

# 变量的值可以被传递
x = 3
y = 5
y = 3
print(y)  # ----> 3

# 把两个变量的值互换：
x = 3
y = 5
# 引入第三个变量：
z = x
x = y
y = z
print(x)  # ---->5
print(y)  # ----> 3

x, y = y, x  # 这种写法更简单

# 字符串 ： 就是一串字符
print('I love china.')  # ---->single quotes单引号
print("Today is good day.")  # ---->double quotes 双引号
# print('Let's go') # 这种写法错误。
print("Let's go!")  # 这样才对
print('"life is short,you need python"')
print(('''What a beautifly cat!'''))

# 转义符使用，引号前加上反斜杠\,把引号固定，只表示引号，没有其他语法含义。就不会再认为是引号的分隔作用了。
print('\"life is short,Let\'s learn python\"')

# 转义符加n  \n 代表换一行
print('I love china.\nI love Dalian.')
