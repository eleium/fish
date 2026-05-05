# with 语句 和上下文管理器。with语句不需要打开文件后，用close()方法关闭文件。
# with语句的结构： with open('路径','w',encondng='utf-8') as f:
f = open('d:/python_learning/fish/elephant/tiger.txt', 'w', encoding='utf-8')
# 比较open()方法和with语句：
with open('d:/python_learning/fish/elephant/tiger.txt', 'w', encoding='utf-8') as h:
    h.write('hello world,do you love python?')
# with语句会自动调用close()方法，不用手动调用。
# with语句会自动处理异常，不用手动处理。
# with语句会自动处理文件打开和关闭

# 用open()方法打开一个文件的过程：

f = open('D:/Pythontraining/file1.txt', 'r+', encoding='utf-8')
print(f.read())
f.close()
# 使用 with 语句打开文件，自动管理文件的打开和关闭，无需手动调用 close() 方法
# 'r+' 模式表示读写模式，既可以读取文件内容，也可以写入文件内容
# encoding='utf-8' 指定文件的编码格式为 UTF-8，避免中文乱码问题
with open('D:/Pythontraining/file1.txt', 'r+', encoding='utf-8') as f:
    # 读取文件内容并打印
    print(f.read())
    # 向文件中写入新的内容

    f.write('\n这是使用 with 语句写入的新内容')
print('-' * 88)
with open('d:/python_learning/fish/test1.py', 'r+', encoding='utf-8') as w:
    w.write('hello sir ,it is a good day,i am happy to you')
    w.seek(0)
    print(w.read())
    """
模式	行为	结果
'w'	清空重写	文件变成只有 hello sir...
'r+'	从开头覆盖	你的内容替换了原内容，残留了后面的旧内容 ← 你现在的情况
'a'	追加到末尾	保持原内容，在后面加新内容
"""

# 上文就是打开文件，下文就是关闭文件。使用了上下文管理器：with语句，就不需要手动关闭文件安啦。
# 但是一定要注意，文件语句的处理代码，一定要放在缩进里面。

f=open('fish.txt','a',encoding='utf-8')
f.write('hello,my friend.')
print(f.read())
f.close()