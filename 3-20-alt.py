def solve(s):
    seen = set()
    start = 0
    longest = 0
    for i, c in enumerate(s):
        if c in seen:
            while s[start] != c:
                seen.remove(s[start])
                start += 1
            seen.remove(s[start])
            start += 1
        seen.add(c)
        longest = max(longest, i - start + 1)
    return longest


class Solution:
    def lengthOfLongestSubstring(self, s):
        return solve(s)
