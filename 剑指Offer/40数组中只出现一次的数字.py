"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        xor = 0
        for i in array:
            xor ^= i

            # 在xor中找到第一个不同的位(第一个1)对数据进行分类，分别为两个队列算异或，找到我们想要的结果
        index = 1
        while index & xor == 0:
            index <<= 1

        result1 = 0
        result2 = 0
        for i in array:
            if i & index == 0:
                result1 ^= i
            else:
                result2 ^= i
        return [result1, result2]
