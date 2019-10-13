# coding=utf-8
#
# @lc app=leetcode id=911 lang=python
#
# [911] Online Election
#
# https://leetcode.com/problems/online-election/description/
#
# algorithms
# Medium (44.36%)
# Likes:    207
# Dislikes: 147
# Total Accepted:    14.4K
# Total Submissions: 30.2K
# Testcase Example:  '["TopVotedCandidate","q","q","q","q","q","q"]\n' +
# '[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]'
#
# In an election, the i-th vote was cast for persons[i] at time times[i].
# 
# Now, we would like to implement the following query function:
# TopVotedCandidate.q(int t) will return the number of the person that was
# leading the election at time t.  
# 
# Votes cast at time t will count towards our query.  In the case of a tie, the
# most recent vote (among tied candidates) wins.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["TopVotedCandidate","q","q","q","q","q","q"],
# [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# Output: [null,0,1,1,0,0,1]
# Explanation: 
# At time 3, the votes are [0], and 0 is leading.
# At time 12, the votes are [0,1,1], and 1 is leading.
# At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the
# most recent vote.)
# This continues for 3 more queries at time 15, 24, and 8.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= persons.length = times.length <= 5000
# 0 <= persons[i] <= persons.length
# times is a strictly increasing array with all elements in [0, 10^9].
# TopVotedCandidate.q is called at most 10000 times per test case.
# TopVotedCandidate.q(int t) is always called with t >= times[0].
# 
# 
# 
#

from collections import defaultdict


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        # 实现一个时序数据库
        # times 是严格递增
        # 但是 q 不是严格递增的
        self.persons = persons
        self.times = times
        self.status = []
        self.data = {}
        self.vote = defaultdict(list)
        for person in self.persons:
            self.data[person] = self.data.get(person, 0) + 1
            if self.data[person] - 1 in self.vote and person in self.vote[self.data[person] - 1]:
                self.vote[self.data[person] - 1].remove(person)
            self.vote[self.data[person]].append(person)
            self.status.append(self.vote[max(self.vote)][-1])

    def qq(self, t):
        """
        :type t: int
        :rtype: int
        """
        # Time Limit
        for index, time in enumerate(self.times):
            if time > t:
                return self.status[index-1]
            elif time == t:
                return self.status[index]
        return self.status[-1]

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        # 用二分去查
        if t <= self.times[0]:
            return self.status[0]
        if t >= self.times[-1]:
            return self.status[-1]
        start = 0
        end = len(self.times) - 1
        while start <= end:
            mid = (start + end) / 2
            if self.times[mid] > t:
                if self.times[mid-1] < t:
                    return self.status[mid-1]
                end = mid - 1
            elif self.times[mid] == t:
                return self.status[mid]
            else:
                if self.times[mid+1] > t:
                    return self.status[mid]
                start = mid + 1


# Your TopVotedCandidate object will be instantiated and called as such:

# if __name__ == '__main__':
#     # obj = TopVotedCandidate([0,1,1,0,0,1,0], [0,5,10,15,20,25,30])
#     # print obj.q(3)
#     # print obj.q(12)
#     # print obj.q(25)
#     # print obj.q(15)
#     # print obj.q(24)
#     # print obj.q(8)
#
#     tv = TopVotedCandidate([0,1,0,1,1], [24,29,31,76,81])
#     # print tv.q(28)
#     # print tv.q(24)
#     print tv.q(29)
#     print tv.q(77)
#     print tv.q(30)
#     print tv.q(25)
#     print tv.q(76)
#     print tv.q(75)
#     print tv.q(81)
#     print tv.q(80)

