# 模块  module 是一种代码的打包手段。
# 把重复出现的代码，打包成函数的形式，只需要调用函数，就可以实现代码的重复

# 类和对象来源于对现实世界的模拟，运用类和对象的打包思维，任何事物都可以看成是对象的属性和方法的有机结合。
# 属性决定了对象的静态特征，方法实现了对象的动态能力。所以现在绝大部分是 面向对象编程。包括python自身的构建。

# 类还不是打包的最高阶段，只是在一个程序里，被重复实例化为多个对象。是同一个程序里。
# 比类更高阶的打包方案是模块。它使得一个或多个源代码被一个过多个程序重复使用。是pyhton里的最高组织结构，也是最高层次的代码重用手段。

# python成为主流语言，因为简洁的语言和严苛的编程风格，以及大量的模块。
# 用python编程，第一件事是实现什么事情，实现什么功能，需要用到哪些模块的组合。各种模块在pipy上。

# 不需要重复造轮子，而要把精力放到程序的执行逻辑上面。

# 导入的模块，是已经存在的。自己创造的模块，就是用编辑模式，创建一个python的源代码的文件的时候，就同时创建了程序模块。

# 1，比如新建一个hello.py文件，并编辑内容：定义两个函数:

# def say_hi():
#     print('hi python')
# def say_hello():
#     print('hello python')

# 2，再创建另一个源文件：call_hello.py
# 3，在 call_hello.py中，调用hello.py里创建的两个函数：将hello.py导入： import hello

import hello


hello.say_hi()
# --->hi python
hello.say_hello()
# --->hello python
#hello.py作为自己定义的模块，里面封装的两个函数，在另一个程序中被成功的调用了

#python 有三种导入模块的方式：
#1  import 模块名  在导入后，用<模块名称>.<对象名称>的方式来调用使用
#2，from 模块名 import 对象名称
#3，import 模块名 as 关联名称


import hello

hello.say_hi()
#--->hi python
hello.say_hello()
#--->hello pyhton
#第一种导入方式，<模块名>.<对象名称>，先写模块名，然后调用具体的要使用的对象名

# ——————---------————————----------——————————————----


from hello import say_hi,say_hello

say_hi()
#---->hi python

say_hello()
#---->hello python
#第二种导入方式：直接导入了模块封装的函数： 使用方法：直接<对象名称>
#这种导入方式，有一个不推荐的方法：from 模块名 import *,这是在要导入的对象很多的情况下，直接导入该模块里面的所有对象。
#这种导入方式的优势，就是调用的时候不用再写模块名了。

#要注意的是，被导入的模块里面的对象的名称不能违规，比如定义了一个def int(x)--->print(f'哈哈{x}'),此时再调用，就会报错：
from hello import *
print(int('500'))
#--->哈哈500    而没有得到int('500')的正常整数化500的结果，名字被覆盖了
print('--  --'*40)

#另外一种情况：两个模块，有一个相同名字的对象。然后用第二种方案的from import的语法来调用，就出问题啦。

#再创建一个文件：hello_from_the_other_side.py，然后导入

from hello import say_hi,say_hello
from hello_from_the_other_side import *

say_hi()
say_hello()
int('500')
#--->hi啊你好呀python
#---> hello啊python
#--->哈哈500
#根本没有调用导入的第一个文件(模块)里面的与第二个模块相同名字的函数对象：后导入的模块方法，覆盖了先导入的模块的同名对象方法。

#第三种导入模块的方案：适合模块的名字比较长的情况下，用关键字as，关联一个新的名称 import 模块名 as 关联的简洁的名字：

from hello import *
import hello_from_the_other_side  as h


say_hi()
say_hello()
#--->hi python
# --->hello python
h.say_hi()
h.say_hello()
#--->hi啊你好呀python
#---> hello啊python
#优点：同时避免了名字冲突的问题，也简化了模块名

#以上是被导入的文件与主文件都在同一个目录（文件夹 ）的情况。如果不在同一个目录，就用相对或绝对目录：


# 1,相对导入（需要作为包运行） 要求被导入的模块是在主文件的子目录里，并且有一个 __init__.py文件。
# main.py 导入 helper.py：
# from utils import helper  # ✅ 可以，因为 utils 是子目录
# 但要注意： 这种写法要求 utils 目录下有一个 __init__.py 文件（可以是空文件），让 Python 把它当作一个包。


# 2,修改 sys.path（动态添加路径） 父目录或其他位置
# import sys  先导入sys包
# sys.path.append('./utils')  # 把 utils 目录加入搜索路径
# import helper  # ✅ 现在可以直接导入
# helper.hello()

#3，使用绝对路径导入（Python 3.3+）   父目录或者其他位置，也必须有 __init__.py文件
# 如果项目结构清晰，可以使用绝对导入：
# main.py
# from utils import helper