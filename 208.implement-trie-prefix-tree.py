# coding=utf-8
#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (36.80%)
# Likes:    1762
# Dislikes: 34
# Total Accepted:    193.5K
# Total Submissions: 485.5K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
#  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#


class TreeNode(object):
    # 其实 value 是不需要的，因为在父节点的子节点列表里存了
    # 可以 用哈希表存子节点，也可以用最大26的数组来存
    # 其实 还需要一个字段，是否单词结尾，因为会有前缀匹配的单词，比如 app,apple
    def __init__(self):
        # self.value = value
        self.children = {}
        self.is_end = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.root
        for w in word:
            if w not in root.children:
                node = TreeNode()
                root.children[w] = node
            root = root.children[w]
        root.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for w in word:
            if w in root.children:
                root = root.children[w]
            else:
                return False
        return root.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for w in prefix:
            if w in root.children:
                root = root.children[w]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# if __name__ == '__main__':
#     obj = Trie()
#     obj.insert('word')
#     obj.insert('app')
#     obj.insert('apple')
#     obj.insert('add')
#     print obj.search('word')
#     print obj.startsWith('prefix')
#     print obj.search('wor')
#     print obj.startsWith('wor')
#     print obj.search('app')
#     print obj.search('apps')
