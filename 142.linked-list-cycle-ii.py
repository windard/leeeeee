# coding=utf-8
#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (30.93%)
# Likes:    1616
# Dislikes: 128
# Total Accepted:    231.7K
# Total Submissions: 701.4K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# 
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
# 
# Note: Do not modify the linked list.
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# 
# 
# 
# Follow-up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.


# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    # def __str__(self):
    #     return "<ListNode %s -> %s>" % (self.val, self.next)


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 先使用快慢指针找到环
        # 从快慢指针交点位置，快指针走 2k 步，慢指针走 k 步
        # 假设从环起点到交点位置为 m
        # 从交点位置和起点位置再次同时开始，走 k-m 步到达环起点

        fast = head and head.next and head.next.next
        if not fast:
            return fast

        slow = head and head.next
        while fast and fast != slow:
            fast = fast and fast.next and fast.next.next
            slow = slow and slow.next

        if not fast:
            return fast

        while head != slow:
            head = head.next
            slow = slow.next

        return head


# if __name__ == '__main__':
#     s = Solution()
#     head = ListNode(3)
#     head.next = ListNode(2)
#     head.next.next = ListNode(0)
#     head.next.next.next = ListNode(-4)
#     head.next.next.next.next = head.next
#     print s.detectCycle(head).val
