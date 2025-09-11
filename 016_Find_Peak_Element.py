'''
Linke:
https://leetcode.com/problems/find-peak-element/description/

Runtime 
0 ms, Beats 100.00%

Memory 
18.05 MB, Beats  18.46%

'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = -1
        r = len(nums) 
        nums.append( -((2**31) + 5))

        while ( l + 1 < r):

            mid = l + int( (r - l )/2 )

            if(nums[mid] < nums[mid+1]):
                l = mid
            else:
                r = mid

        return r
        
 
