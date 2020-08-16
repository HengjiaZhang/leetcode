"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。例如矩阵
[[a, b, c, e],
 [s, f, c, s],
 [a, d ,e, e]]
中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.haspath = False

    def hasPath(self, matrixstring, rows, cols, path):
        # 输入的matrix是字符串，转化为二维数组
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        k = 0
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = matrixstring[k]
                k += 1
        print("The matrix is: ", matrix)
        for i in range(rows):
            for j in range(cols):
                visited = [[0 for _ in range(cols)] for _ in range(rows)]
                self.dfs(matrix, visited, i, j, path)
        return self.haspath

    def dfs(self, matrix, visited, i, j, path):
        rows = len(matrix)
        cols = len(matrix[0])
        if not path:
            self.haspath = True
            return
        if not (0 <= i < rows and 0 <= j < cols):
            return
        if visited[i][j] == 1:
            return
        if matrix[i][j] == path[0]:
            print("Now is visit matrix", (i, j))
            visited[i][j] = 1
            path = path[1:]
            self.dfs(matrix, visited, i + 1, j, path)
            self.dfs(matrix, visited, i - 1, j, path)
            self.dfs(matrix, visited, i, j + 1, path)
            self.dfs(matrix, visited, i, j - 1, path)


solution = Solution()
print(solution.hasPath("ABCESFCSADEE",3,4,"ABCCED"))

