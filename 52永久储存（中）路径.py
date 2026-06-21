# pathlib文档
from pathlib import Path  # 表示从模块pathlib里面，单独导入Path。这种导入方式，后面引用的时候，不需要前缀模块名。

# os.path 模块是啥？ os.path模块与pathlib模块的区别？ python3.4前后的用法。高版本用pathlib模块。

# print(Path.cwd(test.py))  # -->D:\python_learning\fish 获取当前的工作目录路径。而不是某个文件的目录。
# Path.cwd() 不接受任何参数！它只返回当前工作目录，不能传入文件名。
print('-' * 88)
# 正确写法：
print(Path.cwd() / 'test.py')  # 得到当前文件夹里面的文件的路径
# 或者
print(Path('test.py').resolve())  # 得到当前文件夹里面的文件的绝对路径。

print(Path.cwd())  # -->d:/python_learning/fish

# 创建一个路径对象：
p = Path("d:/python_learning/fish")  # 路径必须加引号，否则python会以为是一个变量。必须为字符串格式。
print(p)  # --->d:/python_learning/fish#这个路径对象是可以打印的，输出的时候，会打印成字符串模式。

# 我们有一个文件名叫：fishc_python_test,把它赋值给一个对象 q，即创建了一个路径对象:q
q = Path('fishc_python_test')
print(q)  # --->fishc_python_test 这个路径对象q，其实就是这个文件的名字。
# 把这个文件的路径拼接到完整的路径上：
q = p / "fishc_python_test"
print(q)  # --->d:/python_learning/fish/fishc_python_test

print('_' * 88)
# 路径的方法：
# 用is_file()方法，判断一个路径是否为一个文件
print(p.is_file())  # --->False，因为p=Path('d:/python_learning/fish')是文件夹的路径。
print(q.is_file())  # -->True.

# 用is_dir()方法判断一个路径是否为一个文件夹
print(p.is_dir())  # -->True

# 用exists判断一个路径是否存在
print(p.exists())  # -->True

print(Path('c:/fish').exists())  # False

# 用name属性，获取路径对象的最后一部分：
print(p.name)  # --->fish p=Path('d:/python_learning/fish')
print(q.name)  # --->fishc_python_test  文件夹里没有显示扩展名，路径操作也不显示。
f = open(q, 'r+', encoding='utf-8')
print(f)
print(f.read())
f.close()
print(type(q))
print(type('fishc_python_test'))

print('--' * 88)
# 用suffix获取文件的后缀名：
print(q.suffix)  # 这个文件没有扩展名，所以返回空。
# 创建文件的时候，要指定文件的扩展名。

# 用stem属性获取文件的名。
print(q.stem)  # --->fishc_python_test

# 用parent属性，获取其父级目录：
print(q.parent)  # --->d:/python_learning/fish

# parents，复数形式的属性，会获得逻辑祖先构成的一个不可变序列.每一级的目录，即包含所有父目录。
print(q.parents)  # ---><WindowsPath.parents> 是 pathlib 中一个特殊的对象，表示所有父级目录的集合！
for each in q.parents:
    print(each)

"""
d:/python_learning/fish
d:/python_learning
d:/
"""
# 可以用索引的方式获取想要的层级的目录名：
print(q.parents[0])  # --->d:/python_learning/fish [0]是最近的父级目录。

# 用parts属性把整个路径拆分为一个元组：
print(q.parts)  # --->('d:/','python_learning','fish','fishc_python_test')

# 用stat属性，获取文件或文件夹的信息：
print(q.stat)  # ---><bound method Path.stat of WindowsPath('d:/python_learning/fish/fishc_python_test')>
print(q.stat().st_size)  # --->68  这个文件有68个字节。

print('-' * 88)
# 相对路径 和 绝对路径absolute path

# 绝对路径：从根目录开始，到文件或文件夹的完整路径。
# 相对路径，就是从当前的目录开始，到文件或文件夹的完整路径。 一个.表示当前目录，两个.表示当前目录的父级目录。
print(q.absolute())  # -->d:/python_learning/fish/fishc_python_test
print(Path('./doc'))  # Path('./doc') 只是创建了一个路径对象，并不会检查文件是否存在！
"""这行代码的作用是：
创建一个 Path 对象，表示"当前目录下的 doc"
打印这个路径对象（会显示为字符串形式）
它不会：
检查文件是否存在
❌ 检查文件夹是否存在
❌ 创建文件或文件夹

相当于在纸上写了一个地址，但是这个地址不一定存在。要确认是否真实存在，用exists()验证。
"""

# 用resolve()方法 ，把相对路径转化为绝对路径

# ./fishc_python_test.resolve()#不能用文件或文件夹直接操作，要用路径对象
print(Path('./fishc_python_test').resolve())  # -->d:/python_learing/fish/fishc_python_test
print(Path('../fish_pythn_test').resolve())  # -->d:pythn_learning/fish_pythn_test

# 用iterdir()得到该目录下所有的文件和文件夹
print(p.iterdir())  # --><generator object Path.iterdir at 0x00000264AEC23510>得到一个可迭代生成器
for each in p.iterdir():
    print(each)

print('-' * 88)
from pprint import pprint

print(p)

# 将当前文件夹下的所有文件，保存到一个列表中，用list:
pprint(list(p.iterdir()))
pprint([x for x in p.iterdir() if x.is_file()])

print('-' * 88)
n = p / 'elephant'  # 此时只是创建了一个路径对象，并没有实际创建文件夹。
n.mkdir()  # 现在才创建文件夹了。
"""
p：在第17行定义的路径对象 p = Path("d:/python_learning/fish")，指向当前工作目录
/：这是 pathlib 模块重载的除法运算符，用于拼接路径（不是真正的除法）
'elephant'：要拼接的子目录名称（字符串格式）
n：新的路径对象，结果为 d:/python_learning/fish/elephant

这行代码的作用是创建目录（文件夹）。
mkdir()：是 Path 对象的方法，全称是 "make directory"
它会在文件系统中实际创建一个名为 elephant 的文件夹
完整路径为：d:\python_learning\fish\elephant
"""
"""
还可以这样写：
(p / "elephant").mkdir()
注意要加上括号，因为python中， . 的优先级高于 / 等除法运算符
"""

# 用exist_ok参数=True来避免创建重复的文件夹的时候报错：
n.mkdir(exist_ok=True)

# 用parents=ok参数来避免创建的文件夹里面有不存在的父级目录的时候报错：
m = p / 'dog/cat/pig'
m.mkdir(parents=True)
"""
m = p / 'dog/cat/pig'
✅ 不报错  只是创建路径对象
m.mkdir(parents=True)
✅ 不报错   自动创建所有父目录
m.mkdir()
❌ 报错   父目录不存在时会报错
"""

# 这两个参数可以同时使用：

k = p / 'apple/orange/butterfly'  # 创建一个路径对象，包含多级父目录
k.mkdir(parents=True, exist_ok=True)  # 用parents=True参数来实现

# Path 对象内置了一个 open() 方法，用来打开文件。注意：是Path对象的方法，不是path方法"。
# 除了不用传入第一个参数路径之外，跟open()函数一模一样。

f = open('test1.py', 'r+', encoding='utf-8')

# 这个 open() 是 Python 程序的内置函数，它的作用是：
# ✅ 在程序运行时打开文件，让 Python 代码可以读取或写入文件内容。结果可以用print打印出来。
# ❌ 不是在编辑器中打开文件（像双击文件那样）
f.close()

# pathlib模块中的path对象可以用open()方法执行：最上方已经 from pathlib import Path
n = n / 'flower'
h = n.open('w', encoding='utf-8')
h.write('hello world,do you love python?')
h.close()
"""
p = Path("d:/python_learning/fish")
n = p / 'elephant'  # n = d:/python_learning/fish/elephant
n.mkdir()            # 实际创建文件夹elephant
n = n / 'flower'  # n 变成 d:/python_learning/fish/elephant/flower
#很不好的习惯：用n代替了n,人为的制造了混乱。

h = n.open('w', encoding='utf-8')  # 打开文件（如果不存在会自动创建）
h.write('hello world,do you love python?')  # 写入内容
h.close()  # 关闭文件

此时，flower的路径是：d:/python_learning/fish/elephant/flower
"""

# 用rename()方法给文件重命名：
n.rename('tiger')
# rename() 会移动/重命名文件
# - 如果目标路径只包含文件名（无目录），文件会移动到当前工作目录
# - 如果目标路径包含完整目录，文件会移动到指定目录
# - 原路径的文件消失（不是删除，是被移动）
# - 文件的磁盘数据原地不动，只是目录项被修改了
n.rename("d:/cat")
# 不能用 h.rename('tiger'),因为h是一个文件对象，而不是一个具体的文件。
