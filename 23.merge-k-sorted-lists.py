# coding=utf-8
#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (33.02%)
# Likes:    2764
# Dislikes: 181
# Total Accepted:    429.4K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
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
    def _mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Time Limit
        lists = filter(None, lists)
        if not lists:
            return
        if not lists[0]:
            return
        guard = ListNode(1)
        current = guard
        while lists:
            min_index = -1
            for i in range(len(lists)):
                if lists[i] and (min_index < 0 or lists[min_index].val > lists[i].val):
                    min_index = i
            current.next = lists[min_index]
            current = current.next
            lists[min_index] = lists[min_index].next
            if not filter(None, lists):
                return guard.next

    def __mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # AC
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next

        guard = ListNode(1)
        current = guard
        for node in sorted(nodes):
            current.next = ListNode(node)
            current = current.next
        return guard.next

    def ___mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        from collections import defaultdict
        q = PriorityQueue()
        p = defaultdict(list)
        guard = ListNode(1)
        current = guard
        for i, l in enumerate(lists):
            if l:
                q.put(l.val)
                p[l.val].append(i)
        while True:
            if q.empty():
                return guard.next
            v = q.get()
            il = p[v][:]
            for i in il:
                current.next = lists[i]
                current = current.next
                lists[i] = lists[i].next
                p[v].remove(i)
                if lists[i]:
                    q.put(lists[i].val)
                    p[lists[i].val].append(i)

    def ____mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 类似于 merge-2-sorted-lists
        # 可以逐一合并
        if not lists:
            return
        return reduce(self.merge2Lists, lists)

    def merge2Lists(self, list1, list2):
        guard = ListNode(1)
        current = guard
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        if not list2:
            current.next = list1
        if not list1:
            current.next = list2
        return guard.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 类似于 merge-2-sorted-lists
        # 也可以两两合并
        if not lists:
            return
        while True:
            if len(lists) == 1:
                return lists[0]
            nodes = []
            for i in range(0, len(lists), 2):
                if i+1 >= len(lists):
                    nodes.append(lists[i])
                else:
                    nodes.append(self.merge2Lists(lists[i], lists[i+1]))
            lists = nodes


# if __name__ == '__main__':
#     s = Solution()
#     h1 = ListNode(1)
#     h1.next = ListNode(4)
#     h1.next.next = ListNode(5)
#     h2 = ListNode(1)
#     h2.next = ListNode(3)
#     h2.next.next = ListNode(4)
#     h3 = ListNode(2)
#     h3.next = ListNode(6)
#     print s.mergeKLists([h1, h2, h3])
