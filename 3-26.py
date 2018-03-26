alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Node:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def _insert(self, word, index, node):
        if index == len(word):
            node.end = True
        else:
            c = word[index]
            if c not in node.children:
                node.children[c] = Node()
            self._insert(word, index + 1, node.children[c])

    def _find(self, word, index, node, acc):
        if node.end:
            return acc
        if index == len(word):
            return None
        c = word[index]
        acc.append(c)
        return self._find(word, index + 1, node.children[c], acc)

    def insert(self, word):
        self._insert(word, 0, self.root)

    def find(self, word):
        try:
            result = self._find(word, 0, self.root, [])
            if result is None:
                return None
            return ''.join(result)
        except KeyError:
            return None


def solve(words, sentence):
    t = Trie()
    for word in words:
        t.insert(word)
    sentence = sentence.split()
    l = []
    for word in sentence:
        result = t.find(word)
        if result is None:
            l.append(word)
        else:
            l.append(result)
    return ' '.join(l)


class Solution:
    def replaceWords(self, words, sentence):
        return solve(words, sentence)
