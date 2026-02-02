'''
布尔值：True  /  False
逻辑运算符： and /  or  / not
'''

print(bool(3.14))  # ---->True

"""
一下是最常见的结果为False的布尔值：
1，定义为假的： False 和 None
2，值为0的数据类型： (4-4)，decimal(0), 0, 0.0
3，空的列表，集合等：  "",(),[],{},range(0)
"""

if 100 > 30:
    print('这是真的')
else:
    print('我错了')

# 运行结果是 这是真的，因为100>30是True,执行完第15行就结束了。


if 100 < 30:
    print('假的')
else:
    print('错的就是错的')
# 运行结果是 错的就是错的，因为100<30是False。

if bool(3.14):
    print('这也是真的')

# 布尔类型其实就是特殊的整数类型
1 == True
0 == False

True + False  # ---->1
True - False  # ---->1
True * False  # ---->0
True / False  # ---->语法错误。0不能为除数。

"""逻辑运算符：and or not
and: 左右同时为True,结果为True,有一个False,结果就是False.          三False 一True
or : 左右有一边是True ,结果就是True,除非两边都是False,结果才是False。三True一False
and or :口诀：and 1 True or 3 True.
not: 相反
"""

3 < 4 and 4 < 5 #- --->True
3>4 or 4<5 #---->True

"""
python中，任何对象都可以进行真值测试（测试该对象的值是True还是False),用于if或while语句的
条件判断。还可以当作布尔逻辑运算符的操作数，就是可以当数据被用做布尔运算，比较真假。
"""

'''短路逻辑：从左往右，只有对第一个操作数不能求得逻辑值时，才对随后的操作数求值，

and 的短路求值：从左到右，如果有一个是假，取第一个假，后面的不管了。如果都是真，取后面的。
or 的短路求值
or 从左到右计算，返回第一个真值（如果所有都是假值，则返回最后一个假值）。

(not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)
(not 1) or 0 or 4 or 6 or 9,其中（0 and 1)返回 0，因为and 要返回第一个假值 0 .
False or 0 or 4 or 6 or 9  ,(not 1) 1为真，所以返回False
or 短路求值： 返回遇到的第一个真值，然后忽略后面所有。如果都是假，就是0即最后一个假值.
得到最终：  4    
'''

'''
and：全真返回最后一个真值，遇假返回第一个假值。
or：返回第一个真值，全假返回最后一个假值。
Python 会短路求值，一旦确定结果就停止计算。
'''
'''
运算符的优先级：
not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9

'''