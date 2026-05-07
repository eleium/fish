# 如何将文件保存到硬盘上。
# 1，打开文件：打开或创建一共文件：open()函数：open(file,model='r',encoding='utf-8')
open('fishc_python_test', 'w', encoding='utf-8')

# 如果没有给'fishc'指定路径，默认是当前目录下。即：d:/python_learning/fish/因为当前用的ide就是这个目录：.venv/scripts/python.exe

# 将这个文件赋值给一个对象：创建一共文件对象，以便后面来操作它。
f = open('fishc_python_test', 'w', encoding='utf-8')
# 返回了一共文件对象f。然后就可以用一系列的方法操作这个文件了。
f.write('hello world')

# write:写入一个字符串。  writelines:写入一个列表。列表里自己加上\n来换行。
f.close()  # 关闭文件

# 再次打开：用'rw'模式打开并更新文件：
f = open('fishc_python_test', 'r+', encoding='utf-8')  # 'rw'的写法错误：
"""正确的模式
'r'：只读（read）
'w'：只写（write），会清空文件
'a'：追加（append），在末尾添加
'r+'：读写模式（既能读又能写）"""

f.writelines(['I love python\n' 'I like fishc\n' 'study make me happy'])
f.close()

# 因为文件是可以迭代的，那么python可以将文件用到for 语句中：
f = open('fishc_python_test', 'r', encoding='utf-8')
for each in f:
    print(each)
f.close()
# 用f.tell()方法，查看文件指针的位置。以字符为单位。
f = open('fishc_python_test', 'r', encoding='utf-8')
f.tell()
print(f.tell())  # --->0
f.close()

print('-' * 88)

# 用f.seek()方法，指定文件指针的位置。
f = open('fishc_python_test', 'r', encoding='utf-8')
f.seek(1)  # 把指针放到1的位置，但是没打印，所以没有显示。
print(f.seek(2))  # -->2 文件指针的位置在2. I love python:  I-->0,空格-->1,l-->2,o-->3,v-->4,e-->5,空格-->6,p-->7,...
print(f.read())  # 从2位置开始，读到文件的结束。
# 用f.readline()方法，一次读取一行，到\n就停止了。用f.read()方法，一次读取所有行。

# 在没有用f.close()的情况下，把文件写道硬盘上：用flush()方法，把数据写入硬盘。。
f = open('fishc_python_test', 'w', encoding='utf-8')
f.write('hello world')
f.flush()  # --->没有关闭文件的情况下，把文件写入了硬盘。但是open的model是'w'，所以以前的所有内容被新写入的'hello world'覆盖。
f.close()

# 文件的操作方法：
"""
文件打开模式（第二个参数）

| 模式   | 说明 |        |文件不存在时 |
|--------|------ |---------------------|
| `'r'` | 只读  |         报错 |
| `'w'` | 只写（清空）   | 创建 |
| `'a'` | 追加 |          创建 |
| `'x'` | 独占创建 |      创建（已存在则报错） |
| `'b'` | 二进制模式（配合使用） | - |
| `'t'` | 文本模式（默认） | - |
| `'+'` | 读写模式（配合使用） | - |

---

## 常见组合
| 模式 | 说明 |
|------|------|
| `'r'` | 只读 |
| `'w'` | 只写（清空） |
| `'a'` | 追加 |
| `'x'` | 新建（存在则报错） |
| `'rb'` | 二进制只读 |
| `'wb'` | 二进制只写 |
| `'r+'` | 读写（不清空） |
| `'w+'` | 读写（清空） |
| `'a+'` | 读写（追加） |

---

## 删除文件
用 `os.remove()`：
```python
import os
os.remove('filename.txt')  # 删除文件
```


**`del` 是删除 Python 变量，不是删除文件：**
```python
f = open('test.txt')
del f  # 只是删除变量 f，文件还在磁盘上
```


**总结：打开模式只有 `r/w/a/x` 及其组合，删除文件用 `os.remove()`。**
"""

# 截取模式：truncate()方法：
f = open('fishc_python_test', 'r+', encoding='utf-8')
print(f.truncate(6))
print(f.read(6))  # --->hello
# 特殊的截断模式：打开文件时，用了model: 'w'。将会把所有文件清空！！！！！
