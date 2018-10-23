
ALPHABET_SIZE = ord('z') - ord('a') + 1

class Node:
    children = None
    word_end = False
    word_count = 0

    def __init__(self):
        self.children = [None] * ALPHABET_SIZE


class Trie:
    children = None

    def __init__(self):
        self.children = [None] * ALPHABET_SIZE

    def add(self, word):
        if not word:
            return
        cur = self
        for char in word:
            index = ord(char) - ord('a')
            child = cur.children[index]
            if not child:
                cur.children[index] = child = Node()
            child.word_count += 1
            cur = child
        cur.word_end = True

    def find(self, partial):
        cur = self
        for char in partial:
            index = ord(char) - ord('a')
            child = cur.children[index]
            if not child:
                # return []
                return 0
            cur = child
        # matches = []
        matches = 0
        if cur.word_end:
            # matches.append(partial)
            matches += 1
        # Trie._dfs(cur, partial, matches)
        # return matches
        return matches + Trie._dfs_count(cur)

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


def contacts(queries):
    o = Trie()
    rv = []
    for q in queries:
        if q[0] == 'add':
            o.add(q[1])
        else:
            rv.append(len(o.find(q[1])))
    return rv


if __name__ == '__main__':
    o = Trie()
    o.add('abc')
    o.add('jeremiah')
    o.add('jenkins')
    o.add('jam')
    o.add('jerk')
    o.add('jerkstore')
    o.add('jammin')
    print(o.find('j'))
    print(o.find('jer'))
    print(o.find('jeremiah'))

    # queries_rows = int(input())
    # queries = []
    # for _ in range(queries_rows):
    #     queries.append(input().rstrip().split())
    # print(contacts(queries))

