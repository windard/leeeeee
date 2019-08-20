# coding=utf-8
#
# @lc app=leetcode id=299 lang=python
#
# [299] Bulls and Cows
#
# https://leetcode.com/problems/bulls-and-cows/description/
#
# algorithms
# Easy (40.20%)
# Likes:    375
# Dislikes: 386
# Total Accepted:    105K
# Total Submissions: 261K
# Testcase Example:  '"1807"\n"7810"'
#
# You are playing the following Bulls and Cows game with your friend: You write
# down a number and ask your friend to guess what the number is. Each time your
# friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position
# (called "bulls") and how many digits match the secret number but locate in
# the wrong position (called "cows"). Your friend will use successive guesses
# and hints to eventually derive the secret number.
# 
# Write a function to return a hint according to the secret number and friend's
# guess, use A to indicate the bulls and B to indicate the cows. 
# 
# Please note that both secret number and friend's guess may contain duplicate
# digits.
# 
# Example 1:
# 
# 
# Input: secret = "1807", guess = "7810"
# 
# Output: "1A3B"
# 
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
# 
# Example 2:
# 
# 
# Input: secret = "1123", guess = "0111"
# 
# Output: "1A1B"
# 
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a
# cow.
# 
# Note: You may assume that the secret number and your friend's guess only
# contain digits, and their lengths are always equal.
#


class Solution(object):
    def _getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # 1155\n5505
        # 只要能用 set 做的，都能用 HashMap 来做
        index = 0
        bull = 0
        cow = 0
        secret = list(secret)
        guess = list(guess)
        length = len(guess)
        count = 0
        while count < length:
            if secret[index] == guess[index]:
                secret.pop(index)
                guess.pop(index)
                bull += 1
            else:
                index += 1
            count += 1

        for g in guess:
            if g in secret:
                cow += 1
                secret.remove(g)
        return '{}A{}B'.format(bull, cow)

    def __getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import Counter
        A = sum(map(lambda x: x[0] == x[1], zip(secret, guess)))
        B = sum((Counter(secret) & Counter(guess)).values()) - A
        return '{}A{}B'.format(A, B)

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        data = {}
        bull = 0
        cow = 0
        gu = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                data[secret[i]] = data.get(secret[i], 0) + 1
                gu.append(guess[i])

        for g in gu:
            if data.get(g, 0) > 0:
                data[g] -= 1
                cow += 1
        return '{}A{}B'.format(bull, cow)


# if __name__ == '__main__':
#     s = Solution()
#     print s.getHint("1155", "5505")
#     print s.getHint("1807", "7810")
#     print s.getHint("1123", "0111")
