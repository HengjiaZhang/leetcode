"""
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
"""


# -*- coding:utf-8 -*-
class Solution2:
    def NumberOf1(self, n):
        # python通过bin(n & 0xffffffff)获得的并不是这个负数的补码，只是形式与负数的32位二进制补码相同。
        return bin(n & 0xFFFFFFFF).count('1')

    # -*- coding:utf-8 -*-


class Solution:
    def NumberOf1(self, n):
        count = 0
        for i in range(32):
            count += (n >> i) & 1
        return count