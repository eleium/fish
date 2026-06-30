# 列表推导式： [表达式 for I in 可迭代对象list if(条件过滤，可选)]      直接对该列表(列表是可迭代对象)操作。

# "列表推导式是一种Python语法结构，它允许通过简洁的表达式从一个或多个可迭代对象中生成新的列表，支持条件过滤和嵌套循环。"


# 更新列表中每个元素的值为自身的2倍
list1 = [1, 2, 3, 4, 5]
for i in range(len(list1)):
    # ---->len(list1)列表长度5---->range(5)创建0-4的数列---->for I in range(5)---->循环5次：i从0-4
    list1[i] = list1[i] * 2
    # 这一行代码的作用，就是列表的更改元素值的写法： list[index]='new_value'
    # 这一行一般叫：循环体。for I in range()叫循环条件，也叫循环头。
print(list1)
# for i in range(len(list1)),表示循环5次。即range(0,5),也就是0，1，2，3，4次。那么，i就等于0,1,2,3,4
# list1[i]=list[i]*2 循环体的作用：用新值替换旧值  第二章的 改： list[index]='new_value'
# 第一次循环：list1[0]=1-->1*2=2  并将新值2代替原来的值1，  结果是【2，2，3，4，5】
# 第二次循环：list1[1]=2,2*2=4    并将新值4代替原来的值2，  结果是【2，4，3，4，5】
# 第三次循环：list1[2]=3,3*2=6    并将新值6代替原来的值3，  结果是【2，4，6，4，5】
# 第四次循环：list1[3]=4,4*2=8    并将新值8代替原来的值4，  结果是【2，4，6，8，5】
# 第五次循环：list1[4]=5,5*2=10   并将新值10代替原来的值5， 结果是【2，4，6，8，10】
# 结束，退出循环


list1 = [1, 2, 3, 4, 5]
list1 = [i * 2 for i in list1]  # 列表推导式
print(list1)

# [表达式 for I in list if 过滤]。[expression for target in iterable]列表推导式的结果一定是一个列表.
x = [i for i in range(10)]
print(x)  # ---->[0,1,2,3,4,5,6,7,8,9]

y = []
for i in range(10):
    i = y.append(i + 1)
print(y)  # ---->[1,2,3,4,5,6,7,8,9,10]

s = [c * 2 for c in "Fishs"]
print(s)  # ---->['FF','ii','ss','hh','ss']

code = [ord(c) for c in "Fishs"]  # ord是内置函数，把单个字符变为 utf-8的编码
print(code)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [i[1] for i in matrix]
print(list2)

list3 = [matrix[i][i] for i in range(len(matrix))]  # 矩阵对角线
# len(matrix)=3, range(3)=[0,1,2],即i第一次是0，第二次是1，第三次是2.然后分别带入matrix[I][I].
print(list3)

list4 = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]  # 矩阵反对角线
print(list4)

# 循环与列表推导式的结果看似一样，其实不同：循环是逐个更改原列表，而列表推导式是生成一个新列表，赋值给原变量名。
