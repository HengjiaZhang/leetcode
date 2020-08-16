"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):

        def isValidPlace(row, col):
            return 0 <= row < total_row and 0 <= col < total_col and visited[row][col] == 0

        # write code here
        if not matrix or matrix == [[]]:
            return []
        # 定义四个方向
        drow = [0, 1, 0, -1]
        dcol = [1, 0, -1, 0]

        total_row = len(matrix)
        total_col = len(matrix[0])

        visited = [[0 for _ in range(total_col)] for _ in range(total_row)]

        direction = 0
        col = 0
        row = 0
        result = []

        while True:
            result.append(matrix[row][col])
            visited[row][col] = 1
            if isValidPlace(row + drow[direction], col + dcol[direction]):
                col += dcol[direction]
                row += drow[direction]
            else:
                direction += 1
                direction %= 4
                if isValidPlace(row + drow[direction], col + dcol[direction]):
                    col += dcol[direction]
                    row += drow[direction]
                else:
                    return result

so = Solution()
print(so.printMatrix([[1,2],[3,4],[5,6]]))

