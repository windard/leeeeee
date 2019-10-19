# coding=utf-8
#
# @lc app=leetcode id=337 lang=python
#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (48.64%)
# Likes:    1825
# Dislikes: 38
# Total Accepted:    119.6K
# Total Submissions: 243.8K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house
# has one and only one parent house. After a tour, the smart thief realized
# that "all houses in this place forms a binary tree". It will automatically
# contact the police if two directly-linked houses were broken into on the same
# night.
# 
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [3,2,3,null,3,null,1]
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# Example 2:
# 
# 
# Input: [3,4,5,1,3,null,1]
# 
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 先层次遍历求和
        # 再和顺序打劫一样
        # Wrong Answer
        # 左子树和右子树，可以分开求层
        if not root:
            return 0
        with_index = without_index = 0
        stack = [[root]]
        while stack:
            level = stack.pop()
            current = []
            count = 0
            for root in level:
                count += root.val
                if root.left:
                    current.append(root.left)
                if root.right:
                    current.append(root.right)
            if current:
                stack.append(current)
            with_index, without_index = without_index + count, max(without_index, with_index)
        return max(with_index, without_index)

    def __rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        # 递归
        def calc(head):
            if not head:
                return 0, 0
            elif not head.left and not head.right:
                return head.val, 0
            elif not head.left:
                right_val = calc(head.right)
                return head.val+right_val[1], max(right_val[0], right_val[1])
            elif not head.right:
                left_val = calc(head.left)
                return head.val+left_val[1], max(left_val[0], left_val[1])
            else:
                right_val = calc(head.right)
                left_val = calc(head.left)
                return head.val+left_val[1]+right_val[1], max(left_val[0]+right_val[0],
                                                              left_val[1]+right_val[0],
                                                              left_val[0]+right_val[1],
                                                              left_val[1]+right_val[1])

        left_with_root, left_without_root = calc(root.left)
        right_with_root, right_without_root = calc(root.right)
        return max(left_with_root+right_with_root,
                   left_without_root+right_without_root+root.val,
                   left_without_root+right_with_root,
                   left_with_root+right_without_root)

    def ___rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # better recursion
        # but Time Limit
        if not root:
            return 0

        left_val = self.rob(root.left) if root.left else 0
        right_val = self.rob(root.right) if root.right else 0

        left_left_val = self.rob(root.left.left) if root.left and root.left.left else 0
        left_right_val = self.rob(root.left.right) if root.left and root.left.right else 0

        right_left_val = self.rob(root.right.left) if root.right and root.right.left else 0
        right_right_val = self.rob(root.right.right) if root.right and root.right.right else 0

        return max(root.val + left_left_val + left_right_val + right_left_val + right_right_val,
                   left_val + right_val)

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dp
        # 思路是和我的一样的，但是代码是如此的漂亮
        def calc(head):
            if not head:
                return [0, 0]
            left = calc(head.left)
            right = calc(head.right)

            return [head.val+left[1]+right[1], max(left)+max(right)]
        return max(calc(root))
# @lc code=end


# if __name__ == '__main__':
#     s = Solution()
#     root = TreeNode(3)
#     root.left = TreeNode(4)
#     root.right = TreeNode(5)
#     root.left.left = TreeNode(1)
#     root.left.right = TreeNode(3)
#     root.right.right = TreeNode(1)
#     print s.rob(root)
