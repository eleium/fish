#条件表达式：语句结构：
#  条件成立时执行的语句 if condition else 条件不成立时执行的语句  condition:条件

age = int(input('how old are you?'))
if age <= 18:
    print('you can not smoking')
else:
    print('enjoy your time')

#从传统的if语句结构变成了条件表达式
print("you can't smoking") if age<=18 else print('enjoy your timt')

a=3
b=5
if a<b:
    simall = a
else:
    simall =b

simall =a if a<b else b
print(simall)

#条件表达式还支持多行：

