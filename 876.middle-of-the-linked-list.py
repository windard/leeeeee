# coding=utf-8
#
# @lc app=leetcode id=876 lang=python
#
# [876] Middle of the Linked List
#
# https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (64.97%)
# Likes:    593
# Dislikes: 42
# Total Accepted:    76.4K
# Total Submissions: 117.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a non-empty, singly linked list with head node head, return a middle
# node of linked list.
# 
# If there are two middle nodes, return the second middle node.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is
# [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next
# = NULL.
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second
# one.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given list will be between 1 and 100.
# 
# 
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
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        elif not head.next:
            return head
        fast = low = head
        while fast:
            if fast and fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
            low = low.next
        return low if not fast.next else low.next


# if __name__ == '__main__':
#     s = Solution()
#     print s.middleNode(None)
#     head = ListNode(1)
#     print s.middleNode(head)
#     head.next = ListNode(2)
#     print s.middleNode(head)
#     head.next.next = ListNode(3)
#     print s.middleNode(head)
#     head.next.next.next = ListNode(4)
#     print s.middleNode(head)
#     head.next.next.next.next = ListNode(5)
#     print s.middleNode(head)
