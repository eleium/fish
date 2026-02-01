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

3 < 4 and 4 < 5 - --->True
3>4 or 4<5 ---->True

"""
python中，任何对象都可以进行真值测试（测试该对象的值是True还是False),用于if或while语句的
条件判断。还可以当作布尔逻辑运算符的操作数，就是可以当数据被用做布尔运算，比较真假。
"""