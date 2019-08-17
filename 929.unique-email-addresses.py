# coding=utf-8
#
# @lc app=leetcode id=929 lang=python
#
# [929] Unique Email Addresses
#
# https://leetcode.com/problems/unique-email-addresses/description/
#
# algorithms
# Easy (69.44%)
# Likes:    541
# Dislikes: 146
# Total Accepted:    138.2K
# Total Submissions: 199.1K
# Testcase Example:  '["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]'
#
# Every email consists of a local name and a domain name, separated by the @
# sign.
# 
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com
# is the domain name.
# 
# Besides lowercase letters, these emails may contain '.'s or '+'s.
# 
# If you add periods ('.') between some characters in the local name part of an
# email address, mail sent there will be forwarded to the same address without
# dots in the local name.  For example, "alice.z@leetcode.com" and
# "alicez@leetcode.com" forward to the same email address.  (Note that this
# rule does not apply for domain names.)
# 
# If you add a plus ('+') in the local name, everything after the first plus
# sign will be ignored. This allows certain emails to be filtered, for example
# m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does
# not apply for domain names.)
# 
# It is possible to use both of these rules at the same time.
# 
# Given a list of emails, we send one email to each address in the list.  How
# many different addresses actually receive mails? 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input:
# ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually
# receive mails
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= emails[i].length <= 100
# 1 <= emails.length <= 100
# Each emails[i] contains exactly one '@' character.
# All local and domain names are non-empty.
# Local names do not start with a '+' character.
# 
# 
# 
#
import re


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def delete_domain(email):
            return email.split("@")[0]

        def carry_domain(email):
            return email.split("@")[1]

        def delete_add(email):
            return email.split("+")[0]

        def delete_dot(email):
            return re.sub(r'\.', r'', email)

        def assembly_email(group):
            return '{}@{}'.format(*group)

        domains = map(carry_domain, emails)
        emails = map(delete_domain, emails)
        emails = map(delete_add, emails)
        emails = map(delete_dot, emails)
        emails = map(assembly_email, zip(emails, domains))
        return len(set(emails))


# if __name__ == '__main__':
#     s = Solution()
#     print s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
