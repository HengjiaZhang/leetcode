"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），
请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""


# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    """
    解题思路：
    1、遍历链表，复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
    2、重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next;
    3、拆分链表，将链表拆分为原链表和复制后的链表
    """

    def Clone(self, pHead):
        if not pHead:
            return pHead
        # 1、复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
        currentNode = pHead
        while currentNode:
            cloneNode = RandomListNode(currentNode.label)
            cloneNode.next = currentNode.next
            currentNode.next = cloneNode
            currentNode = cloneNode.next
        # 2、重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next
        currentNode = pHead
        while currentNode:
            currentNode.next.random = currentNode.random.next if currentNode.random else None
            currentNode = currentNode.next.next
        # 3、拆分链表，将链表拆分为原链表和复制后的链表
        old = pHead
        new = pHead.next
        pCloneHead = pHead.next
        while old:
            old.next = old.next.next
            new.next = new.next.next if new.next else None
            old = old.next
            new = new.next
        return pCloneHead

