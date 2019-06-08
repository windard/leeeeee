#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (32.34%)
# Total Accepted:    290.1K
# Total Submissions: 875.1K
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,0,1,8,4,5]\n2\n3'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
# 
# For example, the following two linked lists:
# 
# 
# begin to intersect at node c1.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not
# be 0 if the two lists intersect). From the head of A, it reads as
# [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes
# before the intersected node in A; There are 3 nodes before the intersected
# node in B.
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not
# be 0 if the two lists intersect). From the head of A, it reads as
# [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes
# before the intersected node in A; There are 1 node before the intersected
# node in B.
# 
# 
# 
# 
# Example 3:
# 
# 
# 
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of
# B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must
# be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
# 
# 
# 
# 
# Notes:
# 
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns.
# You may assume there are no cycles anywhere in the entire linked
# structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def _getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodes = set()
        while headA:
            nodes.add(id(headA))
            headA = headA.next
        while headB:
            if id(headB) in nodes:
                return headB
            headB = headB.next
        return None

    def __getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Most Easy Way
        i = 0
        sa = headA
        while headA:
            i += 1
            headA = headA.next
        j = 0
        sb = headB
        while headB:
            j += 1
            headB = headB.next
        if i > j:
            for _ in range(i-j):
                sa = sa.next
        elif i < j:
            for _ in range(j-i):
                sb = sb.next
        while sa and sb:
            if id(sa) == id(sb):
                return sa
            sa = sa.next
            sb = sb.next

    def ___getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        sa = headA
        sb = headB
        while sa or sb:
            if id(sa) == id(sb):
                return sa
            sa = sa.next if sa else headB
            sb = sb.next if sb else headA


    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Most Beautify way
        sa = headA
        sb = headB
        while sa != sb:
            sa = sa.next if sa else headB
            sb = sb.next if sb else headA
        return sa