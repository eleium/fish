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

#第三种导入模块的方案：适合模块的名字比较长的情况下，用关键字as，关联一个新的名称

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