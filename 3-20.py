def solve(s):
    last_seen = {}
    start = 0
    longest = 0
    for i, c in enumerate(s):
        last_i = last_seen.get(c)
        if None is not last_i >= start:
            start = last_i + 1
        last_seen[c] = i
        longest = max(longest, i - start + 1)
    return longest


class Solution:
    def lengthOfLongestSubstring(self, s):
        return solve(s)
