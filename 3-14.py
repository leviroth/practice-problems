from functools import lru_cache


@lru_cache()
def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return unique_paths(m - 1, n) + unique_paths(m, n - 1)


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return unique_paths(m, n)
