# coding=utf-8
#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (32.21%)
# Likes:    957
# Dislikes: 83
# Total Accepted:    194.4K
# Total Submissions: 575.4K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
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
    def _deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 先处理头部
        # 再处理其他
        # 或者先加一个哨兵节点
        # 然后开始
        if not head:
            return
        create = ListNode(0)
        create.next = head
        index = create
        root = head.next
        flag = False
        while root:
            if head.val == root.val:
                head.next = root.next
                root = root.next
                flag = True
            else:
                if flag:
                    create.next = root
                    head = root
                    root = root.next
                    flag = False
                else:
                    head = head.next
                    root = root.next
                    create = create.next
        if flag:
            create.next = root
        return index.next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 先处理头部
        # 再处理其他
        # 或者先加一个哨兵节点
        # 然后开始
        if not head:
            return
        create = ListNode(0)
        create.next = head
        index = create
        root = head.next
        while root:
            if head.val == root.val:

                while root and head.val == root.val:
                    root = root.next
                create.next = root
                head = root
                if root:
                    root = root.next
            else:
                create = create.next
                root = root.next
                head = head.next
        return index.next


# if __name__ == '__main__':
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(1)
#     head.next.next = ListNode(2)
#     head.next.next.next = ListNode(3)
#     head.next.next.next.next = ListNode(3)
#     print s.deleteDuplicates(head)
