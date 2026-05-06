f = open("fish.txt", "a", encoding="utf-8")
f.write("hello,my friend.")
# print(f.read())  # 读取文件内容是空的，因为文件指针已经在文件末尾了。
# 要想用print函数读取文件内容，需要将文件指针移动到文件开头。

f.seek(0)

print(f.read())  # "a"是只写模式，不可读。想要读取，改成"a+"
# "w"表示只写。而且是覆盖写。把所有以前的内容全部删除，然后写入新的内容。。
#'a+' 表示：文件不存在 → 创建.  如果存在 → 在末尾追加 ,也能读取 ✅
f.close()
# 如果程序在执行期间出错了，就不会执行f.close().就会一直占用资源。除非用with语句：
with open("fish.txt", "a", encoding="utf-8") as f:
    f.write("\n谢谢你，我爱你")

