# with 语句 和上下文管理器。with语句不需要打开文件后，用close()方法关闭文件。
#with语句的结构： with open('路径','w',encondng='utf-8') as f:
f = open('d:/python_learning/fish/elephant/tiger.txt', 'w', encoding='utf-8')
#比较open()方法和with语句：
with open('d:/python_learning/fish/elephant/tiger.txt', 'w', encoding='utf-8') as h:
    h.write('hello world,do you love python?')
# with语句会自动调用close()方法，不用手动调用。
# with语句会自动处理异常，不用手动处理。
# with语句会自动处理文件打开和关闭