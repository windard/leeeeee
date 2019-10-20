# coding=utf-8


class TrieTreeNode(object):
    def __init__(self):
        self.is_end = False
        self.children = {}


class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        if len(folder) < 2:
            return folder

        root = TrieTreeNode()
        for fold in folder:
            head = root
            for path in fold[1:].split("/"):
                if path not in head.children:
                    child = TrieTreeNode()
                    head.children[path] = child
                head = head.children[path]
                if head.is_end:
                    break
            head.is_end = True

        result = []
        stack = [[root, '']]
        while stack:
            root, path = stack.pop()
            for child in root.children:
                if root.children[child].is_end:
                    result.append(path+"/"+child)
                    continue
                stack.append([root.children[child], path+"/"+child])
        return result


if __name__ == '__main__':
    s = Solution()
    print s.removeSubfolders(['/a', '/a/b'])
