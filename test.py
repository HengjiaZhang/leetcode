class Solution:
    def GetNumberOfK(self, data, k):
        # write code here

        # 找到大于等于k的第一个数的位置
        low = 0
        high = len(data)
        while low < high:
            mid = (low + high) // 2
            if data[mid] < k:
                low = mid + 1
            else:
                high = mid

        # 找到大于k的第一个数的位置
        left = 0
        right = len(data)
        while left < right:
            mid = (left + right) // 2
            if data[mid] <= k:
                left = mid + 1
            else:
                right = mid

        return left - low


so = Solution()
print(so.GetNumberOfK([1,2,2,2,2,3,4,], 2))