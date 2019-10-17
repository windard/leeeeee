# coding=utf-8
#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (33.68%)
# Likes:    1118
# Dislikes: 78
# Total Accepted:    164.2K
# Total Submissions: 458.3K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
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
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # 先找到入度为0的点，将其进行掉
        # 再删掉其出度，继续找入度为0的点
        # 再删掉其出度，以此类推，不断重复
        # from collections import defaultdict
        # in_course = defaultdict(list)
        # out_course = defaultdict(list)
        # for require in prerequisites:
        #     in_course[require[0]].append(require[1])
        #     out_course[require[1]].append(require[0])
        # 妈耶，我还以为提供的就是可用的
        # 没想到还要我来先判断数据能否满足条件
        in_course = {}
        out_course = {}
        for i in range(numCourses):
            in_course[i] = []
            out_course[i] = []
        for require in prerequisites:
            in_course[require[0]].append(require[1])
            out_course[require[1]].append(require[0])

        result = []
        for _ in range(numCourses):
            for course, point in in_course.items():
                if not point:
                    result.append(course)
                    for n in out_course[course]:
                        in_course[n].remove(course)
                    del in_course[course]
        return result if len(result) == numCourses else []


# if __name__ == '__main__':
#     s = Solution()
#     print s.findOrder(3, [[1,0],[1,2],[0,1]])
#     print s.findOrder(2, [[0,1]])
#     print s.findOrder(2, [[1,0]])
#     print s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
