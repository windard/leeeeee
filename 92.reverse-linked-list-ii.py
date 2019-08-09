# coding=utf-8
#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (34.07%)
# Likes:    1357
# Dislikes: 97
# Total Accepted:    206.5K
# Total Submissions: 579.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
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

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        index = 1
        prev = None
        root = head
        while index < m:
            prev = head
            head = head.next
            index += 1

        top = self.reverse(head, n - m)
        top.next = self.last

        if prev:
            prev.next = self.first
        else:
            root = self.first
        return root

    def reverse(self, head, n):
        if n < 0:
            self.last = head
            return None
        last = self.reverse(head.next, n - 1)
        if not last:
            self.first = head
            return head
        last.next = head
        return head

    def _reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 1->2->3->4->5->NULL
        # 2,4
        # 0,4
        # 0,8
        root = head
        prev = None

        index = 1
        while index < m:
            index += 1
            prev = head
            head = head.next

        top = None
        for _ in range(m, n+1):
            temp = head.next
            head.next = top
            top = head
            head = temp

        if prev:
            prev.next = top
        else:
            root = top

        while top.next:
            top = top.next
        top.next = head
        return root

# if __name__ == "__main__":
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)
    # print s.reverseBetween(head, 1, 4)
    # print s.reverseBetween(head, 2, 4)
