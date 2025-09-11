''' 

Linke: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Runtime 
4 ms, Beats 1.32%

Memory 
18.31 MB, Beats 9.34%

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:

        if sorted(nums) == nums: 
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l + 1 < r:

            mid = l + int(( r - l )/2 )

            if nums[r] < nums[mid]:
                l = mid
            else:
                r = mid

        return nums[r]



         
 
