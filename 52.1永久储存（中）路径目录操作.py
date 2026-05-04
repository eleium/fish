from pathlib import Path

# 用replace()方法来替代指定的文件或文件夹。
m = Path('new_fishC.txt')  # 只是创建路径对象，不会创建真实文件或文件夹。不知道是文件还是文件夹，看下面代码来决定：
# 如果是m.mkdir,那么创建的 是文件夹；如果是m.write_text('hello'),那么创建的是文件,并且文件的内容是'hello'.
# 如果是m.touch(),那么创建的是一个空文件。

mkdir = Path('d:/python_learning/new_fishC.txt')  # 也只是创建路径对象，不会创建真实文件。而且创建的是文件夹对象

m.mkdir()  # 创建了在d:/python_learning/fish 即当前文件目录下的一个文件夹：new_fishC.txt
# m.mkdir('d:/python_learning')  报错：mkdir()不接受路径为参数，只接受 parents:True 或者 exist_ok:True这两个参数。

m.replace('no_fishc.txt')  # 替换文件文件夹的名字：no_fishc.txt
