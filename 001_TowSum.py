'''
Linke:
https://leetcode.com/problems/two-sum/

Runtime
539 ms,  Beats 47.03%

Memory
13.08 MB,  Beats  77.44%

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        frq = dict()
        ans = []

        for i, num in enumerate(nums):

            x = target - num

            if x in frq.keys():
                ans.append(i)
                ans.append(frq[x])
                break
            frq[num] = i
            
        return ans


        
        
