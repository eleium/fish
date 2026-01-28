# 小甲鱼的课程开课，前面讲解了配置python,利用其IDEL交互式和编辑器式开始
# 一个小游戏：
temp = input('不妨猜一下小甲鱼现在心里想的是哪个数字：')
guess = int(temp)

if guess == 8:
    print('猜猜对啦！')
    print('但是没有奖励哦。')
else:
    print('没有蒙对哦。')

    print('结束啦，没啥意思。')  # 这一行的缩进在else下，猜错运行。
# print('结束啦，没啥意思。')#这一行的缩进在if下，猜对猜错都会运行。
#
# 不同的项目可以有不同的环境配置，太棒了。


'''
如何把新的project项目上传到github上：
1:在本地新建一个项目project
2:在这个新的项目里,打开bash here.
3:在bash窗口里：git init,初始化这个项目文件夹为可以版本控制。
4:创建README.md（可选） echo '#My Project'>READ.md(推荐每个仓库都创建一个readme文件。
5：git add . 添加所有文件到暂存区。
6：git commit -m 'first commit or Initial commit'  提交更改。引号内是说明信息。
7；在github上新建仓库，命名与这个项目相关
8：git remote add origin git@github.com:仓库名/repo.git 添加远程仓库地址
9：git push -u origin main  把本地文件推送到github 仓库中。需要同步master与main

'''
