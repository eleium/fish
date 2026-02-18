# 条件表达式：语句结构：
#  条件成立时执行的语句 if condition else 条件不成立时执行的语句  condition:条件
from selectors import SelectSelector

from Tools.scripts.mailerdaemon import emparse_list_from

age = int(input('how old are you?'))
if age <= 18:
    print('you can not smoking')
else:
    print('enjoy your time')

# 从传统的if语句结构变成了条件表达式
print("you can't smoking") if age <= 18 else print('enjoy your time')

a = 3
b = 5
if a < b:
    simall = a
else:
    simall = b

simall = a if a < b else b
print(simall)

# 条件表达式还支持多行：
score = int(input('你考了多少分？'))
if score <= 60:
    print('不及格')
elif 60 < score <= 70:
    print('及格')
elif 70 < score <= 80:
    print('合格')
elif 80 < score <= 90:
    print('良好')
elif 90 < score < 100:
    print('优秀')
elif score == 100:
    print('天才')
else:
    print('别瞎几把填，写入1-100的分值。')

# 用条件表达式可以这么写：

print(
    '不及格' if score <= 60 else
    '及格' if score <= 70 else
    '合格' if 70 < score <= 80 else
    '良好' if 80 < score <= 90 else
    '优秀' if 90 < score < 100 else
    '天才' if score == 100 else
    '别瞎几把填，写入1-100的分值'
)

# 上述条件表达式又叫： 三元条件表达式，可以先赋值一个变量，然后再打印这个变量的值：
leval = ('不及格' if score <= 60 else
         '及格' if score <= 70 else
         '合格' if 70 < score <= 80 else
         '良好' if 80 < score <= 90 else
         '优秀' if 90 < score < 100 else
         '天才' if score == 100 else
         '别瞎几把填，写入1-100的分值')
print(leval)
# 括号内就是各个leval的条件

# 三元表达式的语法结构： value_if_True----> if condition else----> value_if_False
# 三元表达式必须返回一个值，才可以赋值啊，打印啊


print('hello,\nworld.\nthis is the \nfirst crying to you!')
# 以上意思是：可以用小括号包裹多行代码，与用转义符的效果是一样的。


# 分支结构的嵌套
age = 18
isMale = True  #用=表示赋值，是赋值符，用== 表示左右相对，是运算符。这里是给变量赋值，故用=,赋了个布尔值。

if age < 18:
    print('you can not smoking')
else:
    print('enjoy your time')
    if isMale:
        print('here is your smoking')
    else:
        print('no,you should go home')

#又要大于等于18，又要是男孩才可以 enjoy your time,here is your smoking.这就是嵌套。
