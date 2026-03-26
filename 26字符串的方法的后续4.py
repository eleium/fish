#字符串的截取的方法：除了strip()之外，还有:removeprefix()和removesuffix()方法。
x='www.inthehome.com'
print(x.removeprefix('www.'))
print(x.removesuffix('com'))
#以上是removeprefix()和removesuffix()方法的使用，
# removeprefix()方法会删除字符串开头的指定内容，而removesuffix()方法会删除字符串结尾的指定内容。

#拆分和拼接：partition()和rpartition()方法：
print('-'*40)
print(x.partition('.'))#---->('www','.','inthehome.com') 参数是. 原字符串中与参数匹配的分割成三元组。
print(x.rpartition('.'))#---->('www.inthehome','.','com')从右往左分割成三元组。)
print(x.partition('ww'))#---->('', 'ww', 'inthehome.com')
# 在字符串中查找传入的参数（这里是 'ww'）找到后，将字符串分成三部分：(分隔符之前的部分，分隔符本身，分隔符之后的部分)
print(x)#---->验证原来字符串不变。

#split(sep=None,maxsplit=-1)方法：把字符串分割，按照传参分割。参数是字符串里面有的元素。
print('苟日新，日日新，又日新'.split())#---->['苟日新，日日新，又日新'] 变成了一个列表。
print('苟日新，日日新，又日新'.split(' '))#---->['苟日新，日日新，又日新']参数为空格，效果与参数空白一样？
#参数为空，默认为空格。或者是原字符串中没有的字符，将返回一个列表。
# split() 默认按所有空白字符分割（包括：空格、制表符 \t、换行符 \n、回车符 \r 等）
#split() = 智能模式，自动识别所有制表符、换行符、空格等
#split('x') = 精确模式，只找字符 'x'，找不到就返回原样
print('苟日新，日日新，又日新'.split('日'))#---->['苟','新，','新，又','新']，少了一个''空字符串。
# 最关键的一句话：两个分隔符连在一起，中间会切出空字符串！空字符串怎么表现： ''就是空字符串。

print('苟日新，日日新，又日新'.rsplit('日'))
#当你不指定最大分割次数时（即只传入分隔符参数），split() 和 rsplit() 会分割所有出现的分隔符，最终得到的结果列表是完全相同的。

# split(sep=None,maxsplit=-1) :sep=separator 分隔符，即你用什么字符来切割字符串。默认是所有的空白字符，包括：空格、制表符 \t、换行符 \n、回车符 \r 等。
# maxsplit=max_splits 最大分割次数，即你希望字符串被分隔成几个部分。默认是 -1，表示不限制分割次数。
y='a-b-c-d-e'
print(y.split('-',2))  # 输出结果：['a', 'b', 'c-d-e']
# 解释：split('-', 2) 表示使用 '-' 作为分隔符，最多分割 2 次。
# 第一次分割得到 'a' 和 'b-c-d-e'；
# 第二次分割 'b-c-d-e' 得到 'b' 和 'c-d-e'；
# 最终列表包含三个元素：['a', 'b', 'c-d-e']。

#splitlines():方法，默认按照换行符切割并换行输出一个列表。
z='朝辞白帝彩云间\n千里江陵一日还\n两岸猿声啼不住\n轻舟已过万重山'
print(z.splitlines())#参数为空，默认按照换行符切割并换行输出一个列表。
print(z.splitlines(True))#参数为True,会显示换行符。默认是False，不显示。


#join(iterable)方法：把可迭代对象中的元素用字符串连接起来，并返回连接后的字符串。拼接。

print('.'.join(['www', 'ilovefish', 'com']))#要求是可迭代的对象。输出：www.ilovefish.com。 .是分隔符。
print('^'.join(('I', 'love', 'python')))#元组也是可迭代的。输出：I^love^python

#join(iterable)方法拼接字符串，与直接用+ 拼接的区别：
s='hello'
s += s
print(s)

print(''.join(('hello', 'hello')))

#  +：字符串 + 字符串  join：连接符.join (列表 / 元组等)。强推join方法。
#  join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。只调用一次内存，故速度快，拼接越多越快（比起 +）。