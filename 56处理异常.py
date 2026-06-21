# 用try-except-else语句处理异常：当try-except语句块中的代码没有发生异常时，else语句块中的代码就会被执行。
try:
    print(1 / 1)
except:
    print("抓住你了!")
else:
    print("啥事没有啊。")
    # -->1.0
    # -->啥事没有啊。


# try-excepy-finally语句：
# 当try-except语句块中的代码发生异常时，except语句块中的代码就会被执行；
# 当try-except语句块中的代码没有发生异常时，else语句块中的代码就会被执行；
# 无论try-except语句块中的代码是否发生异常，finally语句块中的代码都会被执行。
try:
    print(1 / 0)
except:
    print("抓住啦")
else:
    print("没抓住")
finally:
    print("不管抓住没有都要执行")
    # -->抓住啦
    # -->不管抓住没有都要执行


#finally语句的作用，经常当作收尾工作，比如关闭文件、关闭数据库连接等。
try:
    f=open('test.txt','w')
    f.write('hello world\nhello python')
except:
    print("写入文件失败了")#这句不会被执行，因为上面的代码没问题。
finally:
    f.close()

#异常也可以嵌套：
try:
    try:
        print(1/0)
    except:
        print('内层异常被捕获了')
    print('hello'+1)
except:
    print('外层的异常被捕获了')
finally:
    print('不管内层还是外层的异常，finally中的代码都要执行')


#用raise语句主动抛出异常：
# raise Exception('这是一个异常')
def func(a,b):
    if b==0:
        raise Exception('除数不能为0')
        return a/b#这个不会执行，因为raise语句抛出异常后，函数就会立即终止，不会继续执行后面的代码了。
        #除非把它移到外层，与if语句平级，这样当b不为0时，函数就会正常执行，返回a/b的结果。

# raise 不能创造出新的异常，只能抛出已经存在的异常类的实例。

#如果raise抛出的是错误的异常类型，python解释器会抛出TypeError异常，提示我们抛出的异常类型不正确。
print('-'*88)
try:
    print(1/0)
except:
        raise Exception('NameError')  #报错，应该是ZeroDivisionError,而不是什么NameError


