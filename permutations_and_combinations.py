# coding=utf-8


def power(m, n):
    return m ** n



def permutations(nums, length):
    if length > len(nums):
        return
    nums = list(nums)

    result = []
    loop = 0
    while loop < length:
        if not result:
            for n in nums:
                result.append([n])
        else:
            new_result = []
            for group in result:
                items = nums[:]
                for g in group:
                    items.remove(g)
                for i in items:
                    new_result.append(group + [i])
            result = new_result
        loop += 1
    return result


def combine(n, k):
    start = 1
    n += 1
    result = []

    def inner_combine(s, e, p):
        if e == 0:
            result.append(p)
            return

        for i in range(s, n):
            inner_combine(i + 1, e - 1, p + [i])

    inner_combine(start, k, [])
    return result


def combinations_with_replacement(n, k):
    start = 1
    n += 1
    result = []

    def inner_combine(s, e, p):
        if e == 0:
            result.append(p)
            return

        for i in range(s, n):
            inner_combine(i, e - 1, p + [i])

    inner_combine(start, k, [])
    return result


if __name__ == "__main__":
    print permutations(range(5), 3)
    print permutations('abcde', 2)
    print combine(4, 2)
    print combinations_with_replacement(4, 2)
