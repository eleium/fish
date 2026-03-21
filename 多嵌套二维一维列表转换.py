matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]


flatten=[]
for row in matrix:
        for col in row:
                flatten.append(col)
print(flatten)

x='有内鬼，交易停止!'
x.center(15)#输入的参数小于原字符串的下标数  5<9，输出原字符串
print(x)
print(x.ljust(15))