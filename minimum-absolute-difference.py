# coding=utf-8


class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        min_num = float("inf")
        min_length = []
        arr.sort()
        ready = 0
        next_one = 1
        while next_one < len(arr):
            index = ready + 1
            while index < len(arr):
                if next_one >= len(arr) -1 or arr[index] - arr[ready] <= arr[next_one+1] - arr[next_one]:
                    if arr[ready+1] - arr[ready] < min_num:
                        min_length = [[arr[ready], arr[ready+1]]]
                        min_num = arr[ready+1] - arr[ready]
                    elif arr[ready+1] - arr[ready] == min_num:
                        min_length.append([arr[ready], arr[ready+1]])
                    else:
                        break
                else:
                    break

                index += 1

            ready += 1
            next_one += 1
        return min_length


if __name__ == '__main__':
    s = Solution()
    print s.minimumAbsDifference([1,2,3,4])
    print s.minimumAbsDifference([4,2,1,3])
    print s.minimumAbsDifference([1,3,6,10,15])
    print s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])
