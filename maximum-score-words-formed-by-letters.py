# coding=utf-8


class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        # 背包问题
        # 但是因为容量问题
        # 1 <= words.length <= 14
        # 1 <= words[i].length <= 15
        # 可以直接用暴力
        if not words:
            return 0
        total = []
        max_score = 0
        for word in words:
            if not self.check_coexist([word], letters):
                continue
            max_score = max(max_score, self.count_score([word], score))
            if total:
                # 此处不能变遍历边添加
                current = []
                for t in total:
                    if self.check_coexist(t+[word], letters):
                        max_score = max(max_score,
                                        self.count_score(t+[word], score))
                        current.append(t+[word])
                total.extend(current)
            total.append([word])
        return max_score

    def check_coexist(self, total, letters):
        data = {}
        for w in total:
            for t in w:
                data[t] = data.get(t, 0) + 1

        l_data = {}
        for l in letters:
            l_data[l] = l_data.get(l, 0) + 1

        for key, value in data.items():
            if l_data.get(key, 0) < value:
                return False
        return True

    def count_score(self, total, score):
        count = 0
        for w in total:
            for t in w:
                count += score[ord(t) - ord('a')]
        return count


if __name__ == '__main__':
    s = Solution()
    print s.maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])
    print s.maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10])
    print s.maxScoreWords(["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0])
    print s.maxScoreWords(["add","dda","bb","ba","add"], ["a","a","a","a","b","b","b","b","c","c","c","c","c","d","d","d"], [3,9,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    print s.maxScoreWords(["e","bac","baeba","eb","bbbbd","cad","c","c"], ["a","a","a","a","a","a","a","b","b","b","b","b","b","c","c","c","c","c","c","d","d","d","d","d","d","d","e","e","e","e"], [8,4,6,8,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
