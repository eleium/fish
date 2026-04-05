# 字典的 改：
d = dict.fromkeys('fishC')
print(d)  # --->{'f':None,'i':None,'s':None,'h':None,'C':None}
d['f'] = 100
print(d)

# update()
d.update(ishC=230)
print(d)  # -->{'f':100,'i':None,'s':None,'h':None,'C':230} 增加了一个键值对：ishC:230
