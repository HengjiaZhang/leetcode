"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""

from itertools import permutations


# -*- coding:utf-8 -*-
class Solution:
    def Permutation2(self, ss):
        # write code here
        if not ss:
            return []
        return sorted(list(set(map(''.join, permutations(ss)))))

    def Permutation(self, ss):
        if not ss:
            return []
        result = []
        self.perm(0, ss, result)
        return sorted(list(set(map(''.join, result))))

    # position之前位置是固定好了的，现在来选string[position]
    def perm(self, position, string, result):
        if position == len(string) - 1:
            result.append(string)
            return
        for i in range(position, len(string)):
            temp = string[:position] + string[i] + string[position:i] + string[i + 1:]
            self.perm(position + 1, temp, result)

