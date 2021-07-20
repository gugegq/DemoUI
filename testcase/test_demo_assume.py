#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

import pytest


@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    pytest.assume(x == y)
    pytest.assume(True)
    pytest.assume(False)

# @pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
# def test_simple_assume(x, y):
#     with pytest.assume:
#         assert x == y
#         assert True
#         assert False

# def test_add2():
#     pytest.assume(1 + 4 == 5)
#     # pytest.assume(1 + 5 == 6)
#     # pytest.assume(1 + 6 == 7)
#
#     pytest.assume(1 + 3 == 3)
#     pytest.assume(2 + 5 == 7)
#     pytest.assume(2 + 5 == 9)
#     print("测试完成")

# def test_assert():
#     pytest.assume(1, 3)
#     pytest.assume(1, 1)
#     pytest.assume("test", 3)
#     print("\n我是软断言assume，断言失败，也会执行！")