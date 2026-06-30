#字符串的相关： 判断一个整数字是否回文数（正序和倒序读起来都一样的整数）
s=(input('输入整数：'))

# if s==s[::-1]:
#     print('是回文数')
# else:
#     print('不是回文数')

print(f'是回文数' if s==s[::-1] else '非回文数')

#大小写字母换来换去的方法：capitalize()  casefold() title() swapcase()  upper()  lower()

r='I love FishC.'
print(r.upper())#所有字母大写
print(r.capitalize())#首字母大写，其他字母小写
print(r.lower())#所有字母小写
print(r.casefold())#所有字母小写----包括其他语言比如德语等等
print(r.title())#每个单词的首字母大写
print(r.swapcase())#将字符串的大小写的字母反转。

#以上六个print语句每一个都是生成新的字符串，而下一个print调用的还是原字符串。而不是调用上一个print结果。
print('888'*50)
#字符串的左中右对齐：
#center(width fillchar='') ljust(width fillchar='')  rjust(width fillchar='')  zfill(width)

x='有内鬼，交易停止!'
y=x.center(80,'世')#输入的参数小于原字符串的下标数  5<9，输出原字符串.
# 若>9，两侧平均分布，插入的必须是一个字符。
print(y)
y=x.ljust(15,'m')#原字符串9个，15-9=6，所以字符串在左，右侧会添加6个m.
print(y)
print(x.rjust(15,'m'))
print(x.zfill(13))#当n小于原字符串时，直接显示原字符串

w=str(-520)
print(w.zfill(5))#整数不能用zfill()方法,所以先用str转化一下。
print('hello world')
print('hello')
