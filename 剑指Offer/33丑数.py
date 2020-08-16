"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0

        uglyList = [1] * index
        p2 = 0  # 2 * uglyList[p2] 可能成为下一个丑数,
        # 如果 2 * uglyList[p2]是下一个丑数，那么p2 += 1
        p3 = 0  # 3 * uglyList[p3] 可能成为下一个丑数
        p5 = 0  # 5 * uglyList[p5] 可能成为下一个丑数
        for i in range(1, index):
            newUgly = min(uglyList[p2] * 2, uglyList[p3] * 3, uglyList[p5] * 5)
            uglyList[i] = newUgly
            if newUgly % 2 == 0:
                p2 += 1
            if newUgly % 3 == 0:
                p3 += 1
            if newUgly % 5 == 0:
                p5 += 1
        return uglyList[index - 1]