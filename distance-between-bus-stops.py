# coding=utf-8

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        start, destination = min(start, destination), max(start, destination)
        left = right = 0
        for i in range(start):
            right += distance[i]

        for i in range(start, destination):
            left += distance[i]

        if left < right:
            return left

        for i in range(destination, len(distance)):
            right += distance[i]

        return min(left, right)


if __name__ == '__main__':
    s = Solution()
    print s.distanceBetweenBusStops([1,2,3,4], 0, 1)
    print s.distanceBetweenBusStops([1,2,3,4], 0, 2)
    print s.distanceBetweenBusStops([1,2,3,4], 0, 3)
    print s.distanceBetweenBusStops([7,10,1,12,11,14,5,0], 7, 2)
