#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (52.80%)
# Likes:    2333
# Dislikes: 63
# Total Accepted:    594.7K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
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
    def _reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        ahead = None
        if head.next:
            last = head
            head = head.next
            ahead = head.next
            head.next = last
            last.next = None
        while ahead:
            last = head
            head = ahead
            ahead = ahead.next
            head.next = last
        return head

    def __reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        ahead = head.next
        current = head
        current.next = None
        return self.reverse(current, ahead)

    def reverse(self, current, head):
        if not head:
            return current
        ahead = head.next
        head.next = current
        return self.reverse(head, ahead)

    def ___reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Amazing
        if not head:
            return
        if not head.next:
            return head
        answer = self.___reverseList(head.next)
        head.next.next = head
        head.next = None
        return answer

    def ____reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        if not head.next:
            return head
        last = head.next
        head.next = None
        while last:
            ahead = last.next
            last.next = head
            head = last
            last = ahead
        return head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        current = head
        while current:
            head = head.next
            current.next = previous
            previous = current
            current = head
        return previous

# if __name__ == "__main__":
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)
#     print s.reverseList(head)
