# 变量与字符串：
print('d:\three\two\one\now')

# 反斜杠代表了转义，所以得到如下结果，\t代表制表符，\o不知道，\n代表换行
# d： hree  wo\one
# ow

# 这明显有问题，那么应该怎么解决呢???用n\转义符啊
print('d:/three/two/one/now')  # -->d:/three/two/one/now 这是用的绝对路径，不会出毛病。

print('d:\\three\\two\\one\\now')  # -->d:\three\two\onw\now，把原来的\路径转义后，代表路径的意思，而非制表符啥的。

print(r'd:\three\two\onw\now')  # -->d:\three\two\one\now  小写r,表示后面是原始字符串，\不再有效。
print(r'how are you')  # -->how are you

# triple quoted 三引号

poetry = '''
白日依山尽，
黄河入海流。
欲穷千里目，
更上一层楼。
'''
print(poetry)

# 字符串的加法
print(520 + 1314)  # 这是两个数据相加，是数学相加-->1834

print('520' + '1314')  # 这是两个字符串相加，是拼合字符串-->5201314
print('I love you'*3)# -->I love you I love you I love you 字符串重复3次。配合\n使用

