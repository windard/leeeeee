#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (37.05%)
# Total Accepted:    292.8K
# Total Submissions: 787.1K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
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
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.result = []
        self._checkRootSum(root, 0, sum)
        return bool(self.result)

    def _checkRootSum(self, root, current, total):
        if not root:
            return False
        if current + root.val == total and not root.left and not root.right:
            self.result.append(root.val)
            return True
        else:
            if self._checkRootSum(root.left, current+root.val, total):
                self.result.append(root.left.val)
                return True
            elif self._checkRootSum(root.right, current+root.val, total):
                self.result.append(root.right.val)
                return True

        return False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.checkRootSum(root, 0, sum)

    def checkRootSum(self, root, current, total):
        if not root:
            return False
        if current + root.val == total and not root.left and not root.right:
            return True
        
        return self.checkRootSum(root.left, current+root.val, total) \
                or self.checkRootSum(root.right, current+root.val, total)

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    # root = TreeNode(-2)
    # root.right = TreeNode(-3)
    # print s.hasPathSum(root, 22)
