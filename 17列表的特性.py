#列表是可变的。不同于字符串，元组。即列表内容是可以增删改查的。列表内的元素可以重复出现。

s=[1,3,5,7,9,11,13,2,4]
s[2]=6
print(s)
s[3:]=[8,10,12,14,16]
print(s)
# s[3:5]=['a','b','c','d']
print(s)
s.sort()
print(s)


#sort()方法：让列表从小到大排列：只能是能比较的数字
#sort有两个参数：self , key ,reverse.  sort(reverse=True)
a=[2,5,7,5,6.33,8,99,6.02,33,56]
a.sort(reverse=True)
print(a)

# a.sort(reverse=True)是先排序再反转，而a.reverse()是直接翻转。
# reverse方法：从大到小排列：元素互换第一个与最后一个，第二个与倒数第二个互换

b=[3,4,5,7,8,9,1,2]
b.sort(reverse=True)#先从小到大排序，然后再反转
print(b)


#reverse()方法：反转列表中的元素
c=[3,4,5,2,7,1]
c.reverse()#直接反转
print(c)

####python中，函数与方法的区别：函数是独立的，函数名（参数），方法是属于某个类的，变量名（对象）.方法（参数）
#mylist = [1, 2, 3]

'''方法：属于列表对象
mylist.append(4)   # 对象.方法名(参数)
mylist.sort()      # 对象.方法名()

# 函数：独立存在
len(mylist)        # 函数名(对象)
sorted(mylist)     # 函数名(对象)
max(mylist)        # 函数名(对象)
'''


#count()方法：查找列表中有几个同样的元素，即某个元素出现的次数。

print(a.count(3))#在a 列表里面没有3

#index()方法：查找某个元素的下标索引值：
c=[3,4,5,2,7,1]
c.reverse()
print(c)#---->[1,7,2,5,4,3]已经反转

print(c.index(5))#求元素5的下标索引值---->3

c[c.index(4)]='hello'#先查找下标为4的元素，是4，然后用'hello'代替4。不对！！！
#是先查找列表中的元素4，然后用'hello'代替元素4.
c[4]='world'#这是按照下标索引值查找并替换。c.index(4)是查找到第一个值为4的元素，并替换。两者不同！！！
print(c)

print(c.index(2,1,5))#查找值为2的元素，并从下标索引值1-5里面查找

#copy()方法：

