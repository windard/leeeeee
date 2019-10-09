# coding=utf-8


class Solution(object):
    def _minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        # brute
        max_count = float("inf")
        for chip in set(chips):
            count = sum(map(lambda x: 0 if not (x-chip) % 2 else 1, chips))
            max_count = min(count, max_count)
        return max_count

    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        odd = []
        even = []
        for chip in chips:
            if chip % 2:
                odd.append(chip)
            else:
                even.append(chip)
        return min(len(odd), len(even))


if __name__ == '__main__':
    s = Solution()
    print s.minCostToMoveChips([1,2,3])
    print s.minCostToMoveChips([2,2,2,3,3])
