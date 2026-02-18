print(0.1+0.2)

from decimal import *
print(Decimal(0.1+0.2))#Decimal函数首字母要大写。



#python默认是用二进制来计算的，它占用内存的方式与使用十进制不同，故表现出来是不精确
a='0.1'+'0.2'
print(a)