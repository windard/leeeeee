#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.00%)
# Likes:    1868
# Dislikes: 136
# Total Accepted:    403.2K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
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
    def _removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        faster = lower = head
        for _ in range(n):
            faster = faster.next
        
        if not faster:
            return head.next

        while faster:
            faster = faster.next
            if not faster:
                break
            lower = lower.next

        lower.next = lower.next.next
        return head

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # normal solution
        length = 0
        source = head
        while head:
            head = head.next
            length += 1

        if length <= n:
            return source.next

        head = source
        for _ in range(length - n - 1):
            head = head.next
        head.next = head.next.next
        return source

# if __name__ == "__main__":
#     head = ListNode(1)
#     head.next = ListNode(2)
#     s = Solution()
#     head = s.removeNthFromEnd(head, 1)
#     print head
