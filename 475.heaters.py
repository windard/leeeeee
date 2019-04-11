#
# @lc app=leetcode id=475 lang=python
#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Easy (31.13%)
# Total Accepted:    45.5K
# Total Submissions: 144.7K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! Your first job during the contest is to design a standard
# heater with fixed warm radius to warm all the houses.
# 
# Now, you are given positions of houses and heaters on a horizontal line, find
# out minimum radius of heaters so that all houses could be covered by those
# heaters.
# 
# So, your input will be the positions of houses and heaters seperately, and
# your expected output will be the minimum radius standard of heaters.
# 
# Note:
# 
# 
# Numbers of houses and heaters you are given are non-negative and will not
# exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not
# exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be
# warmed.
# All the heaters follow your radius standard and the warm radius will the
# same.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
#
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()

        max_length = 0
        min_heater = 0
        for i in houses:
            while min_heater < len(heaters) - 1:
                if abs(heaters[min_heater+1] - i) <= abs(heaters[min_heater] - i):
                    min_heater += 1
                else:
                    break
            if abs(heaters[min_heater] - i) > max_length:
                max_length = abs(heaters[min_heater] - i)
        return max_length

# if __name__ == "__main__":
    # s = Solution()
    # print s.findRadius([1,2,3],[2])
    # print s.findRadius([1,2,3,4],[1,4])
    # print s.findRadius([1, 1, 1, 1, 1, 1, 999, 999, 999, 999, 999], [499,500,501])
    # print s.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612])
    # print s.findRadius([1,2,3,4,5,6,7,8,9,10,2],[1,2,3,4,5,6,7,8,9,10,2])
