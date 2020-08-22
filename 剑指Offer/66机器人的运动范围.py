"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？
"""


# -*- coding:utf-8 -*-
# 递归 深度优先搜索
# 用矩阵来记录访问过的点，访问过了就设置为1，否则就是0
class Solution:
    def __init__(self):
        self.rows = None
        self.cols = None
        self.threshold = None
        self.visited = None

    def movingCount(self, threshold, rows, cols):
        # write code here
        self.rows = rows
        self.cols = cols
        self.visited = [[0 for i in range(cols)] for j in range(rows)]
        self.threshold = threshold
        self.dfs(0, 0)
        return sum(sum(i) for i in self.visited)

    # 深度优先搜索
    def dfs(self, i, j):
        # 越界
        if i >= self.rows or j >= self.cols or i < 0 or j < 0:
            return
        # 已经访问过了
        if self.visited[i][j] == 1:
            return
        # 行坐标和列坐标的数位之和大于threshold
        if self.get_sum(i, j) > self.threshold:
            return

        self.visited[i][j] = 1
        self.dfs(i, j + 1)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i - 1, j)

    # 计算这个方格所有位数的和
    def get_sum(self, i, j):
        sums = 0
        while i:
            sums += i % 10
            i //= 10
        while j:
            sums += j % 10
            j //= 10
        return sums


# -*- coding:utf-8 -*-
# 递归 深度优先搜索
# 把访问过的点加入到列表中
class Solution2:
    def __init__(self):
        self.rows = None
        self.cols = None
        self.threshold = None
        self.visited = []

    def movingCount(self, threshold, rows, cols):
        # write code here
        self.rows = rows
        self.cols = cols
        self.threshold = threshold
        self.dfs(0, 0)
        return len(self.visited)

    # 深度优先搜索
    def dfs(self, i, j):
        # 越界
        if i >= self.rows or j >= self.cols or i < 0 or j < 0:
            return
        # 已经访问过了
        if (i, j) in self.visited:
            return
        # 行坐标和列坐标的数位之和大于threshold
        if self.get_sum(i, j) > self.threshold:
            return

        self.visited.append((i, j))
        self.dfs(i, j + 1)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i - 1, j)

    # 计算这个方格所有位数的和
    def get_sum(self, i, j):
        sums = 0
        while i:
            sums += i % 10
            i /= 10
        while j:
            sums += j % 10
            j /= 10
        return sums


# -*- coding:utf-8 -*-
# 广度优先搜索，结果是对的。但是太慢了过不了测试，因为会重复探索格子。
class Solution3:
    def movingCount(self, threshold, rows, cols):
        def isValidPlace(x, y):
            if not(0 <= x < rows and 0 <= y < cols):
                return False
            if matrix[x][y] == 1:
                return False
            if self.get_sum(x, y) > threshold:
                return False
            return True
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        matrix[0][0] = 1
        queue = [(0, 0)]
        while queue:
            place = queue.pop(0)
            x = place[0]
            y = place[1]
            matrix[x][y] = 1
            if isValidPlace(x+1, y):
                queue.append((x+1, y))
            if isValidPlace(x-1, y):
                queue.append((x-1, y))
            if isValidPlace(x, y+1):
                queue.append((x, y+1))
            if isValidPlace(x, y-1):
                queue.append((x, y-1))
        return sum(sum(i) for i in matrix)

    # 计算这个方格所有位数的和
    def get_sum(self, i, j):
        sums = 0
        while i:
            sums += i % 10
            i //= 10
        while j:
            sums += j % 10
            j //= 10
        return sums


# -*- coding:utf-8 -*-
# 广度优先搜索,这样就能过测试了
class Solution4:
    def movingCount(self, threshold, rows, cols):
        if threshold < 0:
            return 0
        def isValidPlace(x, y):
            if not(0 <= x < rows and 0 <= y < cols):
                return False
            if matrix[x][y] != 0:
                return False
            if self.get_sum(x, y) > threshold:
                # matrix[x][y] = -1
                return False
            return True
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        matrix[0][0] = 1
        queue = [(0, 0)]
        while queue:
            place = queue.pop(0)
            x = place[0]
            y = place[1]
            if isValidPlace(x+1, y):
                queue.append((x+1, y))
                matrix[x+1][y] = 1
            if isValidPlace(x-1, y):
                queue.append((x-1, y))
                matrix[x-1][y] = 1
            if isValidPlace(x, y+1):
                queue.append((x, y+1))
                matrix[x][y+1] = 1
            if isValidPlace(x, y-1):
                queue.append((x, y-1))
                matrix[x][y-1] = 1
        return sum(sum(i) for i in matrix)

    # 计算这个方格所有位数的和
    def get_sum(self, i, j):
        sums = 0
        while i:
            sums += i % 10
            i //= 10
        while j:
            sums += j % 10
            j //= 10
        return sums