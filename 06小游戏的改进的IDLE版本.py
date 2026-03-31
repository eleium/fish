import random

times_input = 3#设定输入次数。
while times_input > 0:#当这个变量大于0的时候，开始执行下面的代码
    temp = input('猜一下小甲鱼现在心里想的是哪个数字：')
    guess = int(temp)

    answer = random.randrange(1, 5)
    print(answer)

    if guess == answer:
        print('猜猜对啦！')
        print('但是没有奖励哦。')
        # break
        # 没有break语句，所以如果小于answer，可以无限次下去。
    else:
        if guess < answer:
            print(f'太小了')
        else:
            # guess > answer:  在else语句中，不要写条件了，因为else就是最后的情况：否则的意思。
            print(f'太大啦')
    times_input=times_input-1
else:
    print('game over')
