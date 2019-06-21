#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (43.22%)
# Likes:    1178
# Dislikes: 103
# Total Accepted:    322.5K
# Total Submissions: 716.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
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
    def _swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = source = head
        if head and head.next:
            head = self.swap(head)
            source = head
            last = head.next
            head = head.next.next

        while head and head.next:
            head = self.swap(head)
            last.next = head
            last = last.next.next
            head = head.next.next
        
        return source

    def swap(self, head):
        temp = head.next
        head.next = head.next.next
        temp.next = head
        return temp

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # recursion
        if head and head.next:
            temp = head.next
            resource = self.swapPairs(head.next.next)
            head.next = resource
            temp.next = head
            return temp
        else:
            if head:
                return head
            else:
                return

# if __name__ == "__main__":
#     s = Solution()
    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # print s.swapPairs(head)
