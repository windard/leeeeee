# coding=utf-8
#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (36.71%)
# Likes:    2045
# Dislikes: 95
# Total Accepted:    242.3K
# Total Submissions: 624.6K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#


class Solution(object):
    def _canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 不能用广度，应该用深度优先
        from collections import defaultdict
        lessons = defaultdict(list)
        for require in prerequisites:
            lessons[require[0]].append(require[1])
        for require in prerequisites:
            ns = lessons.get(require[0])
            has_learned = set([require[0]])
            while ns:
                new_s = []
                for n in ns:
                    if n in has_learned:
                        return False
                    else:
                        has_learned.add(n)
                        new_s.extend(lessons.get(n, []))
                ns = new_s
        return True

    def __canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Not Best
        from collections import defaultdict
        lessons = defaultdict(list)
        for require in prerequisites:
            lessons[require[0]].append(require[1])
        has_checked = dict()
        for require in prerequisites:
            if not self.cache_check_dfs(
                    lessons, set(), require[0], has_checked):
                return False
        return True

    def check_dfs(self, lessons, has_learned, target):
        # Time Limit
        for l in lessons.get(target, []):
            if l in has_learned:
                return False
            else:
                if not self.check_dfs(lessons, has_learned.union({target}), l):
                    return False
        return True

    def cache_check_dfs(self, lessons, has_learned, target, has_checked):
        if target in has_checked:
            return has_checked[target]
        else:
            for l in lessons.get(target, []):
                if l in has_learned:
                    has_checked[target] = False
                    return False
                else:
                    if not self.cache_check_dfs(lessons,
                                                has_learned.union({target}),
                                                l, has_checked):
                        has_checked[target] = False
                        return False
            has_checked[target] = True
            return True

    def ___canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # One Complex Solution
        # 核心是删除没有前置节点的点
        income = [0] * numCourses
        outcome = [[] for _ in range(numCourses)]

        for inc, out in prerequisites:
            income[inc] += 1
            outcome[out].append(inc)

        isolated = []
        for index, inc in enumerate(income):
            if not inc:
                isolated.append(index)

        while isolated:
            point = isolated.pop()
            numCourses -= 1
            for inc in outcome[point]:
                income[inc] -= 1
                if not income[inc]:
                    isolated.append(inc)

        return not numCourses

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Elegant DFS
        # 回溯

        def dfs(n):
            if points[n] == 1:
                return True
            elif points[n] == -1:
                return False
            points[n] = -1
            for ns in sources[n]:
                if not dfs(ns):
                    return False
            points[n] = 1
            return True

        points = [0] * numCourses
        sources = [[] for _ in range(numCourses)]

        for inc, out in prerequisites:
            sources[out].append(inc)

        for nc in range(numCourses):
            if not dfs(nc):
                return False
        return True


# if __name__ == '__main__':
#     s = Solution()
#     print s.canFinish(2, [[1, 0]])
#     print s.canFinish(2, [[1, 0], [0, 1]])
#     print s.canFinish(3, [[0,1],[0,2],[1,2]])
