# 字典的 改：
d = dict.fromkeys('fishC')
print(d)  # --->{'f':None,'i':None,'s':None,'h':None,'C':None}
d['f'] = 100
print(d)

# update()
d.update(ishC=230)  # 添加一个键值对，字典里原来没有该键值对。
print(d)  # -->{'f':100,'i':None,'s':None,'h':None,'C':None,'ishC':230}
# 增加了一个键值对：ishC:230

d.update({"i": 100, "s": 200})
print(d)  # -->{'f':100,'i':100,'s':200,'h':None,'C':None,'ishC':230}
