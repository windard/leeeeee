# coding=utf-8
#
# @lc app=leetcode id=135 lang=python
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (28.99%)
# Likes:    585
# Dislikes: 129
# Total Accepted:    108.9K
# Total Submissions: 373.9K
# Testcase Example:  '[1,0,2]'
#
# There are N children standing in a line. Each child is assigned a rating
# value.
# 
# You are giving candies to these children subjected to the following
# requirements:
# 
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# 
# 
# What is the minimum candies you must give?
# 
# Example 1:
# 
# 
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# ⁠            The third child gets 1 candy because it satisfies the above two
# conditions.
# 
# 
#


class Solution(object):
    def _candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Same with @838
        # 相邻的孩子
        # 评分低的孩子，只有一个
        # 评分相同的孩子，也只有一个
        num = total = 0
        min_rating = min(ratings)
        min_index = ratings.index(min_rating)
        for i in range(min_index, -1, -1):
            if i == min_index:
                num = 1
            else:
                if ratings[i] > ratings[i+1]:
                    num += 1
                else:
                    num = 1
            total += num

        num = 1
        for i in range(min_index + 1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                num += 1
            else:
                num = 1
            total += num

        return total

    def __candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Too Complex
        # 遇到递增的，先从1开始加
        # 遇到递减的，先到最低点开始反向加
        if len(ratings) < 2:
            return len(ratings)
        num = 0
        total =[]
        # index = 1
        # while index < len(ratings):
        #     if ratings[index] > ratings[index-1]:
        #         num += 1
        #         total.append(num)
        #         index += 1
        #     else:
        #         for j in range(index+1, len(ratings)):
        #             if ratings[j] > ratings[j-1]:
        #                 button = j - 1
        #         else:
        #             button = len(ratings) - 1
        #         num = 1
        #         for j in range(button-1, index-1, -1):
        #             if ratings[j] > ratings[j+1]:
        #                 num += 1
        #             total.append(num)
        #         index = button + 1
        #         num = 0
        # if ratings[-1] > ratings[-2]:
        #     num += 1
        #     total.append(num)
        # else:
        #     total.append(1)
        # print ratings, total
        # return sum(total)

        # 这样算最后还要特殊处理最后一个节点
        index = 0
        while index < len(ratings) - 1:
            if ratings[index+1] > ratings[index]:
                num += 1
                total.append(num)
                index += 1
            else:
                for j in range(index+1, len(ratings)):
                    if ratings[j] > ratings[j-1]:
                        button = j - 1
                else:
                    button = len(ratings) - 1
                num = 1
                for j in range(button-1, index-1, -1):
                    if ratings[j] > ratings[j+1]:
                        num += 1
                    total.append(num)
                index = button + 1
                num = 0
        if ratings[-1] > ratings[-2]:
            num += 1
            total.append(num)
        else:
            total.append(1)
        print ratings, total
        return sum(total)

    def ___candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # 先算递增
        # 把递增都算完
        # 不行，山顶不能先定调，需要两边协商
        num = 0
        total = []
        index = 0
        if len(ratings) < 2:
            return len(ratings)
        while index < len(ratings) - 1:
            if ratings[index+1] > ratings[index]:
                num += 1
                total.append(num)
                index += 1
            else:
                if num:
                    num += 1
                    total.append(num)
                    index += 1

                for j in range(index, len(ratings)-1):
                    if ratings[j] < ratings[j+1]:
                        button = j
                        break
                else:
                    button = len(ratings) - 1

                num = 1
                for j in range(button-1, index-1, -1):
                    if ratings[j] > ratings[j+1]:
                        num += 1
                    else:
                        num = 1
                    total.append(num)

                index = button
                num = 0

        if ratings[-1] > ratings[-2]:
            num += 1
            total.append(num)
        else:
            total.append(1)

        print ratings, total
        return sum(total)

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # 先算递增
        # 把递增都算完
        # 不行，山顶不能先定调，需要两边协商
        num = 0
        total = []
        index = 0
        if len(ratings) < 2:
            return len(ratings)
        while index < len(ratings) - 1:
            if ratings[index+1] > ratings[index]:
                num += 1
                total.append(num)
                index += 1
            else:

                for j in range(index+1, len(ratings)-1):
                    if ratings[j] < ratings[j+1]:
                        button = j
                        break
                else:
                    button = len(ratings) - 1

                num = 1
                current = [1]
                for j in range(button-1, index, -1):
                    if ratings[j] > ratings[j+1]:
                        num += 1
                    else:
                        num = 1
                    current.append(num)
                up = down = 1
                if current:
                    if ratings[index] > ratings[index+1]:
                        down = current[-1]+1
                if total:
                    up = total[-1]+1
                current.append(max(up, down))
                # 开始计算山顶
                total.extend(current[::-1])

                index = button + 1
                num = 1

        if ratings[-1] > ratings[-2]:
            num += 1
            total.append(num)

        # print ratings, total
        return sum(total)


# if __name__ == '__main__':
#     s = Solution()
#     print s.candy([1,6,10,8,7,3,2])
#     print s.candy([1,3,2,2,1])
#     print s.candy([1,0,2])
#     print s.candy([1,2,2])
#     print s.candy([1,1,1,1])
#     print s.candy([11,1,5,26,2])
