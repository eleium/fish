#列表、元组、字符串相互转换的函数：
#列表函数：用list将一个可迭代对象变成一个列表：
name='jack'#字符串
list(name)#用list把字符串变成列表---->['j','a','c','k']
print(list(name))

game=(1,2,3,'a') #元组
list(game)#---->[1,2,3,'a']用list把元组变成列表

#元组函数：用tuple将可迭代对象变成元组：
name1='jack'#字符串
tuple(name1)#---->('j','a','c','k')
game1=[1,2,3,'a']#列表被tuple()转换成了元组
tuple(game1)#---->(1,2,3,'a')字母一定带''.

#字符串的函数：用str将可迭代对象转为字符串：就是再原来列表或元组外添加一个''，但python又不显示''.
# 是将对象转换成它的字符串表示形式，print() 显示什么，字符串内容就是什么
name2=['j','a','c','k']#列表
str(name2)#---->['j', 'a', 'c', 'k']python 自动加 空格。
print(str(name2))

game2=(1,2,3,'a')
print(str(game2))#---->'(1, 2, 3, 'a')'python会自动加空格，而省略掉最外层 的 ''.即：（1， 2， 3， 'a')

#min()和max()函数：对比传入的参数，并返回最小值或最大值。

s=[1,1,2,3,5,7]#斐波那契数列
print(min(s))

t='hello'
print(max(t))#---->o     如果min()、max()传入的是字符串，将比较字符串中每个字符的编码值。按26个字母顺序。大写在小写前。
#如果是空的可迭代对象，比如：[],有一个default参数，可以指定输出内容：

m=[]
# min(m)#报错
print(min(m, default='写错啦'))#---->写错啦

#min()、max()传入多个参数时，自动比较大小：
print(min(1, 2, 3, 4, ))#---->1
print(max('abcdef'))#---->这是字符串而非多个参数。
print(max('hello','world'))#---->world 这是多个字符串，是同类元素，按字母顺序比较前后。

"""

✅ 可以比较：
数字之间（整数、浮点数都可以混合）
字符串之间
同类型的元素
❌ 不能比较：
不同类型（如数字和字符串混在一起会报错）"""

print('-'*50)
#len()函数和sum()函数：len()有最大值：2的63次方-1.sun()函数：求和，只能针对数字。


print(len((1,2,3)))#元组
print(len('hello'))#字符串---->5
print(len([1,2,3]))#列表

print(sum((1,2,3)))#元组#---->6
print(sum([1,2,3]))#列表#---->6

#sum()函数有个start参数，指定开始求和的位置
s=[1,2,3,4,5,6]
print(sum(s, start=100))#---->121 即：100+1+2+3+4+5+6
print('-'*50)

#sorted()函数和reversed()函数， 列表list有个sort()函数，对列表排序。
w=[3,4,6,8,6,4,2,6,8,0]
print(id(w))
print(w.sort())#---->None:sort() 方法返回 None，因为它会直接修改原列表（原地排序），而不是返回新列表。
#因为 w.sort() 自己把列表排好，但不返回东西，没有赋值。所以 w.sort() 就是 None。

print(id(w))

print(w)#--->[0, 2, 3, 4, 4, 6, 6, 6, 8, 8],这是因为刚才sort()已经修改了列表w，

print(id(w))
#三个id都一样，说明 w 是同一个对象。（盒子里的东西改变，盒子本身不变）
print('-'*50)
s=[1,2,3,0,6]
print(id(s))
sorted(s)#sorted()把列表s当作参数传入，跟列表的s.sort()方法的格式不同，结果相同。
print(sorted(s))#---->[0, 1, 2, 3, 6]
#sorted()返回的是一个新列表，而s.sort()是原来的列表。
print(id(sorted(s)))
"""
不同点（很重要）：
返回值不同：
sorted(s) → 返回一个新的已排序的列表，原列表不变
s.sort() → 返回 None，但会直接修改原列表
使用格式不同：
sorted(s) → 函数，需要接收返回值：result = sorted(s)
s.sort() → 方法，直接修改：s.sort()
"""


print('-'*50)
#sorted()也有两个参数：reverse=True 和 key=lambda x:x
s=[1,2,3,0,6]
sorted(s,reverse=True)#---->[6,3,2,1,0] 排序后反转
print(sorted(s,reverse=True))#---->[6,3,2,1,0]revers=True表示：反转=True,前面的reverse表示排序。

t=['fishc','apple','book','banana','pen']
sorted(t)#---->['apple', 'book', 'banana', 'fishc', 'pen'] 以字母顺序排列。
sorted(t,key=len)#---->['pen', 'book', 'fishc', 'apple', 'banana']字符串顺序排列，但长度不同，长度小的排前面。
print(sorted(t,key=len))
print(sorted(t,key=len,reverse=True))#---->['banana', 'fishc', 'apple', 'book', 'pen']反转排序

t.sort(key=len)
print(t)
#与sorted()函数一样，sort()函数也有两个参数：reverse=True 和 key=lambda x:x。
#sort()方法只能用于列表。sorted()函数可以处理任何可迭代对象

print(sorted('hello'))#---->['e', 'h', 'l', 'l', 'o']字符串变为列表：以字母顺序排列
print(sorted((1,0,0,8,6)))#---->[0, 0, 1, 6, 8]元组变为列表：以数字顺序排列

#reversed()函数：返回一个反向迭代器，迭代器中的元素是可迭代对象倒序后的元素。
s=[1,2,5,8,0]
print(reversed(s))#----><list_reverseiterator object at 0x00000273EF5D3D60>返回的是一个迭代器
print(list(reversed(s)))#---->[0, 8, 5, 2, 1]反转后的列表
print(s)#---->[1, 2, 5, 8, 0]这是原列表

#reversed()函数可以支持任何可迭代的对象
#转为列表
print(list(reversed('hello')))
print(list(reversed((1,2,3))))
print(list(reversed([1,2,3,4,5,6]))) #都可以输出反转后到一个列表。

#转为元组
print(tuple(reversed('hello')))
print(tuple(reversed((1,2,3))))
print(tuple(reversed([1,2,3,4,5,6]))) #都可以输出反转后到一个元组。

#用str转为字符串，会出现地址，然后把地址转为字符串：
print(str(reversed('hello')))
print(str(reversed((1,2,3))))
print(str(reversed([1,2,3,4,5,6])))
"""
reversed() 返回的是一个 reversed 迭代器对象
这个对象是惰性计算的，不会立即生成所有反转的元素
用 str() 转换时，只是把这个对象的地址信息转换成字符串
"""
#转为字符串（针对字符串反转）
print(''.join(reversed('hello')))