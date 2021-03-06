"""
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}，
{2,[3,4,2],6,2,5,1}，
{2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}，
{2,3,4,2,[6,2,5],1}，
{2,3,4,2,6,[2,5,1]}。
窗口大于数组长度的时候，返回空
"""


class Solution:
    def maxInWindows(self, num, size):
        if not num or not size or size > len(num):
            return []
        # index 存的是当前窗口最大值的位置的候选
        index = []
        result = []
        """
        1. 遍历数组的每一个数字，下标为i
        2. 如果容器(index)为空，则直接将当前位置(i)加入到容器中。
        3. 如果容器不为空，则让当前位置的数字(num[i])和容器的最后一个位置的数字(num[index[-1]])比较，
            如果大于，则将容器的最后一个位置的数字删除，
            然后继续将当前位置的数字数字和容器的最后一个位置的数字比较
        4. 直到当前元素小于容器的最后一个元素，则直接将当前元素的位置 i 加入到容器的末尾
        """
        for i in range(len(num)):
            while index and num[index[-1]] < num[i]:
                index.pop()
            index.append(i)
            # 判断容器头部的下标是否过期
            if index[0] + size <= i:
                index.pop(0)
            # 判断是否形成了窗口
            if i + 1 >= size:
                result.append(num[index[0]])
        return result