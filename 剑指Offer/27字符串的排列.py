"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""

from itertools import permutations


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.result = []

    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        self.perm(0, ss)
        return sorted(list(set(self.result)))

    # begin之前位置是固定好了的，现在来选string[begin]
    def perm(self, begin, string):
        if begin == len(string) - 1:
            self.result.append(string)
            return
        for i in range(begin, len(string)):
            temp = string[:begin] + string[i] + string[begin:i] + string[i + 1:]
            self.perm(begin + 1, temp)


class Solution2:
    def Permutation2(self, ss):
        # write code here
        if not ss:
            return []
        return sorted(list(set(map(''.join, permutations(ss)))))