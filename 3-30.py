from functools import reduce

class Solution:
    def singleNumber(self, nums):
        return reduce(int.__xor__, nums, 0)
