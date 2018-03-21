from collections import Counter


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def letter_counts(counter):
    return tuple(counter[c] for c in alphabet)


def solve(words):
    groups = {}
    for word in words:
        counter = Counter(word)
        group = groups.setdefault(letter_counts(counter), [])
        group.append(word)
    return list(groups.values())


class Solution:
    def groupAnagrams(self, strs):
        return solve(strs)
