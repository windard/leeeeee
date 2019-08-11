#
# @lc app=leetcode id=109 lang=python
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (39.60%)
# Likes:    1135
# Dislikes: 70
# Total Accepted:    186K
# Total Submissions: 444.6K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # link to list
        array_list = []
        while head:
            array_list.append(head.val)
            head = head.next
        if not array_list:
            return
        return self.convertListToBST(array_list)
    
    def convertListToBST(self, array_list):
        
        if not array_list:
            return
        mid = len(array_list) / 2
        root = TreeNode(array_list[mid])
        root.left = self.convertListToBST(array_list[:mid])
        root.right = self.convertListToBST(array_list[mid+1:])
        return root

    def __sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # Double point to get middle position
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            root = TreeNode(head.next.val)
            root.left = TreeNode(head.val)
            return root

        fast = lower = head
        while fast and fast.next and fast.next.next:
            lower = lower.next
            fast = fast.next.next
        root = TreeNode(lower.val)
        root.right = self.sortedListToBST(lower.next)
        first = head
        while head.next != lower:
            head = head.next
        head.next = None
        root.left = self.sortedListToBST(first)
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.head = head
        length = 0
        while head:
            head = head.next
            length += 1
        return self.createBST(0, length)
    
    def createBST(self, start, end):
        if start == end:
            return
        mid = (start + end) / 2
        left = self.createBST(start, mid)
        root = self.head
        if self.head.next:
            self.head = self.head.next
        root.left = left
        root.right = self.createBST(mid+1, end)
        return root


# if __name__ == "__main__":
#     s = Solution()
#     head = ListNode(-10)
#     head.next = ListNode(-3)
#     head.next.next = ListNode(0)
#     head.next.next.next = ListNode(5)
#     head.next.next.next.next = ListNode(9)
#     print s.sortedListToBST(head)
