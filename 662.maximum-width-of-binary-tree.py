# coding=utf-8
#
# @lc app=leetcode id=662 lang=python
#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (39.53%)
# Likes:    720
# Dislikes: 142
# Total Accepted:    37.8K
# Total Submissions: 95.8K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given a binary tree, write a function to get the maximum width of the given
# tree. The width of a tree is the maximum width among all levels. The binary
# tree has the same structure as a full binary tree, but some nodes are null.
# 
# The width of one level is defined as the length between the end-nodes (the
# leftmost and right most non-null nodes in the level, where the null nodes
# between the end-nodes are also counted into the length calculation.
# 
# Example 1:
# 
# 
# Input: 
# 
# ⁠          1
# ⁠        /   \
# ⁠       3     2
# ⁠      / \     \  
# ⁠     5   3     9 
# 
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4
# (5,3,null,9).
# 
# 
# Example 2:
# 
# 
# Input: 
# 
# ⁠         1
# ⁠        /  
# ⁠       3    
# ⁠      / \       
# ⁠     5   3     
# 
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2
# (5,3).
# 
# 
# Example 3:
# 
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2 
# ⁠      /        
# ⁠     5      
# 
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2
# (3,2).
# 
# 
# Example 4:
# 
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /     \  
# ⁠     5       9 
# ⁠    /         \
# ⁠   6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8
# (6,null,null,null,null,null,null,7).
# 
# 
# 
# 
# Note: Answer will in the range of 32-bit signed integer.
# 
#
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 同一深度的才算宽度
        # [2,1,4,3,null,5]
        # [1,1,1,1,null,null,1,1,null,null,1]
        # [1,3,2,5]
        # [1,3,2,5,3,null,9]
        self.max_width = 0
        self.getWidth(root)
        return self.max_width

    def getWidth(self, root):
        # 没明白它的宽度是怎么计算的
        if not root:
            return -1, -1

        ll, _ = self.getWidth(root.left)
        _, rr = self.getWidth(root.right)
        self.max_width = max(2**min(ll, rr), self.max_width)
        return ll+1, rr+1

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 同一深度即可
        # 无需最外扩散宽度
        # 宽度呈指数增长，而非线性增长
        # 用递归不好做，用循环吧

        root.val = 0
        max_count = 0
        stack = [[root]]
        while stack:
            level = stack.pop()
            max_count = max(level[-1].val - level[0].val + 1, max_count)
            current = []
            for node in level:
                if node.left:
                    node.left.val = 2 * node.val
                    current.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 1
                    current.append(node.right)
            if current:
                stack.append(current)
        return max_count


# if __name__ == '__main__':
#     s = Solution()
#     head = TreeNode(1)
#     head.left = TreeNode(2)
#     head.left.left = TreeNode(3)
#     head.left.left.left = TreeNode(4)
#     head.right = TreeNode(3)
#     head.right.right = TreeNode(4)
#     head.right.right.right = TreeNode(6)
#     print s.widthOfBinaryTree(head)
