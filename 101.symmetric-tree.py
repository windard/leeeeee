#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (42.73%)
# Total Accepted:    368.6K
# Total Submissions: 860K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # iteratively solution
        q = []
        if root:
            q.append(root)
        while q:
            i = len(q)
            while i:
                r = q.pop(0)
                if r:
                    q.append(r.left)
                    q.append(r.right)
                i -= 1
            if not self.checkSymmetricList(q):
                return False
        return True

    def checkSymmetricList(self, q):
        length = len(q)
        mid = length / 2
        for i in range(mid):
            if q[i] and q[length-1-i]:
                if q[i].val != q[length-1-i].val:
                    return False
            else:
                if q[i] != q[length-1-i]:
                    return False
        return True

    def _checkSymmetricList(self, q):
        length = len(q)
        mid = length / 2
        for i in range(mid):
            if q[i] and q[length-1-i]:
                if q[i].val == q[length-1-i].val:
                    continue
            elif not q[i] and not q[length-1-i]:
                continue
            return False
        return True

    def _isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # recursively solution
        if root:
            return self.checkSymmetric(root.left, root.right)
        return True

    def checkSymmetric(self, left, right):
        if left and right:
            if left.val == right.val:
                if self.checkSymmetric(left.left, right.right):
                    return self.checkSymmetric(left.right, right.left)
        elif not left and not right:
            return True
        return False

# if __name__ == "__main__":
#     s = Solution()
#     t = TreeNode(1)
#     t.left = TreeNode(2)
#     t.right = TreeNode(2)
#     t.left.left = TreeNode(3)
#     t.right.right = TreeNode(3)
#     t.left.right = TreeNode(4)
#     t.right.left = TreeNode(4)
#     print s.isSymmetric(t)
#     print t.left == t.right