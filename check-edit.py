class Solution():
    def solve(self, paths):
        result = []
        for path in paths:
            index = 0
            temp = ''
            flag = False
            while index < len(path):
                if index and path[index - 1] == path[index]:
                    if not flag:
                        temp += path[index]
                    while index < len(path) and path[index - 1] == path[index]:
                        index += 1
                    if flag:
                        flag = False
                    else:
                        flag = True
                else:
                    temp += path[index]
                    if index < len(path)-1 and path[index] != path[index+1]:
                        flag = False
                    index += 1
            result.append(temp)

        return result

    def parse(self):
        n = input()
        result = []
        for i in range(n):
            result.append(raw_input())
        answer = self.solve(result)
        for a in answer:
            print a


if __name__ == '__main__':
    s = Solution()
    # s.parse()
    # print s.solve(["helloo", "helllo", "wooooow", "aabbbcc"])
    print s.solve(["aabcc"])
    print s.solve(["yyybeettxjjjpppddsrxxxkkkyyyooowwwwwkyyxxppplllwwwiivvssnrvvvccclyydddhaaayiic"])