__all__=["say_hello","x"]
#文件了定义了两个变量：x,y和两个函数：say_hi和say_hello
#通过__all__属性，限制了被导入时只能导入这两个对象
x=500
y='python'



def say_hi():
    print('hi python')

def say_hello():
    print('hello python')

def int(x):
    print(f'哈哈{x}')
    