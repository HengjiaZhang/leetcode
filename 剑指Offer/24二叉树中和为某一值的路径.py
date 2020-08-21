"""
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    # 返回二维列表，内部每个列表表示找到的路径
    # 先找到所有路径，再对每个路径分别判断和是否为expectNumber
    def __init__(self):
        self.path = []

    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        self.GetPath(root, [root.val])
        result = []
        for i in self.path:
            if sum(i) == expectNumber:
                result.append(i)
        return result

    def GetPath(self, root, path):
        if root.left is None and root.right is None:
            self.path.append(path)
        if root.left:
            self.GetPath(root.left, path + [root.left.val])
        if root.right:
            self.GetPath(root.right, path + [root.right.val])


class Solution2:
    # 返回二维列表，内部每个列表表示找到的路径
    # 添加路径的时候直接判断
    def __init__(self):
        self.path = []

    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        self.expectNumber = expectNumber
        self.GetPath(root, [root.val])
        return self.path

    def GetPath(self, root, path):
        if root.left is None and root.right is None and sum(path) == self.expectNumber:
            self.path.append(path)
        if root.left:
            self.GetPath(root.left, path + [root.left.val])
        if root.right:
            self.GetPath(root.right, path + [root.right.val])


class Solution3:
    # 返回二维列表，内部每个列表表示找到的路径
    # 迭代
    def FindPath2(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        result = []
        stack = []
        stack.append((root, [root.val]))
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None and sum(path) == expectNumber:
                result.append(path)
            if node.right is not None:
                stack.append((node.right, path + [node.right.val]))
            if node.left is not None:
                stack.append((node.left, path + [node.left.val]))
        return result
