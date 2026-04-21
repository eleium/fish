"""1.通常企业发放的年终奖是根据一年的盈利进行提成，A 公司的提成规则如下：

1当利润低于或等于 10 万元时：年终奖为 10%
2当利润高于 10 万元，低于 20 万元时：低于 10 万元的部分按 10% 提成，高于 10 万元的部分，按 7.5% 提成
3当利润 20 万到 40 万之间时：低于 10 万元的部分按 10% 提成，高于 10 万元低于 20 万元的部分，按 7.5% 提成，高于 20 万元的部分，按 5% 提成
4当利润 40 万到 60 万之间时：低于 10 万元的部分按 10% 提成；高于 10 万元低于 20 万元的部分，按 7.5% 提成；高于 20 万元低于 40 万元的部分，按 5% 提成；高于40万元的部分，按 3% 提成
5当利润 60 万到 100 万之间时：低于 10 万元的部分按 10% 提成；高于 10 万元低于 20 万元的部分，按 7.5% 提成；高于 20 万元低于 40 万元的部分，按 5% 提成；高于40万元低于 60 万元的部分，按 3% 提成；高于60万元的部分，按 1.5% 提成
6当利润高于 100 万元时：低于 10 万元的部分按 10% 提成；高于 10 万元低于 20 万元的部分，按 7.5% 提成；高于 20 万元低于 40 万元的部分，按 5% 提成；高于40万元低于 60 万元的部分，按 3% 提成；高于60万元低于 100 万的部分，按 1.5% 提成；超过 100 万元的部分按 1% 提成

请编写一个程序，根据录入的利润，计算出应该发放的奖金总数？ """
profit = float(input('请输入利润'))
# profit:利润的意思。
bonus = 0
#bonus:奖金的意思。

if profit <= 10:
    bonus = profit * 0.1

elif 10 < profit < 20:
    profit <= 10:
    bonus = profit * 0.1
else:
    bonus = profit * 0.075
if 20 < profit < 40:
    if profit <= 10:
        bonus = profit * 0.1
    elif 10 < profit < 20:
        bonus = profit * 0.075
    else:
        bonus = profit * 0.05
if 40 < profit < 60:
    if profit <= 10:
        bonus = profit * 0.1
    elif 10 < profit < 20:
        bonus = profit * 0.075
    elif 20 < profit < 40:
        bonus = profit * 0.05
    else:
        bonus = profit * 0.03
if 60 < profit < 100:
    if profit <= 10:
        bonus = profit * 0.1
    elif 10 < profit < 20:
        bonus = profit * 0.075
    elif 20 < profit < 40:
        bonus = profit * 0.05
    elif 40 < profit < 60:
        bonus = profit * 0.03
    else:
        bonus = profit * 0.015
if profit > 100:
    if profit <= 10:
        bonus = profit * 0.1
    elif 10 < profit < 20:
        bonus = profit * 0.075
    elif 20 < profit < 40:
        bonus = profit * 0.05
    elif 40 < profit < 60:
        bonus = profit * 0.03
    elif 60 < profit < 100:
        bonus = profit * 0.015
    else:
        bonus = profit * 0.01
print(f'年终奖为：{bonus:.2f}万元')
