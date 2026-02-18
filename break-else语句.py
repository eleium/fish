day = 0
while day <= 7:
    answer = input('今天好好学习了吗？')
    day = day+1
    if answer != '有':
        #print('今天好好学习了。')
        break
else:
    print('连续7天好好学习了')