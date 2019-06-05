#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (35.78%)
# Total Accepted:    385.9K
# Total Submissions: 1.1M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, determine if it has a cycle in it.
# 
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
# 
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
# 
# 
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# 
# 
# 
# 
# Follow up:
# 
# Can you solve it using O(1) (i.e. constant) memory?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def _hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = []
        while head:
            if id(head) in nodes:
                return True
            nodes.append(id(head))
            head = head.next
        return False

    def __hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        quick = head.next
        while True:
            if slow == quick:
                return True

            slow = slow and slow.next
            if not slow:
                return False
            quick = quick and quick.next and quick.next.next
            if not quick:
                return False
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val != 'windard':
                head.val = 'windard'
            else:
                return True
            head = head.next
        return False
