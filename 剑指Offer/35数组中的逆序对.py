"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
"""


class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        self.MergeSort(data)
        return self.count % 1000000007

    def MergeSort(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.MergeSort(data[:mid])
        right = self.MergeSort(data[mid:])
        return self.Merge(left, right)

    def Merge(self, list1, list2):
        result = []
        index1 = 0
        index2 = 0
        while index1 < len(list1) and index2 < len(list2):
            if list1[index1] <= list2[index2]:
                result.append(list1[index1])
                index1 += 1
            else:
                """
                出现逆序对
                算法1：list1[index1]及其后面所有的数都大于list2[index2]
                算法2：list2[index2]及其前面所有的数都小于list1[index1] (这是错的，可能算重，可能算漏)
                """
                self.count += (len(list1) - index1)
                # self.count += (index2 + 1) (错的)
                result.append(list2[index2])
                index2 += 1
        if index1 == len(list1):
            result.extend(list2[index2:])
        if index2 == len(list2):
            result.extend(list1[index1:])
        return result
