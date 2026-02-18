i = 1  # 定义赋值变量，也可以叫计数器。从1开始。
while i <= 9:  # 外循环的条件，等于i<10.
    j = 1  # 为啥是j=1？#一个缩进表示属于外层循环，外循环每一遍，都要执行一次。为啥=1？表示内循环每次从1开始。
    while j <= i:
        print(f'{j}*{i}={j * i}', end='\t')  # print默认是end=\n,就是换行。这里用\t制表符，不换行，有缩进。
        j = j + 1
    print()  # 打印空行，每一次内循环结束后就来一个空行。
    i = i + 1  # 推动外循环往9走。超过9，条件不符了就完成外循环，外循环结束。
    #这个外循环推动器可以写在外循环条件while i<=9:下一行不？

print('--' * 80)

for i in range(1, 10):  # for会对每一个在函数range(1,10)1-9不含10里取值（遍历）的i开始外循环
    for j in range(1, i + 1):  # 内循环开始，遍历从1-i。循环里面套循环，这是内循环
        print(f"{j}*{i}={j * i}", end="\t")  # 真正的循环体，到底每次循环要干的事。内循环里面。
        # 参数end='\t'是制表符，表示缩进4个空格。默认是end='\n'表示换行
    print()  # 每次内循环后要执行的。这里是换行的意思。这个是外循环的命令。注意#######
# 外层循环每循环一次，其包含的内层循环就要遍历所有的循环。时针走一格，分针要走一圈。

"""
while是有条件循环，而for是无条件循环。两者都循环执行循环体，循环内容。
while:如果、当。。。的时候，咱就。。。这么干，然后下次还......这么干，一直到不符合了。
for: 开始干啦啊，就这么。。。。。。干，一遍一遍又一遍，一直到超出range()列表次数。
while循环需要先定义赋值一个变量。
while的步骤：定义变量--->判断循环条件--->执行循环内容--->递增变量---->再次循环
"""
"""
你的理解：while是有条件循环
✅ 正确！

补充：
- while循环依赖条件表达式
- 条件为True，继续循环
- 条件为False，退出循环
- 可以处理复杂的条件判断

你的理解：for是无条件循环
⚠️ 需要补充：

更准确的说法：
- for是"遍历循环"或"迭代循环"
- 不是无条件，而是"隐含条件"
- 条件是：是否还有下一个元素

示例：
for i in range(1, 10):
    # 隐含条件：range(1, 10)中还有元素吗？
    # 有元素 → 继续循环
    # 没有元素 → 退出循环
    
    
    你的理解：如果、当。。。的时候，咱就。。。这么干，然后下次还......这么干，一直到不符合了。
✅ 很形象！

更精确的表述：
while 条件:
    执行循环体
    递增变量
    
执行过程：
1. 检查条件是否为True
2. 如果True，执行循环体
3. 执行完循环体后，回到步骤1
4. 如果False，退出循环

你的理解：开始干啦啊，就这么。。。。。。干，一遍一遍又一遍，一直到超出range()列表次数。
✅ 基本正确！

更精确的表述：
for 变量 in 可迭代对象:
    执行循环体
    
执行过程：
1. 从可迭代对象中取出一个元素
2. 赋值给变量
3. 执行循环体
4. 回到步骤1，取下一个元素
5. 没有元素了，退出循环
"""

"""
# while可以处理复杂条件
count = 0
while count < 10 and user_input != 'quit':
    # 两个条件都要满足
    user_input = input("输入：")
    count += 1

# while可以处理不确定次数的循环
while True:
    user_input = input("输入quit退出：")
    if user_input == 'quit':
        break  # 手动退出

# while可以处理动态条件
import random
target = random.randint(1, 100)
guess = 0
while guess != target:
    guess = int(input("猜数字："))
    # 不知道要猜多少次
    
    
    
for语句更灵活、多样：   
# 遍历列表
fruits = ['苹果', '香蕉', '橙子']
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in 'Python':
    print(char)

# 遍历字典
person = {'name': '张三', 'age': 25}
for key, value in person.items():
    print(f"{key}: {value}")

# 遍历文件
with open('data.txt', 'r') as f:
    for line in f:
        print(line)

# 使用enumerate获取索引
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
"""



"""
#while循环的陷阱
1：忘记递增（死循环）
i = 1
while i <= 9:
    print(i)
    # 忘记 i = i + 1
    # 结果：无限输出1

# 陷阱2：条件永远为True
while True:
    print("死循环")
    # 没有break语句

# 陷阱3：条件一开始就为False
i = 10
while i < 5:
    print(i)  # 永远不会执行
    i += 1

# 陷阱4：浮点数精度问题
num = 0.1
while num != 1.0:
    print(num)
    num += 0.1
    # 可能永远不会等于1.0（浮点数精度）
    
    
# for循环的陷阱
1：修改循环变量无效
for i in range(5):
    print(i)
    i = 10  # 修改无效，下次循环i会被重新赋值

# 陷阱2：遍历时修改列表
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        numbers.remove(num)  # 危险！可能跳过元素

# 正确做法：遍历副本
for num in numbers[:]:  # 创建副本
    if num == 3:
        numbers.remove(num)
        """



""""循环的控制语句：
# break - 立即退出循环
for i in range(10):
    if i == 5:
        break  # 退出循环
    print(i)
# 输出：0 1 2 3 4

# continue - 跳过本次循环
for i in range(10):
    if i == 5:
        continue  # 跳过本次
    print(i)
# 输出：0 1 2 3 4 6 7 8 9

# else - 循环正常结束时执行
for i in range(5):
    print(i)
else:
    print("循环正常结束")

# 注意：break会跳过else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("不会执行")  # 因为break了
"""

"""如何选择while还是for
使用while的情况：
✅ 不确定循环次数
✅ 需要复杂条件判断
✅ 需要手动控制循环变量
✅ 游戏循环、用户交互
✅ 等待某个事件发生

示例：
- 猜数字游戏（不知道猜多少次）
- 用户输入验证（直到输入正确）
- 服务器监听（一直运行）

使用for的情况：
✅ 确定循环次数
✅ 遍历序列（列表、字符串、字典等）
✅ 不需要手动控制循环变量
✅ 代码更简洁

示例：
- 九九乘法表（固定9行）
- 遍历文件内容
- 处理列表数据"""


"""优化
# 优化1：减少循环内的计算
# 不好的写法
for i in range(1000):
    result = complex_calculation()  # 每次都计算
    print(result + i)

# 好的写法
result = complex_calculation()  # 只计算一次
for i in range(1000):
    print(result + i)

# 优化2：使用列表推导式
# 不好的写法
squares = []
for i in range(10):
    squares.append(i ** 2)

# 好的写法
squares = [i ** 2 for i in range(10)]

# 优化3：使用内置函数
# 不好的写法
total = 0
for num in numbers:
    total += num

# 好的写法
total = sum(numbers)"""


"""嵌套的理解：
# 嵌套循环执行次数
for i in range(3):  # 外层循环3次
    for j in range(4):  # 内层循环4次
        print(f"i={i}, j={j}")
# 总共执行：3 × 4 = 12次

# 执行顺序：
# i=0: j=0, j=1, j=2, j=3
# i=1: j=0, j=1, j=2, j=3
# i=2: j=0, j=1, j=2, j=3

# 比喻：
# 时钟 - 时针走1格，分针走一圈
# 外层循环走1次，内层循环走完整遍"""


"""循环的else子句，很重要
# for循环的else
for i in range(5):
    print(i)
else:
    print("循环正常结束")
# 输出：0 1 2 3 4 循环正常结束

# while循环的else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("循环正常结束")
# 输出：0 1 2 循环正常结束

# break会跳过else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("不会执行")
# 输出：0 1 2

# 实际应用：查找元素
def find_element(lst, target):
    for item in lst:
        if item == target:
            print(f"找到了：{item}")
            break
    else:
        print(f"没找到：{target}")

find_element([1, 2, 3], 2)  # 找到了：2
find_element([1, 2, 3], 5)  # 没找到：5"""


"""实践：
# 1. 选择合适的循环类型
# 遍历序列 → 用for
for item in my_list:
    process(item)

# 不确定次数 → 用while
while condition:
    do_something()

# 2. 避免修改循环变量（for循环）
for i in range(10):
    # 不要修改i
    print(i)

# 3. 使用有意义的变量名
# 不好的写法
for i in students:
    print(i)

# 好的写法
for student in students:
    print(student)

# 4. 限制循环次数（防止死循环）
max_attempts = 3
attempt = 0
while attempt < max_attempts:
    if check_password():
        break
    attempt += 1

# 5. 使用enumerate获取索引
for index, value in enumerate(my_list):
    print(f"索引{index}: {value}")

# 6. 使用zip同时遍历多个列表
names = ['张三', '李四', '王五']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}岁")"""
