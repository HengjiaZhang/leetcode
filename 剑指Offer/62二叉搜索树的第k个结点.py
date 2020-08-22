"""
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如：（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution2:
    # 递归
    # 返回对应节点TreeNode
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root] + self.inorderTraversal(root.right)

    def midnode(self, root):
        if not root:
            return None
        self.midnode(root.left)
        result.append(root)
        self.midnode(root.right)

    def KthNode(self, pRoot, k):
        # write code here
        # global result
        # result=[]
        # self.midnode(pRoot)
        result = self.inorderTraversal(pRoot)
        if k <= 0 or len(result) < k:
            return None
        else:
            return result[k - 1]

    def KthNode2(self, pRoot, k):
        # write code here
        global result
        result = []
        self.midnode(pRoot)
        # result = self.inorderTraversal(pRoot)
        if k <= 0 or len(result) < k:
            return None
        else:
            return result[k - 1]


class Solution:
    # 循环
    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return None
        stack = []
        cur = pRoot
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if k == 1:
                    return cur
                else:
                    k -= 1
                cur = cur.right