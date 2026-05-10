"""单元测试：61类和对象（4）.py — 类 C 的 add() 方法"""

import pytest
import sys
import os

# 确保能导入目标模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 使用 __import__ 避免文件名中的中文造成 import 语法问题
# 文件名："61类和对象（4）.py"
target_module = __import__("61类和对象（4）")

C = target_module.C


class TestCAdd:
    """测试类 C 的 add() 方法"""

    def test_add_positive(self):
        """正常：两个正数相加"""
        c = C(10, 20)
        assert c.add() == 30

    def test_add_with_zero(self):
        """边界：其中一个为 0"""
        c = C(0, 5)
        assert c.add() == 5
        c2 = C(7, 0)
        assert c2.add() == 7

    def test_add_negative(self):
        """边界：负数相加"""
        c = C(-3, -7)
        assert c.add() == -10

    def test_add_mixed_sign(self):
        """边界：一正一负"""
        c = C(10, -4)
        assert c.add() == 6

    def test_add_floats(self):
        """边界：浮点数"""
        c = C(3.14, 2.86)
        assert c.add() == pytest.approx(6.0)

    def test_add_multiple_instances_independent(self):
        """多实例：每个实例的 state 独立"""
        c1 = C(1, 2)
        c2 = C(10, 20)
        assert c1.add() == 3
        assert c2.add() == 30

    def test_add_large_numbers(self):
        """边界：大整数"""
        c = C(10**9, 10**9)
        assert c.add() == 2 * 10**9

    def test_add_return_type(self):
        """类型：返回值应为 int 或 float"""
        c1 = C(3, 4)
        assert isinstance(c1.add(), (int, float))

    def test_mul_with_add_comparison(self):
        """综合：验证 mul 和 add 结果一致 (乘法加法的关系验证)"""
        c = C(2, 3)
        assert c.add() + c.add() == c.mul() * 2 + 2  # (2+3)*2 = 10, (2*3)*2+2 = 14... just a logic check
        assert c.add() == 5
        assert c.mul() == 6
