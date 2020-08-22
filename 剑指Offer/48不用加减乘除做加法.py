"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""


# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            c = ((num1 & num2) << 1) & 0xffffffff
            num1 = (num1 ^ num2) & 0xffffffff
            num2 = c

        # （长度不超过31位）第32位是0
        if num1 <= 0x7fffffff:
            result = num1
        else:
            # result = ~(num1^0xffffffff)
            result = num1 - 2 * 0x80000000
        return result
