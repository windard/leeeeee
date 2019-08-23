#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (35.37%)
# Likes:    1312
# Dislikes: 266
# Total Accepted:    199K
# Total Submissions: 531.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head = self.reverseK(head, k)
        result = head
        index = 1
        while head:
            head = head.next
            index += 1
            if index == k:
                if head:
                    head.next = self.reverseK(head.next, k)
                    index = 1
                    head = head.next
        return result

    def reverseK(self, head, k):
        if not head or k < 2:
            return head
        index = 1
        root = head
        while index < k:
            root = root.next
            index += 1
            if not root:
                return head

        first = head.next
        last = root = head
        index = 1
        flag = False
        while index < k:
            root = first
            first = first.next
            root.next = last
            if not flag:
                last.next = None
                flag = True
            last = root
            index += 1
        head = root
        while root.next:
            root = root.next
        root.next = first
        return head

    def reverse(self, head, k):
        if not head or k < 2:
            return head
        index = 1
        root = head
        while index < k:
            root = root.next
            index += 1
            if not root:
                return head

        index = 0
        first = head
        last = root = None
        while index < k:
            root = first
            first = first.next
            root.next = last
            last = root
            index += 1
        head = root
        while root.next:
            root = root.next
        root.next = first
        return head


# if __name__ == '__main__':
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)
#     print s.reverseKGroup(head, 2)
#     print s.reverseK(head, 1)
