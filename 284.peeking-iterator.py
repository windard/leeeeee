#
# @lc app=leetcode id=284 lang=python
#
# [284] Peeking Iterator
#
# https://leetcode.com/problems/peeking-iterator/description/
#
# algorithms
# Medium (39.46%)
# Likes:    308
# Dislikes: 211
# Total Accepted:    79.3K
# Total Submissions: 191.3K
# Testcase Example:  '["PeekingIterator","next","peek","next","next","hasNext"]\n' +
# '[[[1,2,3]],[],[],[],[],[]]'
#
# Given an Iterator class interface with methods: next() and hasNext(), design
# and implement a PeekingIterator that support the peek() operation -- it
# essentially peek() at the element that will be returned by the next call to
# next().
# 
# Example:
# 
# 
# Assume that the iterator is initialized to the beginning of the list:
# [1,2,3].
# 
# Call next() gets you 1, the first element in the list.
# Now you call peek() and it returns 2, the next element. Calling next() after
# that still return 2. 
# You call next() the final time and it returns 3, the last element. 
# Calling hasNext() after that should return false.
# 
# 
# Follow up: How would you extend your design to be generic and work with all
# types, not just integer?
# 
#
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


# class MyPeekingIterator(object):
#     def __init__(self, iterator):
#         """
#         Initialize your data structure here.
#         :type iterator: Iterator
#         """
#         self.iterator = iterator

#     def peek(self):
#         """
#         Returns the next element in the iteration without advancing the iterator.
#         :rtype: int
#         """
#         from copy import deepcopy
#         i = deepcopy(self.iterator)
#         return i.next()
        
#     def next(self):
#         """
#         :rtype: int
#         """
#         return self.iterator.next()

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return self.iterator.hasNext()


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.has_next = self.iterator.hasNext()
        if self.has_next:
            self.value = self.iterator.next()
        else:
            self.value = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.value

    def next(self):
        """
        :rtype: int
        """
        value = self.value
        if self.iterator.hasNext():
            self.value = self.iterator.next()
        else:
            self.has_next = False
            self.value = None
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

