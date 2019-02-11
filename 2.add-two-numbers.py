#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.41%)
# Total Accepted:    744.6K
# Total Submissions: 2.4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseNodes(self, l1):
        l2 = ListNode(l1.val)
        while l1.next:
            l1 = l1.next
            l3 = ListNode(l1.val)
            l3.next = l2
            l2 = l3
        return l2

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val
        left = val / 10
        right = val % 10
        lr = ListNode(right)
        while (l1.next or l2.next):
            val = left
            if l1.next:
                val += l1.next.val
                l1 = l1.next
            if l2.next:
                val += l2.next.val
                l2 = l2.next
            left = val / 10
            right = val % 10
            ln = ListNode(right)
            ln.next = lr
            lr = ln
        if left:
            ln = ListNode(left)
            ln.next = lr
            lr = ln
        return self.reverseNodes(lr)


