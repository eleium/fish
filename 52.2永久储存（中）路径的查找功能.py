# 用glob()方法查找功能

from pathlib import Path
from pprint import pprint

# 查找当前目录的特定后缀文件：
p = Path(".")  # 当前目录
p.glob("*.txt")
pprint(list(p.glob("*.txt")))  # --->[]
p.glob("*.py")
pprint(list(p.glob("*.py")))

# 查找当前目录的下一级目录的特定后缀文件：
pprint(list(p.glob("./.venv/*.cfg")))

print("_" * 88)

# 查找当前目录及当前目录下的所有子目录:即查找当前目录以及所有递归子目录下的文件和文件夹
# pprint(list(p.glob('**./')))
"""
'**./' 这个模式是无效的。错误信息明确指出：'**' 只能作为完整的路径组件使用，不能和 ./ 连在一起。
glob 模式的正确用法
** 表示递归匹配所有子目录
* 表示匹配任意字符（不包括路径分隔符）
** 必须单独使用，前后应该有 / 或作为路径的一部分"""

pprint(list(p.glob("**/")))
print("-.-" * 88)
# 查找当前及递归子目录下的所有.py文件
pprint(list(p.glob("**/*.py")))
