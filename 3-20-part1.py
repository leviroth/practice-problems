def is_palindrome(s, lo, hi):
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True


def solve(s):
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return is_palindrome(s, lo + 1, hi) or is_palindrome(s, lo, hi - 1)
        lo += 1
        hi -= 1
    return True


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return solve(s)
