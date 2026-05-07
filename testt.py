#glob 是 Python 内置模块，用于按模式匹配查找文件路径，就像"模糊搜索"一样。
import glob
from pathlib import Path


p=Path('.')
p.glob('*.txt')
p.glob('*.py')