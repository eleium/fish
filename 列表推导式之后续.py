
b=[[0]*3]*3
b[1][1]=1
print(b)

list1=[[0]*3 for i in range(3)]
list1[1][1]=1
print(list1)

#你这两段代码结果不同的核心原因是：
# [[0]*3]*3 生成的是同一个列表的 3 个引用（浅拷贝），
# 而 [[0]*3 for i in range(3)] 生成的是3 个独立的新列表（深拷贝逻辑），
# 修改元素时前者会 “牵一发而动全身”，后者只改目标位置。

enve=[i for i in range(10) if i%2==0]
print(enve)
enve1=[i+1 for i in range(10) if i%2==0]
print(enve1)
#以上两个例子说明：列表推导式 先执行 for语句，然后再执行 if语句，最后执行表达式：i+1


#用列表推导式找出F开头的单词：

words=['great','Fantistic','excellent','FishC','Brillani']

words1=[w for w in words if w[0]=='F']#都已经指定列表推导式了，就要记得：过滤条件在后面。
print(words1)

words2=[i[0]=='F' for i in words]#判断第一个字母是否为F。
print(words2)

#把二维列表降维：创建嵌套列表     iterable:可重复，可迭代
#[expression for target1 in iterable1
#            for target2 in iterable2
#            for targetn in iterablen]


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
flatten=[col for row in matrix for col in row ]
print(flatten)#flatten: 展开，扁平化的意思


#降维一个二维列表的标准语法：
# flattened = [元素 for 子列表 in 二维列表 for 元素 in 子列表]

#外层循环for row in matrix放在前面.  内层循环for col in row放在后面。看第41行的代码
#用循环嵌套的方法实现把二维列表扁平化为一维列表。
flatten=[]
for row in matrix:
        for col in row:
                flatten.append(col)
print(flatten)

d=[x+y for x in 'fishc' for y in 'FISHC']
print(d,end='\n')#直接打印了d列表，而非打印列表d内的元素，所以end='\n'没有起作用。

_=[]
for x in 'fishc':
    for y in 'FISHC':
        _.append(x+y)
print(_)#python里面，用_代表不重要的，临时的变量名

#带过滤筛选的列表推导式：

m=[[x,y] for x in range(10) if x%2==0 for y in range(10) if y%3==0]
print(m,end='\n')

_=[]
for x in range(10):
    if x%2==0:
        for y in range(10):
            if y%3==0:
                _.append([x,y])#以列表的形式加入列表
print(_)


#列表推导式的原则： kiss ---->keep it simple and stupid 简洁胜于复杂。
#列表推导式可以很复杂，以便高速的执行，但是阅读与维护的成本很高。