#跟属性访问相关的函数和魔法方法
#对象可以通过(.)来进行属性访问，可以访问一个已有属性，还可以创建一个新属性
#python有几个BIF()函数: hasattr()判断是否有这个属性,
# getattr(),获取这个对象的属性，包括私有属性
# setattr()，增加这个对象的属性
# delattr()删除这个对象的属性
# 专门为对象的属性访问服务的。


class C():
    def __init__(self,name,age):
        self.name=name
        self.__age=age
c=C('小甲鱼',18)
print(hasattr(c,"name"))
#--->True

print(getattr(c,"name"))
#--->小甲鱼
print(getattr(c,"_C__age"))
#--->18

setattr(c,"_C__age",20)
print(getattr(c,"_C__age"))
#-->20

# getattr(obj, "name") 不是错
# 但如果属性名是固定的字符串，就和 obj.name 完全一样
# 所以没有必要用 getattr，直接用 obj.name 更清晰  直接用print(c.name),或者：print(c._C__age)

#delattr的用法与del()的用法一样。
delattr(c,"_C__age")
print(hasattr(c,"_C__age"))
#--->false
