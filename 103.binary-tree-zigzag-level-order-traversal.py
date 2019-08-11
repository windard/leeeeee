#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (40.48%)
# Likes:    957
# Dislikes: 59
# Total Accepted:    222.2K
# Total Submissions: 530.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        nodes = [[root]]
        result = []
        flag = True
        while nodes:
            level = []
            current = []
            roots = nodes.pop()
            for root in roots:
                if flag:
                    current.append(root.val)
                else:
                    current.insert(0, root.val)
                if root.left:
                    level.append(root.left)
                if root.right:
                    level.append(root.right)
            nodes.append(level)
            result.append(current)
            flag = not flag
            if not level:
                break
        return result


# if __name__ == "__main__":
#     s = Solution()
#     head = TreeNode(3)
#     head.left = TreeNode(9)
#     head.right = TreeNode(20)
#     head.right.left = TreeNode(15)
#     head.right.right = TreeNode(7)
#     print s.zigzagLevelOrder(head)
