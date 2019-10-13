#
# @lc app=leetcode id=147 lang=python
#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (36.41%)
# Likes:    395
# Dislikes: 445
# Total Accepted:    156.3K
# Total Submissions: 410.9K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list using insertion sort.
# 
# 
# 
# 
# 
# A graphical example of insertion sort. The partial sorted list (black)
# initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and
# inserted in-place into the sorted list
# 
# 
# 
# 
# 
# Algorithm of Insertion Sort:
# 
# 
# Insertion sort iterates, consuming one input element each repetition, and
# growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it
# there.
# It repeats until no input elements remain.
# 
# 
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        guard = ListNode(-float("inf"))
        last = None
        while head:
            root = guard
            while root:
                if root.val < head.val:
                    last = root
                    root = root.next
                else:
                    break
            last.next = head
            head = head.next
            last.next.next = root
        return guard.next


# if __name__ == '__main__':
#     s = Solution()
#     head = ListNode(4)
#     head.next = ListNode(2)
#     head.next.next = ListNode(1)
#     head.next.next.next = ListNode(3)
#     print s.insertionSortList(head)
