from hello import *

print(x)
say_hello()

# print(y)
# say_hi()

#--->500
#----> hello python

# NameError: name 'y' is not defined  另一个y变量没有被导入，所以报错。

# 这时候用另一种导入方案：就可以正常访问了。
import hello as h

print(h.x)
h.say_hello()

print(h.y)
h.say_hi()



#__all__属性还可以定义在__init__.py构造文件中。默认直接from ...import *语法导入一个包，无法访问包里面的模块 
#这时候在__init__.py里，用__all__=['模块1','模块2'],列表里面是字符串。就可以访问到这两个模块了。


#总结：对于模块，如果没有定义__all__属性，用from ... import * ,将导入该模块的所有东西。
#相反的， 对于包，如果没有定义__all__属性，那么from ... import * 将不导入任何模块。
