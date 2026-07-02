"""
if语句用来当作python的分支。共有5种语句结构

"""

# 1，判断一个条件是否成立，如果成立就执行该语句下的某条语句或代码块.
# 语法结构如下：
# if condition:                 condition：条件
#     statement(s)              statement:  语句
#

if 4 < 5:
    print("里面")
    print("还是在里面")
print("这下在外面了")

# --->里面
# --->还是在里面
# --->这下在外面了


if 4 > 5:
    print("里")
    print("还是里")
print("hh,外面")
# --->hh,外面

# 由于4>5=False,所以里面的代码块不执行。只输出：hh,外面


# 2，判断一个条件：如果成立就执行其包含的代码；如果不成立就执行另外的代码。
# 语法结构如下：

"""
if condition:
    statement(s)
else:
    statement(s)
    """

if "小甲鱼" == "小女孩":
    print("小甲鱼是个女孩")
else:
    print("小甲鱼不是女孩")

# ---->小甲鱼不是女孩

# 字符串 '小甲鱼'!='小女孩'---->False---->程序不执行print('小甲鱼是个女孩')---->执行else:


# 3, if -elif -elif   判断多个个条件，如果第一个不成立就判断第二个，如果第二个也不成立就继续判断第三个，。。。。。。
"""语法结构：多条件分支语句

if condition1:
    statement(s1)
elif condition2:
    statement(s2)
elif condition3:
    statement(s3)
else:
    statement(s4)
    
"""

# 多个if 条件：不管条件成立与否，都要执行到最后。

score = input("请输入你的分数：")
score = int(score)

if 0 <= score < 60:
    print("D")
if 60 <= score < 80:
    print("C")
if 80 <= score < 90:
    print("B")
if 90 <= score < 100:
    print("A")
if score == 100:
    print("S")
# 如果是59分，第一个if 0<=score<60成立之后，输出D。但是还要执行后面的4个if语句。因为这些if 语句是平等的关系。

# 可以写成：if-elif: 碰到第一个if或者elif 条件成立，就不执行后面的了。
if 0 <= score < 60:
    print("D")
elif 60 <= score < 80:
    print("C")
elif 80 <= score < 90:
    print("B")
elif 90 <= score < 100:
    print("A")
elif score == 100:
    print("S")

# 如果是59分，第一个if语句 0<=score<60,成立，就打印D。此时，程序就结束了。不再向下执行。
# 如此，效率增高。

# 4，if -elif -else: 结构：上面if 和elif
if 0 <= score < 60:
    print("D")
elif 60 <= score < 80:
    print("C")
elif 80 <= score < 90:
    print("B")
elif 90 <= score < 100:
    print("A")
elif score == 100:
    print("S")
else:
    print("请输入正确合法的数值")
