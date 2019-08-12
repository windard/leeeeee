#
# @lc app=leetcode id=292 lang=python
#
# [292] Nim Game
#
# https://leetcode.com/problems/nim-game/description/
#
# algorithms
# Easy (55.49%)
# Likes:    367
# Dislikes: 1145
# Total Accepted:    184.7K
# Total Submissions: 331.8K
# Testcase Example:  '4'
#
# You are playing the following Nim Game with your friend: There is a heap of
# stones on the table, each time one of you take turns to remove 1 to 3 stones.
# The one who removes the last stone will be the winner. You will take the
# first turn to remove the stones.
# 
# Both of you are very clever and have optimal strategies for the game. Write a
# function to determine whether you can win the game given the number of stones
# in the heap.
# 
# Example:
# 
# 
# Input: 4
# Output: false 
# Explanation: If there are 4 stones in the heap, then you will never win the
# game;
# No matter 1, 2, or 3 stones you remove, the last stone will always
# be 
# removed by your friend.
#


class Solution(object):
    def _canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Time Limit
        if n < 5:
            return False
        return any([not self.canWinNim(n-1),
                    not self.canWinNim(n-2),
                    not self.canWinNim(n-3)])

    def __canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # MemoryError
        # 1348820612
        if n < 5:
            return False
        win_list = [False]*n
        for i in range(4, n):
            win_list[i] = any([not win_list[i-1], not win_list[i-2], not win_list[i-3]])
        return win_list[-1]

    def ___canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Time Limit
        # 1348820612
        if n < 4:
            return True
        first, second, third = True, True, True
        index = 3
        while index < n:
            first, second, third = second, third, any([not first, not second, not third])
            index += 1
        return third

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

# if __name__ == "__main__":
#     s = Solution()
#     for i in range(100):
#         print i, s.canWinNim(i)
