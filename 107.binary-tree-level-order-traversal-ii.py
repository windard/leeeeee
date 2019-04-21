#
# @lc app=leetcode id=107 lang=python
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (45.67%)
# Total Accepted:    213.2K
# Total Submissions: 464.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
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
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
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
    def _levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # iteration
        q = []
        if root:
            q.append(root)
        res = []
        while q:
            l = []
            for _ in range(len(q)):
                r = q.pop(0)
                l.append(r.val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            res.append(l)
        res.reverse()
        return res
        # return list(reversed(res))
    
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # recursion
        return reversed(self.leaveOfRoot(root, 0, []))
    
    def leaveOfRoot(self, root, index, res):
        if not root:
            return res
        if len(res) > index:
            res[index].append(root.val)
        else:
            res.append([root.val])
        res = self.leaveOfRoot(root.left, index+1, res)
        res = self.leaveOfRoot(root.right, index+1, res)
        return res

# if __name__ == "__main__":
#     s = Solution()
#     r = TreeNode(3)
#     r.left = TreeNode(9)
#     r.right = TreeNode(20)
#     r.right.left = TreeNode(15)
#     r.right.right = TreeNode(7)
#     print s.levelOrderBottom(r)