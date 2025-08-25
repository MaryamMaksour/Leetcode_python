'''
Linke:
https://leetcode.com/problems/squares-of-a-sorted-array/description/

Runtime
29 ms,  Beats 6.97%

Memory
14.23 MB,  Beats 66.03%

Trying to solve it with:
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l = 0
        ans = []
        for i, num in enumerate(nums):
            if abs(nums[l]) > abs(num):
                l = i

        r = l+1

        while l >= 0 or r < len(nums):
            
            if l < 0:
                ans.append(nums[r]*nums[r])
                r += 1
            elif r == len(nums):
                ans.append(nums[l]*nums[l])
                l -= 1
            elif nums[l]*nums[l] < nums[r]*nums[r]:
                ans.append(nums[l]*nums[l])
                l -= 1
            else:
                ans.append(nums[r]*nums[r])
                r += 1

        return ans
            
