"""
1.输入数字后，提示是比8大还是小，或者一屁蒙对。
2.应当提供几次机会，明确机会次数。
3.每次运行这个游戏，答案应该是随机的。不能固定一个答案8.
"""
# 调入 random 随机模块
import random

times_input = 3  # 设定输入次数。
while times_input > 0:  # 当这个变量大于0的时候，开始执行下面的代码
    temp = input('猜一下小甲鱼现在心里想的是哪个数字：')
    guess = int(temp)

    answer = random.randrange(1, 5)#这一行可以提到第十行，当作全局全域赋值。效果一样，逻辑更对。
    print(answer)

    if guess == answer:
        print('猜猜对啦！')
        print('但是没有奖励哦。')
        break  # 如果猜对了就跳出程序，不需要再猜。
    else:
        if guess < answer:
            print(f'太小了')
        else:
            # guess > answer:#在else语句中，不要写条件了，因为else就是最后的情况：否则的意思。
            print(f'太大啦')

    times_input = times_input - 1
else:
    print('game over')

"""
while 语句：
while 条件:
    如果条件为真True,执行这行代码
    """
