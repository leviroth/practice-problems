def move_zeroes(nums):
    dest = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[dest] = num
            dest += 1
    while dest < len(nums):
        nums[dest] = 0
        dest += 1


class Solution:
    def moveZeroes(self, nums):
        move_zeroes(nums)
