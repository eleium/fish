# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
num = input("enter a number:")

list_num = list(map(int, str(num)))
n = len(str(num))

huiwen_num=True

for i in range(n//2):
    #只需要比较一半
    if list_num[i] - list_num[-i - 1] != 0:
        huiwen_num=False
        break

if huiwen_num:
    print(f"{num}是回文数。")
else:
    print(f"{num}不是回文数")


num=input('enter a number:')
if str(num)==str(num)[::-1]:
    #注：[::-1] 是 Python 中非常经典的切片操作，意为“从头到尾，步长为 -1”，也就是将字符串完全反转。)
    print(f"{num}是回文数。")
else:
     print(f"{num}不是回文数")



     

#答案
x = int(input("请输入一个正整数："))

if x < 0 or (x % 10 == 0 and x != 0):
    print("不是回文数。")
else:
    revertedNumber = 0
    while x > revertedNumber:
        revertedNumber = revertedNumber * 10 + x % 10
        x //= 10

    if x == revertedNumber or x == revertedNumber // 10:
        print("是回文数。")
    else:
        print("不是回文数。")