#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (45.43%)
# Total Accepted:    496.1K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
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
    def _mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Too Complex
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val <= l2.val:
            ll = ListNode(l1.val)
            if l1.next:
                l1 = l1.next
            else:
                l1 = None
        else:
            ll = ListNode(l2.val)
            if l2.next:
                l2 = l2.next
            else:
                l2 = None
        ls = ll
        while l1 or l2:
            if not l1:
                ll.next = l2
                break
            if not l2:
                ll.next = l1
                break
            if l1.val <= l2.val:
                ll.next = l1
                ll = l1
                if l1.next:
                    l1 = l1.next
                else:
                    l1 = None
            else:
                ll.next = l2
                ll = l2
                if l2.next:
                    l2 = l2.next
                else:
                    l2 = None

        return ls

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        guard = ListNode(1)
        current = guard
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        if not l2:
            current.next = l1
        if not l1:
            current.next = l2
        return guard.next


# if __name__ == '__main__':
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(4)
#     root = ListNode(1)
#     root.next = ListNode(3)
#     root.next.next = ListNode(4)
#     print s.mergeTwoLists(head, root)
