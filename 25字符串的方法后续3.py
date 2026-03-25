'''
截取方法：
strip(chars=None)
lstrip(chars=None)
rstrip(chars=None)
removeprefix(prefix)
removesuffix(suffix)
'''

print('    左侧不要空白'.lstrip())#---->左侧不要空白
print('右侧不要空白    '.rstrip())#---->右侧不要空白
print('    两侧不要空白    '.strip())#---->两侧不要空白
#chars=None:空白，该方法就是去除空白留白。

print('--'*40)
x='www.ilovefishc.com'
print('www.python.com'.lstrip('wp'))#.python.com
print('www.ilovefishc.com'.lstrip('wcom.'))#---->ilovefishc.com
print('www.ilovefishc.com'.rstrip('wcom.'))#---->www.ilovefishc
#strip()里面的参数chars='wcom.'代表的是5个独立的字符：w/c/o/m/.而不是一个字符串。
#它会从左 右两侧，连续删除所有出现在这个集合里的字符，直到遇到第一个不在集合里的字符为止
print(x)