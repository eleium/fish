"""
分支结构可以让程序根据条件判断，做不同的事情，而循环结构可以让程序根据条件判断，来一直做同样的事情。
Python 有两种循环语句： while and for.
"""
# while循环的语句结构：当条件符合的时候，就一直执行
# while condition:
#     statement(s)
#

love = 'yes'  # 给变量love赋值为字符串：yes
while love == 'yes':  # 如果变量的值是，等于yes,就执行循环
    love = input('今天你还爱我吗？')  # 变量love被赋值为：今天你还爱我吗？的输入：如果与yes相对就循环。
    # 如果不是，与yes不相等,那么循环就结束。

"""
第1行：love = 'yes'
作用：初始化变量 love 并赋值为字符串 'yes'。
细节：
love 是一个自定义变量名，用于存储用户的回答。
'yes' 是字符串类型（注意引号），表示“是”。
意义：为后续的 while 循环设置初始条件。
第2行：while love == 'yes':
作用：开始一个 条件循环，只要 love 的值等于 'yes'，循环就会持续执行。
细节：
while 是 Python 的关键字，用于创建循环。
love == 'yes' 是循环条件，== 是比较运算符（检查是否相等）。
如果条件为 True，执行循环体（缩进部分的代码）；否则跳过循环。
意义：根据用户的输入决定是否继续循环。
第3行：love = input('今天你还爱我吗？')
作用：在循环体内，通过 input() 函数获取用户输入，并将结果赋值给变量 love。
细节：
input('今天你还爱我吗？')：
显示提示文本 今天你还爱我吗？，等待用户输入。
用户输入的内容（如 yes 或 no）会作为字符串返回。
love = ...：将用户输入的新值重新赋给 love，覆盖之前的值。
意义：动态更新循环条件，控制循环是否继续。
代码执行流程
初始状态：

love = 'yes' → 循环条件 love == 'yes' 为 True，进入循环。
第一次循环：

打印 今天你还爱我吗？，等待输入。
如果用户输入 yes：
love 仍为 'yes' → 循环继续，再次询问。
如果用户输入其他内容（如 no）：
love 变为新值（如 'no'）→ 条件 love == 'yes' 为 False，退出循环。
循环结束：

当 love 不是 'yes' 时，程序终止。"""

i = 1
sum = 0
while i <= 100:
    sum = sum + i  # sum += i
    i = i + 1  # i += 1
print(sum)

# 死循环
while True:  # 因为True 永远是真，不会为False，所以会一直循环，死循环。死循环也有很大的作用。
    print('世界真美好')
    break  # 用break来结束循环。


while True:
    answer=input('可以退出吗？')
    if answer==('可以'):
        break
    print('还没好？')#如果输入了'可以',程序就不执行这一个体内的代码，直接break了。