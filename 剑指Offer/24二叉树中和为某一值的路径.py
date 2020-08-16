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


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    # 递归
    def FindPath(self, root, expectNumber):
        if root is None:
            return []
        result = []
        self.sums = expectNumber
        self.DFS(root, result, [root.val])
        return result

    def DFS(self, root, result, path):
        if root.left is None and root.right is None and sum(path) == self.sums:
            result.append(path)
        if root.left is not None:
            self.DFS(root.left, result, path + [root.left.val])
        if root.right is not None:
            self.DFS(root.right, result, path + [root.right.val])

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
