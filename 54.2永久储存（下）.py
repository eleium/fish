    # python对象序列化的第一人：pickle模块。它解决的就是python对象永久储存的问题。
    # pickle module的核心作用就是把list ,tuple,dict,set,等储存为一个文件
    # 所谓序列化，就是把对象转换为一个二进制字节流的过程。

import pickle

# 以下都是python 的对象
x, y, z = 1, 2, 3
s = "fish"
l = ["甲鱼", 520, 3.14]
d = {"one": 1, "two": 2}

with open('date.pkl','wb') as f:#用.pkl做后缀，用'wb'二进制写入文件。
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(z,f)
    pickle.dump(s,f)
    pickle.dump(l,f)
    pickle.dump(d,f)

#此时，date.pkl文件就储存了这些对象的二进制字节流了。因为是二进制的文件，所以用记事本等文本编辑器无法直接查看，
# 但我们可以通过pickle.load()函数来读取这些对象。
with open('date.pkl','rb') as f:
    x=pickle.load(f)
    y=pickle.load(f)
    z=pickle.load(f)
    s=pickle.load(f)
    l=pickle.load(f)
    d=pickle.load(f)
print(x,y,z,s,l,d,sep="\n") #-->1 2 3 fish ['甲鱼', 520, 3.14] {'one': 1, 'two': 2}
#或者在写的时候用元组的方式，然后在读的时候就可以一次性解包，读出来了。
with open('date.pkl','wb') as f:
    pickle.dump((x,y,z,s,l,d),f)
with open('date.pkl','rb') as f:
    x,y,z,s,l,d = pickle.load(f)
print(x,y,z,s,l,d,sep="\n") #-->1 2 3 fish ['甲鱼', 520, 3.14] {'one': 1, 'two': 2}