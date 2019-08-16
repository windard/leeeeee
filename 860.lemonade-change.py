# coding=utf-8
#
# @lc app=leetcode id=860 lang=python
#
# [860] Lemonade Change
#
# https://leetcode.com/problems/lemonade-change/description/
#
# algorithms
# Easy (50.28%)
# Likes:    318
# Dislikes: 60
# Total Accepted:    31.3K
# Total Submissions: 61.7K
# Testcase Example:  '[5,5,5,10,20]'
#
# At a lemonade stand, each lemonade costs $5. 
# 
# Customers are standing in a queue to buy from you, and order one at a time
# (in the order specified by bills).
# 
# Each customer will only buy one lemonade and pay with either a $5, $10, or
# $20 bill.  You must provide the correct change to each customer, so that the
# net transaction is that the customer pays $5.
# 
# Note that you don't have any change in hand at first.
# 
# Return true if and only if you can provide every customer with correct
# change.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.
# 
# 
# 
# Example 2:
# 
# 
# Input: [5,5,10]
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: [10,10]
# Output: false
# 
# 
# 
# Example 4:
# 
# 
# Input: [5,5,10,10,20]
# Output: false
# Explanation: 
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5
# bill.
# For the last customer, we can't give change of $15 back because we only have
# two $10 bills.
# Since not every customer received correct change, the answer is false.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= bills.length <= 10000
# bills[i] will be either 5, 10, or 20.
# 
# 
# 
# 
# 
# 
#


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # pay back with the transaction and carry with the minimal
        carry = {5: 0, 10: 0, 20: 0}
        amount = 5
        for bill in bills:
            if bill > amount:
                pay_back = bill - amount
                if pay_back == 5:
                    if carry[5] > 0:
                        carry[5] -= 1
                    else:
                        return False
                elif pay_back == 15:
                    if carry[5] > 0 and carry[10] > 0:
                        carry[5] -= 1
                        carry[10] -= 1
                    elif carry[5] > 2:
                        carry[5] -= 3
                    else:
                        return False
                else:
                    return False

            carry[bill] += 1
        return True


# if __name__ == '__main__':
#     s = Solution()
#     print s.lemonadeChange([5, 5, 10])
#     print s.lemonadeChange([10, 10])
#     print s.lemonadeChange([5, 5, 10, 10, 20])
#     print s.lemonadeChange([5, 5, 5, 10, 20])
