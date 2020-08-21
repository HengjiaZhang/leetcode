"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""

import functools


# -*- coding:utf-8 -*-
class Solution:
    """
    In Python2, sort allowed an optional function (cmp参数)
    which can be called for doing the comparisons.
    That function should take two arguments to be compared and then
    return a negative value for less-than,
    return zero if they are equal, or
    return a positive value for greater-than.
    """

    def PrintMinNumber2(self, numbers):
        s = list(map(str, numbers))
        s.sort(cmp=lambda x, y: int(x + y) - int(y + x))
        return "".join(s)

    """
    Python3 弃用了cmp， 所以要把cmp参数转成key参数

    The value of the key parameter should be a function that takes a single argument 
    and returns a key to use for sorting purposes.

    In Python 3.2, the functools.cmp_to_key() function was added to the 
    functools module in the standard library.
    """
    def PrintMinNumber(self, numbers):
        s = list(map(str, numbers))
        # s.sort(key=functools.cmp_to_key(self.my_cmp))
        s.sort(key=functools.cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
        return "".join(s)

    def my_cmp(self, x, y):
        return int(x + y) - int(y + x)
