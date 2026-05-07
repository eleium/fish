#用try ...except处理异常：
#异常的种类很多，常见的有：
#ZeroDivisionError:Division by zero :除数为零错误。
# print(10/0)#--->ZereDivisonError:Division by zero

#SyntaxError:Invalid character : 语法错误
#NameError:名称错误


#TypeError:类型错误
# print('hello'+1)#--->TypeError:can only concatenate str (not "int") to str


#处理异常：用try把你觉得可能出问题的代码包裹起来，然后用except来处理异常：
try:
    print(1/0)#这是一段你觉得会报错的内容
# except ZeroDivisionError:#你觉得会是ZeroDivisonError这个错误
#     print('除数是零，搞错啦。')#你希望如故真的是这个错误，就发出这个提示。
#只有代码真的是ZeroDivisionError这个类型的错误，except ZeroDivisionError才会执行。否则python还是报错，红彤彤一片。

    #或者你不知道会是什么错误，你就用except Exception来处理：
except :
    print('出错了，不知道是啥错')

#如果try里面的代码没有出错，那么except里面的代码就不会执行：
try:
    print(1 / 1)
except Exception:
    print('出错了')
#这次try代码正确，所以except代码不执行。
#except和except Exception的区别：前者except捕获一切异常，包括系统级错误。而后者只捕获绝大多数异常，不包括系统级错误。

#用as给出一个异常对象：
try:
    print(1/0)
except Exception as e:#把异常对象命名为e,这个错误将是ZeroVivisionError这个错误，e就是Division by zero.
    print(f'出错啦，犯的是{e}这个错误')

#如果我们不知道会有多个错误，就用元组的方式把可能的错误都列出来：
try:
    print(1/0)
    print('hello'+1)
except (ZeroDivisionError,TypeError) as e:
    print(f'出错啦，犯的是{e}这个错误')
#try-except语句将会捕获异常，并且程序不会崩溃，而是继续执行except块中的代码。显示出到底是哪个出错了。
#或者直接用pass来忽略错误：
try:
    print(1/0)
    print('hello'+1)
except (ZeroDivisionError,TypeError):
    pass
#此时python什么都不会发生，因为只要检测出是ZeroDivisonError或者TypeErroe中的一个错误，pass就会被执行，程序继续往下走。
print('-'*80)

#或者把except分开，分别处理不同的错误：这样更加清晰：
try:
    print(1/0)
    print('hello'+1)
except ZeroDivisionError as e:
    print(f'出错啦，犯的是{e}这个错误')
except TypeError as e:
    print(f'出错啦，犯的是{e}这个错误')
#检测到第一个错误后，就会执行第一个except块中的代码，第二个except块中的代码就不会执行了。