a = 3
b = 5
if a < b:
    simall = a
else:
    simall = b
print(simall)

print(simall) if a < b else print(simall)


score = int(input('你的分数：'))
print(
    '不及格' if score <= 60 else
    '及格' if score <= 70 else
    '合格' if 70 < score <= 80 else
    '良好' if 80 < score <= 90 else
    '优秀' if 90 < score < 100 else
    '天才' if score == 100 else
    '别瞎几把填，写入1-100的分值'
)

leval=( '不及格' if score <= 60 else
    '及格' if score <= 70 else
    '合格' if 70 < score <= 80 else
    '良好' if 80 < score <= 90 else
    '优秀' if 90 < score < 100 else
    '天才' if score == 100 else
    '别瞎几把填，写入1-100的分值')
print(leval)

