#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (35.28%)
# Likes:    829
# Dislikes: 49
# Total Accepted:    226.7K
# Total Submissions: 632.9K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        first = head
        answer = first
        if not first:
            return   
        head = head.next     
        while head:
            if head.val == val:
                first.next = head.next
            else:
                first = first.next
            head = head.next
        return answer
