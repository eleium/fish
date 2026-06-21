#字符串的count方法可以计算字符串中重复的元素：包括子字符串

#count(sub[,start[,end]])这是啥表达？为啥不直接： count(sub(start,end))?
#是python中文档签名的表示法，[ ]表示是可选参数。

a=('hello','world',1,2,3,(1,2,3),5,5,(1,2,3))#这是元组，不是字符串
print(a.count((1, 2, 3)))
print(a.count(5))
# print(a.count('hello'),0,5)#总报错，参数太多，3个？为啥？
#因为a是元组！！！不是字符串！！！所以报错


#count方法对字符串可以用三个参数，包括两个开始和结束的下标，即查找范围。
# 元组只接受一个参数。 所以要区分好 元组和字符串：有逗号的就是元组。


b='hello','world',123,(1,2,3),5,5,(1,2,3)#仍然是元组。元组最厉害的就是以逗号做结构，不需要括号
# print(b.count('hello', 0, 5))

#find(sub[,start[,end]])找到子符串的字串，从下标start到end。从左往右找。输出的是下标值
#rfind(sub[,start[,end])) 从右往左找
c='hello'
print(c.find('world'))#find方法的作用：字符串中查找指定「子串」第一次出现的起始索引（下标）；如果找不到该子串，返回 -1。
print(c.find('hello'))
print(c.find('l'))


#字符串的替换 ：expandtabs()

code="""
    print('I love china.)
    print(c.upper())
    print(c.lower())
    """
new_code=code.expandtabs(4)#一个tab键等于4个空格。
print(new_code)

#replaced(old,new,count=-1)：返回一个old参数指定的子字符串为一个new 参数指定的一个new子字符串
#其中count是替换的次数。默认-1，即：如果不设置这个参数，默认更换全部。
print('在吗？我在你家楼下，很想你！！'.replace('在吗', '想你'))


#translate(table)方法：返回一个根据table参数指定的一个新的字符串。table:用于指定转换规则的表格。不一定非得是table.
table=str.maketrans('ABCDEFG','1234567')#先给参数table创建规则：用1234567来代替ABCDEFG
new_lan='I Love FishC'.translate(table)#使用translate(table)方法
print(new_lan)#----> I love 6ish3

table1=str.maketrans('ABCDEFG','1234567','Love')#第三个参数表示把这个字符串忽略掉
new_lan='I Love FishC'.translate(table1)
print(new_lan)#---->I 6ish3
