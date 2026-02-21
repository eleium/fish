'''格式：

for i in 可迭代对象：    把可迭代对象里面的元素依次赋值给变量i(a,b,'小王',33)
    statement(s)

所谓迭代：从一个容器里（元组，列表，字典，集合等）以此取出每一个元素叫迭代。
'''

for each in 'today':  # 'today'不要（）括起来。它是字符串。
    print(each)

print('*' * 88)

i = 0
while i < len('today'):
    print('today'[i])
    i = i + 1

sum = 0  # 看来for循环也可以有定义变量这一步骤。
for i in range(1001):
    sum = sum + i
print(sum)

"""range有三种用法：都只能用整数,而且左开右闭：含第一个，不含最后一个。

1.range(stop)： 0- n-1
2.range(start,stop):  a- b-1
3.range(start,stop,step):  a- b-1,间隔步进：x 
"""

for m in range(11):
    print(m)
print('*' * 88)
for m in range(3, 11):
    print(m)
print('*' * 88)
for m in range(1, 11, 2):
    print(m)
print('*' * 88)

for m in range(100, 45, -5):  # 从100开始减去5.
    print(m)

print('*' * 88)

# 找出10以内的素数：素数就是除了1和它本身，不能被其他自然数整除的数或质数

for n in range(2, 10):#在2-9之间遍历，目的是得到让外层循环执行的次数，并且n是要被判断是否质数的数。
    for x in range(2, n):#在2-n-1之间遍历，目的是得到内层循环的次数：2-3，2-4，2-5，2-6，2-7，2-8，2-9
        if n % x == 0:#如果能被整除，就打印：循环条件：如果是偶数，就：
            print(n,'=',x,'*',n//x)#打印出： n = x * n//x
            break#跳出.因为是偶数，就跳出本循环。
    else:#如果不是偶数，是素数，就打印：
        print(f'{n}是一个质数')#如果 n%x !=0,就打印这句。
