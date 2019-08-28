# coding=utf-8
#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (36.33%)
# Likes:    760
# Dislikes: 204
# Total Accepted:    173.7K
# Total Submissions: 456.2K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# 
# 
#
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "<ListNode %s -> %s>" % (self.val, self.next)


class Solution(object):
    def _partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 节点前移
        if not head:
            return head

        # 找到插入位置
        root = head
        last = None

        while root:
            if root.val >= x:
                break
            last = root
            root = root.next

        flag = True
        if not last:
            last = ListNode(1)
            last.next = root
            head = last
            flag = False

        # 开始插入
        if not root:
            return head
        fast = root.next
        while fast:
            if fast.val < x:
                root.next = fast.next
                last.next, fast.next = fast, last.next
                last = last.next
                fast = root.next
            else:
                root = root.next
                fast = fast.next

        return head if flag else head.next

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Double Point
        # 快慢指针
        # 快指针指向大于x的链表
        # 慢指针指向小于x的链表
        # 最后将两者相连
        fast = ListNode(0)
        root = fast
        lower = ListNode(0)
        index = lower

        while head:
            if head.val < x:
                lower.next = head
                lower = lower.next
            else:
                fast.next = head
                fast = fast.next
            head = head.next
        lower.next = root.next
        fast.next = None
        return index.next


# if __name__ == '__main__':
#     s = Solution()
#     head = ListNode(6)
#     head.next = ListNode(4)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(2)
#     head.next.next.next.next = ListNode(5)
#     head.next.next.next.next.next = ListNode(2)
#     print s.partition(head, 3)
