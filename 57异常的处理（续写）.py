# assert语句：只能抛出一个AssertionError异常。表示断言。通常用于代码调试。
s = "python"
assert s == "python"
# assert s != "python"  # --->AssertionError:s!='python'    这行注释掉，否则下面的代码就不会被执行了。
# 类似与if语句的条件判断，如果条件为True，assert语句就会继续执行后面的代码；
# 如果条件为False，assert语句就会抛出一个AssertionError异常，并且后面的代码不会被执行了。


# 利用异常，来实现goto:
try:
    while True:
        while True:
            while True:
                raise
            print("跳出来了~")
        print("跳出来了~")
    Print("跳出来了~")
except:
    print("到这里啦")

#与c语言的goto语句类似，python的raise语句可以跳出多层循环。