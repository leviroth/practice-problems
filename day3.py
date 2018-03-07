def value(l, i):
    if i < 0:
        return float("-inf")
    try:
        return l[i]
    except IndexError:
        return float("-inf")


def is_peak(l, i):
    value(l, i - 1) < value(l, i) > value(l, i + 1)


def _solve(l, lo, hi):
    if lo > hi:
        return lo
    mid = (lo + hi) // 2
    if is_peak(l, mid):
        return mid
    if value(l, mid) < value(l, mid + 1):
        return _solve(l, mid + 1, hi)
    return _solve(l, lo, mid - 1)


def solve(l):
    return _solve(l, 0, len(l) - 1)


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return solve(nums)
