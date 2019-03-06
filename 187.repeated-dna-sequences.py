#
# @lc app=leetcode id=187 lang=python
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (35.15%)
# Total Accepted:    118.1K
# Total Submissions: 334.3K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
#
# Example:
#
#
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
#
#
#

from collections import Counter

class Solution(object):
    def _findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # bit hash map
        
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        c = Counter()
        for key,value in enumerate(s):
            if key < 10:
                continue
            c[s[key-10:key]] += 1
        c[s[-10:]] += 1
        return [key for key,value in c.items() if key and value > 1]
