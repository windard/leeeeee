# coding=utf-8


class Solution(object):
    def _maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Limit
        max_length = 0
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
            if self.check_frequency(frequency):
                max_length = sum(frequency.values())

        return max_length

    def __maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 倒着找
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        for n in nums[::-1]:
            if self.check_frequency(frequency):
                return sum(frequency.values())
            frequency[n] -= 1
            if frequency[n] == 0:
                del frequency[n]
        return 0

    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        frequency = {}
        frequency_count = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
            if frequency[n] - 1 in frequency_count:
                frequency_count[frequency[n] - 1] -= 1
                if not frequency_count[frequency[n] - 1]:
                    del frequency_count[frequency[n] - 1]
            frequency_count[frequency[n]] = frequency_count.get(frequency[n], 0) + 1
            if self.check_frequency_and_count(frequency, frequency_count):
                max_length = sum(frequency.values())

        return max_length

    def check_frequency_and_count(self, frequency, frequency_count):
        # 判断 1,1,1,1
        if len(frequency) < 2:
            return True
        # 判断 1,2,3,4, 不能包括 1,1,2,2,3,3,4,4
        if len(frequency_count) < 2 and frequency_count.keys()[0] == 1:
            return True
        if len(frequency_count) == 2:
            # 判断 4,4,4,4,5,5,5,5,5
            if max(frequency_count) == min(frequency_count) + 1 and frequency_count[max(frequency_count)] == 1:
                return True
            # 判断 4,4,4,4,5,5,5,5,6
            if min(frequency_count) == 1 and frequency_count[min(frequency_count)] == 1:
                return True
        return False

    def check_frequency(self, frequency):
        # 特判 1,1,1,1
        if len(frequency) == 1:
            return True
        # 特判 1,2,3,4
        if all(map(lambda x: x == 1, frequency.values())):
            return True
        data = {}
        for f in frequency.values():
            data[f] = data.get(f, 0) + 1
        if len(data) > 2:
            return False
        # 特判 3,3,3,2,2
        if max(data) == min(data) + 1 and data[max(data)] == 1:
            return True
        # 特判 3,3,3,2,2,2,1
        if min(data) == 1 and data[min(data)] == 1:
            return True
        return False

    def check_minus(self, frequency):
        top = 0
        level = 0
        for f in frequency.values():
            if not level:
                level = f
            else:
                if f != level:
                    if not top:
                        if f == level + 1 or f == 1:
                            top = f
                        else:
                            return False
                    else:
                        return False
        return top and level


if __name__ == '__main__':
    s = Solution()
    # print s.maxEqualFreq([1,1])
    # print s.maxEqualFreq([1,2])
    print s.maxEqualFreq([2,2,1,1,5,3,3,5])
    print s.maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5])
    print s.maxEqualFreq([1,1,1,2,2,2])
    print s.maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6])
