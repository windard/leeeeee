# coding=utf-8
#
# @lc app=leetcode id=71 lang=python
#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (29.34%)
# Likes:    485
# Dislikes: 1305
# Total Accepted:    160.6K
# Total Submissions: 545.9K
# Testcase Example:  '"/home/"'
#
# Given an absolute path for a file (Unix-style), simplify it. Or in other
# words, convert it to the canonical path.
# 
# In a UNIX-style file system, a period . refers to the current directory.
# Furthermore, a double period .. moves the directory up a level. For more
# information, see: Absolute path vs relative path in Linux/Unix
# 
# Note that the returned canonical path must always begin with a slash /, and
# there must be only a single slash / between two directory names. The last
# directory name (if it exists) must not end with a trailing /. Also, the
# canonical path must be the shortest string representing the absolute
# path.
# 
# 
# 
# Example 1:
# 
# 
# Input: "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory
# name.
# 
# 
# Example 2:
# 
# 
# Input: "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the
# root level is the highest level you can go.
# 
# 
# Example 3:
# 
# 
# Input: "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced
# by a single one.
# 
# 
# Example 4:
# 
# 
# Input: "/a/./b/../../c/"
# Output: "/c"
# 
# 
# Example 5:
# 
# 
# Input: "/a/../../b/../c//.//"
# Output: "/c"
# 
# 
# Example 6:
# 
# 
# Input: "/a//b////c/d//././/.."
# Output: "/a/b/c"
# 
# 
#


class Solution(object):
    def _simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 不能出现三个点
        # ... 可能出现三个点，格式错误，直接返回
        # 不是的，三个点竟然算作正常路径
        # ..hidden 算作正常路径,牛逼吖
        # 字母只有小写字符
        # 也不一定，不管了，只要不是 . ..  都可以
        index = 0
        result = []
        while index < len(path):
            if path[index] != '/':
                t = ''
                while index < len(path) and path[index] != '/':
                    t += path[index]
                    index += 1
                if t == '.':
                    pass
                elif t == '..':
                    if result:
                        result.pop()
                else:
                    result.append(t)

            index += 1

        return '/' + '/'.join(result)

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        sl = path.split("/")
        result = []
        for s in sl:
            if s in ['', '.', '..']:
                if s == '..':
                    if result:
                        result.pop()
            else:
                result.append(s)
        return '/' + '/'.join(result)

#
# if __name__ == '__main__':
#     s = Solution()
#     print s.simplifyPath("/...")
#     print s.simplifyPath("/.../")
#     print s.simplifyPath("/..hidden")
#     print s.simplifyPath('/home/')
#     print s.simplifyPath("/../")
#     print s.simplifyPath("/home//foo/")
#     print s.simplifyPath("/a/./b/../../c/")
#     print s.simplifyPath("/a/../../b/../c//.//")
#     print s.simplifyPath("/a//b////c/d//././/..")
