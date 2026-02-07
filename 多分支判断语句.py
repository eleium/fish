score=input('请输入你的等级：')
score=int(score)

if 0<=score<60:
    print('不及格')
elif 60<=score<90:
    print('良')
elif 90<= score<100:
    print('优秀')
#else:
#    print('天才')
#还有一种情况：输入的不在0-100之内，是非法输入，所以上面的程序还不能用else
    
elif score==100:
    print('天才')
else:
    print('请输入0-100之间的数字')