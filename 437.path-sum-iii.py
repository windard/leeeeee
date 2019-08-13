# coding=utf-8
#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (41.98%)
# Total Accepted:    99.6K
# Total Submissions: 235K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
# 
# 
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # Wrong Answer
        self.answer = 0
        self.checkSum(root, 0, sum)
        return self.answer
    
    def checkSum(self, root, current, total):
        if not root:
            return
        stat = current + root.val
        if stat == total:
            self.answer += 1
        else:
            self.checkSum(root.left, stat, total)
            self.checkSum(root.right, stat, total)
        self.checkSum(root.left, 0, total)
        self.checkSum(root.right, 0, total)

    def __pathSum(self, root, um):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # Time Limit
        self.count = 0
        path = self.get_path_sum(root, um)
        for p in path:
            if sum(p) == um:
                self.count += 1
        return self.count

    def get_path_sum(self, root, um):
        if not root:
            return []
        result = []
        path = self.get_path_sum(root.left, um) + self.get_path_sum(root.right, um)
        for p in path:
            if sum(p) == um:
                self.count += 1
        result.append([root.val])
        for p in path:
            result.append(p+[root.val])
        return result

    def get_path(self, root):
        if not root:
            return []
        path = self.get_path(root.left) + self.get_path(root.right)
        result = []
        self.path.extend(path)
        result.append([root.val])
        for p in path:
            result.append(p+[root.val])
        return result

    def ___pathSum(self, root, um):
        """
        :type root: TreeNode
        :type um: int
        :rtype: int
        """
        # Memory Limit
        self.path = []
        self.path.extend(self.get_path(root))
        # print self.path
        count = 0
        for p in self.path:
            if sum(p) == um:
                count += 1
        return count

    def pathSum(self, root, um):
        """
        :type root: TreeNode
        :type um: int
        :rtype: int
        """
        self.count = 0
        self.depth(root, um, [])
        return self.count

    def depth(self, root, um, nums):
        if not root:
            return
        result = []
        result.append(root.val)
        for num in nums:
            result.append(num+root.val)
        self.count += len(filter(lambda x: x == um, result))
        self.depth(root.left, um, result)
        self.depth(root.right, um, result)


# if __name__ == "__main__":
#     s = Solution()
    # head = TreeNode(1)
    # head.right = TreeNode(2)
    # head.right.right = TreeNode(3)
    # head.right.right.right = TreeNode(4)
    # head.right.right.right.right = TreeNode(5)
    # print s.pathSum(head, 5)

    # head = TreeNode(10)
    # head.left = TreeNode(5)
    # head.right = TreeNode(-3)
    # head.right.right = TreeNode(11)
    # head.left.left = TreeNode(3)
    # head.left.right = TreeNode(2)
    # head.left.right.right = TreeNode(1)
    # head.left.left.left = TreeNode(3)
    # head.left.left.right = TreeNode(-2)
    # print s.pathSum(head, 8)
    #
    # head = TreeNode(5)
    # head.left = TreeNode(4)
    # head.right = TreeNode(8)
    # head.left.left = TreeNode(11)
    # head.left.left.left = TreeNode(7)
    # head.left.left.right = TreeNode(2)
    # head.right.left = TreeNode(13)
    # head.right.right = TreeNode(4)
    # head.right.right.left = TreeNode(5)
    # head.right.right.right = TreeNode(1)
    # print s.pathSum(head, 22)

