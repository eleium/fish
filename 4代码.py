"""一个小游戏："""

temp = input('不妨猜一下小甲鱼现在心里想的是哪个数字：')  # 赋值操作。把input()内的字符串赋值给temp变量。
guess = int(temp)  # 赋值操作：把temp字符串转为整数，然后赋值给变量 guess.
# 要求input 的是数字，才能用int函数。

if guess == 8:  # 如果条件为真：True
    print('猜猜对啦！')  # 就执行这行代码。
    print('但是没有奖励哦。')
else:  # 如果条件为假：False
    print('没有蒙对哦。')  # 就执行这一行代码

    print('结束啦，没啥意思。')  # 这一行的缩进在else下，猜错，条件为假才运行。

temp1 = input('你是谁：')  # 输入是是啥，输出就是啥
print(temp1)
