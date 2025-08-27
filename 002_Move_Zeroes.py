'''

Link:
https://leetcode.com/problems/move-zeroes/

Runtime:
3 ms,  Beats 89.05%


Memory:
13.53 MB,  Beats 61.90%

'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_idx = -1

        for i, num in enumerate(nums):
            if num != 0 and zero_idx != -1:
                nums[zero_idx] = num
                nums[i] = 0
                zero_idx += 1
            elif num == 0 and zero_idx == -1:
                zero_idx = i

