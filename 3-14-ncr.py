import math


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def unique_paths(m, n):
    return nCr(m + n - 2, m - 1)


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return unique_paths(m, n)
