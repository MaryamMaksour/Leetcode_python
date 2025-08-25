'''
Linke:
https://leetcode.com/problems/two-sum/

Runtime
7 ms,  Beats 49.11%

Memory
12.93 MB,  Beats  35.35%

Note:
Your solution must use only constant extra space.
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1

        while(l < r):
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]


            

        
