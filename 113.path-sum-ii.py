#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (39.46%)
# Likes:    892
# Dislikes: 33
# Total Accepted:    233.8K
# Total Submissions: 573.1K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \    / \
# 7    2  5   1
# 
# 
# Return:
# 
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    def _pathSum(self, root, um):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        paths = self.getPath(root, [[]])
        for path in paths:
            if sum(path) == um:
                res.append(path)
        return res

    def getPath(self, root, path):
        if not root:
            return path
        temp = []
        for p in path:
            temp.append(p+[root.val])
        if not root.left and not root.right:
            return temp
        if not root.left:
            return self.getPath(root.right, temp)
        if not root.right:
            return self.getPath(root.left, temp)
        return self.getPath(root.left, temp) + self.getPath(root.right, temp)

    def pathSum(self, root, um):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        return self.getPathWithUm(root, um, [])
        
    def getPathWithUm(self, root, um, path):
        if not root:
            return path
        temp = path[:]
        temp.append(root.val)
        if not root.left and not root.right:
            if sum(temp) == um:
                return [temp]
            return []
        if not root.left:
            return self.getPathWithUm(root.right, um, temp)
        if not root.right:
            return self.getPathWithUm(root.left, um, temp)
        return self.getPathWithUm(root.left, um, temp) + self.getPathWithUm(root.right, um, temp)


# if __name__ == "__main__":
#     s = Solution()
#     head = TreeNode(5)
#     head.left = TreeNode(4)
#     head.right = TreeNode(8)
#     head.left.left = TreeNode(11)
#     head.left.left.left = TreeNode(7)
#     head.left.left.right = TreeNode(2)
#     head.right.left = TreeNode(13)
#     head.right.right = TreeNode(4)
#     head.right.right.left = TreeNode(5)
#     head.right.right.right = TreeNode(1)
#     print s.pathSum(head, 22)
