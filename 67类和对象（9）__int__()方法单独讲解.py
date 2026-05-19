class ZH_INT:
    def __init__(self, num):
        self.num = num

    def __int__(self):
        try:
            return int(self.num)
        except ValueError:
            #fmt:off
            zh = {"零": 0,"一": 1,"二": 2,"三": 3,"四": 4,"五": 5,"六": 6,"七": 7,"八": 8,"九": 9,
                "壹": 1,"贰": 2,"叁": 3,"肆": 4,"伍": 5,"陆": 6,"柒": 7,"捌": 8,"玖": 9,
            }
            #fmt:on
            result = 0
            #result=0起到什么作用？是try语句的一部分吗？

            for each in self.num:
                if each in zh:
                    #zh有定义吗？有。zh={字典}
                    result += zh[each]
                else:
                    result += int(each)
                result *= 10
            return result // 10
            #上面两行的作用是啥？


n = ZH_INT("五二零")

print(int(n))
#--->520

#--------------------------------------------------------------------------
class MyClass:
    def __len__(self):     # 必须是这个名字
        return 10

obj = MyClass()
print(obj.__len__())
print(len(obj))  # 输出 10

class Test:
    def __abc__(self):
        return "hello"

t = Test()
print(t.__abc__())     # 可以手动调用，输出 "hello"
# 但 Python 不会自动调用它，因为没有对应的内置操作