# coding=utf-8
#
# @lc app=leetcode id=331 lang=python
#
# [331] Verify Preorder Serialization of a Binary Tree
#
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
#
# algorithms
# Medium (39.02%)
# Likes:    581
# Dislikes: 35
# Total Accepted:    63.2K
# Total Submissions: 161K
# Testcase Example:  '"9,3,4,#,#,1,#,#,2,#,6,#,#"'
#
# One way to serialize a binary tree is to use pre-order traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node,
# we record using a sentinel value such as #.
# 
# 
# ⁠    _9_
# ⁠   /   \
# ⁠  3     2
# ⁠ / \   / \
# ⁠4   1  #  6
# / \ / \   / \
# # # # #   # #
# 
# 
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
# 
# Given a string of comma separated values, verify whether it is a correct
# preorder traversal serialization of a binary tree. Find an algorithm without
# reconstructing the tree.
# 
# Each comma separated value in the string must be either an integer or a
# character '#' representing null pointer.
# 
# You may assume that the input format is always valid, for example it could
# never contain two consecutive commas such as "1,,3".
# 
# Example 1:
# 
# 
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# 
# Example 2:
# 
# 
# Input: "1,#"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: "9,#,#,1"
# Output: false
#

# @lc code=start


class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        # 前序遍历
        # 中左右
        node_list = preorder.split(",")
        # 回溯

        def backtrack():
            if node_list:
                if node_list[0] != '#':
                    root = TreeNode(node_list.pop(0))
                    root.left = backtrack()
                    root.right = backtrack()
                    return root
                else:
                    node_list.pop(0)
                    return None
            raise ValueError("Not Fill")

        try:
            backtrack()
        except ValueError:
            return False
        else:
            return not node_list


# @lc code=end

# if __name__ == '__main__':
#     s = Solution()
#     print s.isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#')
#     print s.isValidSerialization('1,#')
#     print s.isValidSerialization('9,#,#,1')
