"""
if语句用来当作python的分支。共有5种语句结构

"""
# 1，判断一个条件是否成立，如果成立就执行该语句下的某条语句或代码块.
# 语法结构如下：
# if condition:                 condition：条件
#     statement(s)              statement:  语句
#

if 4 < 5:
    print('里面')
    print('还是在里面')
print('这下在外面了')

'''
里面
还是在里面
这下在外面了
'''

if 4 > 5:
    print('里')
    print('还是里')
print('hh,外面')

# 由于4>5=False,所以里面的代码块不执行。只输出：hh,外面


# 2，判断一个条件：如果成立就执行其包含的代码；如果不成立就执行另外的代码。
# 语法结构如下：

'''
if condition:
    statement(s)
else:
    statement(s)
    '''

if '小甲鱼' == '小女孩':
    print('小甲鱼是个女孩')
else:
    print('小甲鱼不是女孩')
# 字符串'小甲鱼'!='小女孩'---->False---->程序不执行print('小甲鱼是个女孩')---->执行else:
# 故输出：小甲鱼不是女孩



#3,判断多个个条件，如果第一个不成立就判断第二个，如果第二个也不成立就继续判断第三个，。。。。。。
'''语法结构：多条件分支语句

if condition1:
    statement(s1)
elif condition2:
    statement(s2)
elif condition3:
    statement(s3)
else:
    statement(s4)
    
'''

