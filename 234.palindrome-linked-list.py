#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (35.33%)
# Likes:    1557
# Dislikes: 231
# Total Accepted:    251.8K
# Total Submissions: 702.2K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "<ListNode %s -> %s>" % (self.val, self.next)


import copy


class Solution(object):
    def _isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        start = head
        length = 0
        while head:
            head = head.next
            length += 1
        half = length / 2
        head = start
        nums = []
        for _ in range(half):
            nums.append(head.val)
            head = head.next
        if length % 2 != 0:
            head = head.next
        for _ in range(half):
            if head.val != nums.pop():
                return False
            head = head.next
        return True

    def __isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nums = []
        start = head
        while head:
            nums.append(head.val)
            head = head.next
        while start:
            if nums.pop() != start.val:
                return False
            start = start.next
        return True

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 如果能反转链表
        # 还可以直接反转，直接对比
        # 或者使用快慢指针找到中点
        # 再反转，依次对比
        # 不能用 deepcopy，对长链表深度超限
        # 但是还是需要新建对象
        # 不能使用指针引用
        # start = copy.deepcopy(head)
        start = head
        # print start, head, id(start), id(head)

        # start reverse
        head = self.reverse(head)
        # prev = None
        # current = head
        # while head:
        #     head = head.next
        #     current.next = prev
        #     prev = current
        #     current = head
        # head = prev
        # end reverse
        # 原链表位置已经改变
        # 结构迁移，逆序链表需要再开空间
        # 而非在原链表上改变
        # print start, head, id(start), id(head)
        while start:
            if start.val != head.val:
                return False
            start = start.next
            head = head.next
        return True

    def reverse(self, head):
        prev = None
        current = ListNode(head.val) if head else None
        while head:
            head = head.next
            current.next = prev
            prev = current
            current = ListNode(head.val)  if head else None
        return prev


    def _reverse(self, head):
        prev = None
        current = head
        while head:
            head = head.next
            current.next = prev
            prev = current
            current = head
        return prev

# if __name__ == "__main__":
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(1)
#     head.next.next = ListNode(2)
#     head.next.next.next = ListNode(1)
#     print s.isPalindrome(head)
