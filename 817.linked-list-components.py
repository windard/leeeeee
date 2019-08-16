# coding=utf-8
#
# @lc app=leetcode id=817 lang=python
#
# [817] Linked List Components
#
# https://leetcode.com/problems/linked-list-components/description/
#
# algorithms
# Medium (53.80%)
# Likes:    237
# Dislikes: 595
# Total Accepted:    27.8K
# Total Submissions: 50.5K
# Testcase Example:  '[0,1,2,3]\n[0,1,3]'
#
# We are given head, the head node of a linked list containing unique integer
# values.
# 
# We are also given the list G, a subset of the values in the linked list.
# 
# Return the number of connected components in G, where two values are
# connected if they appear consecutively in the linked list.
# 
# Example 1:
# 
# 
# Input: 
# head: 0->1->2->3
# G = [0, 1, 3]
# Output: 2
# Explanation: 
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
# 
# 
# Example 2:
# 
# 
# Input: 
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# Output: 2
# Explanation: 
# 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the
# two connected components.
# 
# 
# Note: 
# 
# 
# If N is the length of the linked list given by head, 1 <= N <= 10000.
# The value of each node in the linked list will be in the range [0, N -
# 1].
# 1 <= G.length <= 10000.
# G is a subset of all values in the linked list.
# 
# 
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def _numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        # Wrong Answer
        count = 1
        setG = set(G)
        while head:
            if head.val not in setG:
                count += 1
            head = head.next
        return count

    def __numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        groups = []
        setG = set(G)
        group = []
        while head:
            if head.val in setG:
                group.append(head.val)
            else:
                if group:
                    groups.append(group)
                    group = []
            head = head.next
        if group:
            groups.append(group)
        return len(groups)

    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        count = 0
        setG = set(G)
        while head:
            if head.val in setG:
                while head and head.val in setG:
                    head = head.next
                count += 1
            else:
                head = head.next
        return count

# if __name__ == "__main__":
#     s = Solution()
#     head = ListNode(0)
#     head.next = ListNode(1)
#     head.next.next = ListNode(2)
#     print s.numComponents(head, [1, 0])

#     head = ListNode(0)
#     head.next = ListNode(1)
#     head.next.next = ListNode(2)
#     head.next.next.next = ListNode(3)
#     print s.numComponents(head, [0, 1, 3])
    
#     head = ListNode(0)
#     head.next = ListNode(1)
#     head.next.next = ListNode(2)
#     head.next.next.next = ListNode(3)
#     head.next.next.next.next = ListNode(4)
#     print s.numComponents(head, [0, 3, 1, 4])
