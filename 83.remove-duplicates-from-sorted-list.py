#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (41.92%)
# Total Accepted:    306.9K
# Total Submissions: 730.4K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        first = head
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return first

    def _deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 排序过的列表吖
        # 不用存下来
        # 。。。。
        if not head:
            return head
        dumped = []
        dumped.append(head.val)
        first = head
        while head.next:
            if head.next.val in dumped:
                if head.next.next:
                    head.next = head.next.next
                    continue
                else:
                    head.next = None
                    break
            else:
                dumped.append(head.next.val)
            head = head.next
        return first

