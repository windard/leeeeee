# coding=utf-8


class Solution(object):
    def _reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Wrong Solution
        l = list(s)
        start = 0
        end = len(l) - 1
        while start < end:
            while start < len(l) and l[start] != '(':
                start += 1
            else:
                if start >= len(l):
                    break

            while end >= 0 and l[end] != ')':
                end -= 1
            else:
                if end < 0:
                    break

            start += 1
            end -= 1
            self.reverse(l, start, end)
        return ''.join(l).replace('(', '').replace(')', '')

    def reverse(self, l, s, e):
        while s < e:
            l[s], l[e] = l[e], l[s]
            s += 1
            e -= 1

    def __reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Double Point
        # O(n)
        # Still Wrong
        length = 0
        start = 0
        end = len(s) - 1
        left = right = ""

        while start <= end and s[start] != '(':
            left += s[start]
            start += 1

        while end >= start and s[end] != ')':
            right = s[end] + right
            end -= 1

        while start <= end:
            # 每轮计算 () 之间的数据
            if s[start] == '(' and s[end] == ')':
                start += 1
                end -= 1
                length += 1

            while start <= end and s[start] != '(':
                if length % 2:
                    right = s[start] + right
                else:
                    left += s[start]
                start += 1

            while start <= end and s[end] != ')':
                if length % 2:
                    left += s[end]
                else:
                    right = s[end] + right
                end -= 1
        return left + right

    def ___reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 最终还是要入栈来做
        stack = []
        last_stack = stack
        stacks = []
        for v in s:
            if v == '(':
                new_stack = []
                stacks.append(last_stack)
                last_stack = new_stack
            elif v == ')':
                before_stack = stacks.pop()
                before_stack.extend(last_stack[::-1])
                last_stack = before_stack
            else:
                last_stack.append(v)
        return ''.join(stack)

    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 其实可以不用额外的栈来存储
        stack = []
        last_stack = stack
        for v in s:
            if v == '(':
                new_stack = []
                new_stack.append(last_stack)
                last_stack = new_stack
            elif v == ')':
                before_stack = last_stack.pop(0)
                before_stack.extend(last_stack[::-1])
                last_stack = before_stack
            else:
                last_stack.append(v)
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    print s.reverseParentheses("ta()usw((((a))))")
    print s.reverseParentheses("(abcd)")
    print s.reverseParentheses("(u(love)i)")
    print s.reverseParentheses("(ed(et(oc))el)")
    print s.reverseParentheses("a(bcdefghijkl(mno)p)q")
