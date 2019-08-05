#
# @lc app=leetcode id=538 lang=python
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (49.97%)
# Likes:    1274
# Dislikes: 84
# Total Accepted:    79.7K
# Total Submissions: 156.1K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
# 
# 
# Example:
# 
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
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
    def _convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # first inorder traversal
        # second add them
        # but Time Limit
        res = []
        nodes = []
        head = root

        while root or nodes:
            if not root:
                root = nodes.pop()
                res.append(root.val)
                root = root.right
            else:
                nodes.append(root)
                root = root.left
        self.adder(head, res)
        return head

    def adder(self, root, nodes):
        if not root:
            return
        root_val = root.val
        for node in nodes:
            if node > root_val:
                root.val += node

        self.adder(root.left, nodes)
        self.adder(root.right, nodes)

    def __convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # first inorder traversal
        # second add them
        # but Time Limit
        res = []
        nodes = []
        head = root

        while root or nodes:
            if not root:
                root = nodes.pop()
                res.append(root.val)
                root = root.right
            else:
                nodes.append(root)
                root = root.left
        
        temp_res = -float("inf")
        temp_sum = 0
        data = {}
        for r in res[::-1]:
            if r == temp_res:
                data[r] = data[temp_res]
            else:
                data[r] = temp_sum

            temp_res = r
            temp_sum += r
        self.helper(head, data)
        return head
    
    def helper(self, root, data):
        if not root:
            return
        root.val += data[root.val]
        self.helper(root.left, data)
        self.helper(root.right, data)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # reversed inorder traversal
        nodes = []
        current = 0
        head = root

        while root or nodes:
            if not root:
                root = nodes.pop()
                current, root.val = current + root.val, current + root.val
                root = root.left
            else:
                nodes.append(root)
                root = root.right

        return head

# if __name__ == "__main__":
#     s = Solution()
#     head = TreeNode(2)
#     head.left = TreeNode(1)
#     head.right = TreeNode(3)
#     s.convertBST(head)
