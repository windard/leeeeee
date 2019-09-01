# coding=utf-8


class Solution(object):

    def find_position(self, points, distant):
        # Time Limit
        self.count = 0

        def backtrack(nodes, path):
            if path and max(path) - min(path) > distant:
                return
            if len(path) == 3:
                if max(path) - min(path) <= distant:
                    self.count += 1
                return
            for i, n in enumerate(nodes):
                backtrack(nodes[i + 1:], path + [n])

        backtrack(points, [])
        return self.count % 99997867

    def parse_and_print(self):
        _, distant = raw_input().split()
        points = raw_input().split()
        points = map(int, points)
        print self.find_position(points, int(distant))


if __name__ == '__main__':
    s = Solution()
    # s.parse_and_print()
    print s.find_position([1,2,3,4], 3)
