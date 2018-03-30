class Solution(object):
    def hammingWeight(self, n):
        counter = 0
        while n > 0:
            counter += n & 1
            n >>= 1
        return counter
