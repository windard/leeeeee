#
# @lc app=leetcode id=599 lang=python
#
# [599] Minimum Index Sum of Two Lists
#
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
#
# algorithms
# Easy (47.26%)
# Likes:    360
# Dislikes: 144
# Total Accepted:    57.5K
# Total Submissions: 119.9K
# Testcase Example:  '["Shogun","Tapioca Express","Burger King","KFC"]\n' +
#  '["Piatti","The Grill at Torrey Pines","Hungry Hunter ' +
#  'Steakhouse","Shogun"]'
#
# 
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both
# have a list of favorite restaurants represented by strings. 
# 
# 
# You need to help them find out their common interest with the least list
# index sum. If there is a choice tie between answers, output all of them with
# no order requirement. You could assume there always exists an answer.
# 
# 
# 
# Example 1:
# 
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# 
# 
# 
# Example 2:
# 
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is
# "Shogun" with index sum 1 (0+1).
# 
# 
# 
# 
# Note:
# 
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.
# 
# 
#
class Solution(object):
    def _findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        together = list(set(list1) & set(list2))
        min_index = float("inf")
        data = {}
        for to in together:
            index = list1.index(to) + list2.index(to)
            data[to] = index
        min_index = min(data.values())
        return [key for key, value in data.items() if value == min_index]

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        index = float("inf")
        d1 = dict(zip(list1, range(len(list1))))
        d2 = dict(zip(list2, range(len(list2))))
        for l in list1:
            i = d1.get(l) + d2.get(l, float("inf"))
            if i < index:
                index = i
                res = [l]
            elif i == index:
                res.append(l)
        return res

# if __name__ == "__main__":
    # s = Solution()
    # print s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"])
    # print s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"])
    # print s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"])
