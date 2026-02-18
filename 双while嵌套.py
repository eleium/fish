day=1
hour=1
while day <= 7:
    while hour <=8:
        print('今天坚持学习8小时。')
        hour=hour+1
        if hour>1:
            break#break只跳出一层循环体
    day=day+1#这个是外层循环的推动器，共推了7次。
