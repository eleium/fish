#14个字符串方法，都是判断和检测：返回的都应该是一个bool类的值 ： True 或者 False


#方法的参数有中括号表示是可选参数。
#中括号仅用于「文档 / 说明层面的标记」，不是代码里的语法—— 实际写代码调用方法时，不能给参数加中括号！

"""
startswith(prefix[,start[,end]])  用于判断 子字符串是否处于字符串的起始位置,可选参数指定起始、结束位置
endswith(suffix[,start[,end]])    用于判断 子字符串是否处于字符串的末尾，可选参数指定起始、结束位置。

一、先搞懂 prefix 和 suffix 的字面意思 + 核心作用
这两个是英文单词，对应方法的核心参数，理解字面意思就能记住作用：
表格
单词	中文含义	        方法中的作用
prefix	前缀	        startswith() 的必选参数，表示 “要判断字符串是否以这个内容开头” 的目标子串
suffix	后缀	        endswith() 的必选参数，表示 “要判断字符串是否以这个内容结尾” 的目标子串
简单说：
prefix = 「开头要找的内容」，suffix = 「结尾要找的内容」；
两个参数都支持单个字符串（如 'py'）或元组（如 ('py', 'java')），元组表示 “多选一匹配”（有一个匹配就返回 True）。

isupper()     用于判断 字符串是否是大写
islower()     用于判断 字符串是否是小写
istitle()     用于判断 每个单词的首字母大写，其余字母全小写，且字符串非空.这叫： 标题模式。
isalpha()     用于判断 字符串是否全部由字母组成，且不能包含空格，符号，数字
isascii()     用于判断 字符串是否全部由ASCII组成 字符串中所有字符的 ASCII 编码在 0-127 范围内，就返回 True。
isspace()     用于判断 字符串里面是否全部由空白字符组成（空格 / 换行 / 制表符等），且非空
isprintable() 用于判断 字符串是否可以打印
isdecimal()   用于判断 字符串是否都是由10进制的数组成（0-9）
isdigit()     用于判断 字符串是否由数字字符组成
isnumeric()   用于判断 字符串是否由数值字符组成，范围最广，非空
isalnum()     用于判读 字符串是否全部由数字和字母组成，不含符号
isidentifier()用于判读 字符串是否由 PYTHON的合法的标识符组成
"""
#startswith()  用于判断 子字符串是否处于字符串的起始位置
print('today is monthday'.startswith('monthday'))#---->False

x='我爱python'
print(x.startswith('我'))
print(x.startswith('我',1))#---->False:我的下标是：0



#endswith()    用于判断 子字符串是否处于字符串的末尾
print('today is monthday'.endswith('monthday'))#---->True
print(x.endswith('py',0,4))#---->True:从0到4下标（不含4），里面以py结尾。

x='他爱python'
if x.startswith(('你','我','他')):#元组里有多个待匹配字符串，有一个匹配成功就可以。
    print('我们都爱python')

print('-'*50)


#startswith()  用于判断 子字符串是否处于字符串的起始位置
print('today is monthday'.startswith('today'))#---->True

#isupper()     用于判断 字符串是否是大写
print('today is monthday'.isupper())#---->False

#islower()     用于判断 字符串是否全部是小写
print('today is monthday'.islower())#---->True


#istitle()     用于判断 每个单词的首字母大写，其余字母全小写，且字符串非空.这叫： 标题模式。
print('today is monthday'.istitle())#---->False  每个单词的首字母不是大写


#isalpha()     用于判断 字符串是否全部由字母组成，且不能包含空格，符号，数字
print('today is monthday'.isalpha())#---->False   字符串全是字母，但是有空格,空格不是字母。

print('-'*50)


#isascii()     用于判断 字符串是否全部由ASCII组成 字符串中所有字符的 ASCII 编码在 0-127 范围内，就返回 True。
print('how are your sun 12 years Bob?'.isascii())#---->True

#isspace()     用于判断 字符串里面是否全部由空白字符组成（空格 / 换行 / 制表符等），且非空
print('hello world'.isspace())#---->False
print('  '.isspace())#---->True


#isprintable() 用于判断 字符串是否可以打印
print('hello world'.isprintable())#---->True
print('hello world\n'.isprintable())#---->False:\n是转义字符，不是可打印字符


#isdecimal()   用于判断 字符串是否都是由10进制的数组成（0-9）
print('123'.isdecimal())#--->True
print('hello'.isdecimal())#---->False

#isdigit()     用于判断 字符串是否由数字字符组成
print('hello'.isdigit())#---->False
print('1234'.isdigit())#---->True

#isnumeric()   用于判断 字符串是否由数值字符组成，范围最广，非空.全部由字母（a-z/A-Z）或数字（0-9）组成
print('hulllaaa'.isnumeric())#---->False 必须是数值，如:三 ，44，four
print('三four44'.isnumeric())#---->False four英文数不行
print('三99'.isnumeric())#---->True
'''
能被 isnumeric() 识别的数值字符（返回 True）：
普通阿拉伯数字：0-9（如 '123'）；
中文数字：零、壹、贰、叁、仟、万、亿（如 '壹贰叁'）；
罗马数字：Ⅰ、Ⅱ、Ⅲ、Ⅹ、Ⅻ（如 'ⅩⅤ'）；
分数 / 次方类数值字符：½、⅓、²、³（如 '½'）；
其他语言的数值字符：如日语数字 壱、弐 等。
❌ 不能被识别的（返回 False）：
小数（.）、负数（-）、科学计数法（e）：如 '12.3'、'-45'、'1e3'；
空格、字母、符号：如 '12 3'、'12a'、'12!'；
空字符串：'''''


#isalnum()     用于判读 字符串是否全部由数字和字母组成，不含符号
print('44aa'.isalnum())#---->True

#isidentifier()用于判读 字符串是否由 PYTHON的合法的标识符组成
print('_code123H/*%W'.isidentifier())#---->False  与python 文件名命名规则类似。
print('I_love_520'.isidentifier())#---->True
print('520_I_love'.isidentifier())#---->False

'''
首字符：只能是字母（a-z/A-Z） 或 下划线（_）（不能是数字、符号）；
其余字符：只能是字母、数字、下划线（不能是任何符号，如 /、*、% 等）；
非空字符串（空串返回 False）；
不能是 Python 关键字（但关键字本身调用 isidentifier() 会返回 True，比如 'class'.isidentifier() → True）。
'''
x='I Love Python'
print(x.istitle())#---->True
print(x.upper().isupper())#---->True
print(x)#---->I Love Python#  返回的还是原来的x没有被upper过。
#！！！！ 所有字符串方法都不能改变原字符串！！！字符串不可变！！！


x='2²'
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())

x='一二三'
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())

#由上：isnumeric()范围最广，isdigit()次之，isdecimal()范围最小


import keyword
print(keyword.iskeyword('if'))#判断一个字符串是不是python的保留字符串。要先导入keyword模块。