#
# @lc app=leetcode id=455 lang=python
#
# [455] Assign Cookies
#
# https://leetcode.com/problems/assign-cookies/description/
#
# algorithms
# Easy (48.06%)
# Total Accepted:    60.4K
# Total Submissions: 125.3K
# Testcase Example:  '[1,2,3]\n[1,1]'
#
# 
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie. Each child i has a greed
# factor gi, which is the minimum size of a cookie that the child will be
# content with; and each cookie j has a size sj. If sj >= gi, we can assign the
# cookie j to the child i, and the child i will be content. Your goal is to
# maximize the number of your content children and output the maximum number.
# 
# 
# Note:
# You may assume the greed factor is always positive. 
# You cannot assign more than one cookie to one child.
# 
# 
# Example 1:
# 
# Input: [1,2,3], [1,1]
# 
# Output: 1
# 
# Explanation: You have 3 children and 2 cookies. The greed factors of 3
# children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could
# only make the child whose greed factor is 1 content.
# You need to output 1.
# 
# 
# 
# Example 2:
# 
# Input: [1,2], [1,2,3]
# 
# Output: 2
# 
# Explanation: You have 2 children and 3 cookies. The greed factors of 2
# children are 1, 2. 
# You have 3 cookies and their sizes are big enough to gratify all of the
# children, 
# You need to output 2.
# 
# 
#
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i

    def _findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        l = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                l += 1
            j += 1
        return l

    def _findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        l = 0
        for i in g:
            while s:
                if s[0] >= i:
                    s.pop(0)
                    l += 1
                    break
                else:
                    s.pop(0)
            else:
                return l
        return l

# if __name__ == "__main__":
#     s = Solution()
#     print s.findContentChildren([1,2,3], [1,1])
#     print s.findContentChildren([10,9,8,7], [5,6,7,8])
