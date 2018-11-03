from collections import defaultdict


class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.word_count = 0
        self.word_end = False


class Trie:
    def __init__(self):
        self.head = Node()

    def add(self, word):
        cur = self.head
        for char in word:
            cur = cur.children[char]
            cur.word_count += 1
        cur.word_end = True

    def search(self, word):
        cur = self.head
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.word_end

    def search_prefix(self, prefix):
        cur = self.head
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.word_count

    def match_prefix(self, prefix):
        cur = self.head
        for char in prefix:
            if char not in cur.children:
                return []
            cur = cur.children[char]

        def dfs(node, prefix, words):
            for char, child in node.children.items():
                concat = prefix + char
                if child.word_end:
                    words.append(concat)
                dfs(child, concat, words)

        matches = []
        dfs(cur, prefix, matches)
        return matches

    @classmethod
    def _dfs_count(cls, node):
        count = 0
        for i, child in enumerate(node.children):
            if child:
                count += child.word_count
                # match = 0
                # if child.word_end:
                #     match = 1
                # count += match + cls._dfs_count(child)
        return count

    @classmethod
    def _dfs(cls, node, prefix, words):
        for i, child in enumerate(node.children):
            if child:
                concat = prefix + chr(ord('a') + i)
                if child.word_end:
                    words.append(concat)
                cls._dfs(child, concat, words)


if __name__ == '__main__':
    o = Trie()
    o.add('abc')
    o.add('jeremiah')
    o.add('jenkins')
    o.add('jam')
    o.add('jerk')
    o.add('jerkstore')
    o.add('jammin')
    assert(o.search('abc') == True)
    assert(o.search('ab') == False)
    assert(o.search_prefix('abc') == 1)
    assert(o.search_prefix('ab') == 1)
    assert(o.search_prefix('j') == 6)
    assert(o.search_prefix('jer') == 3)
    assert(o.search_prefix('z') == 0)
    print(o.match_prefix('je'))
