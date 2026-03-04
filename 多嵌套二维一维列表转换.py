matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]


flatten=[]
for row in matrix:
        for col in row:
                flatten.append(col)
print(flatten)