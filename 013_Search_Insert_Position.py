'''

Linke:
https://leetcode.com/problems/search-insert-position/description/


Runtime 
0 ms, Beats 100.00%

Memory 
18.53 MB, Beats 26.52%

''' 


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = -1
        r = len(nums)

        while l + 1 < r:
            
            mid = l + int((r - l)/2)

            if(nums[mid] < target):
                l = mid
            else:
                r = mid
        
        return r



        
