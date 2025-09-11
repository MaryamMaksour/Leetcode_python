'''

Linke:
https://leetcode.com/problems/first-bad-version/


Runtime 
36 ms, Beats 66.64%

Memory 
17.79 MB, Beats 43.75%

'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        l = -1
        r = n+1
        ans = 0

        while l + 1 < r:
            
            mid = l + int((r - l)/2)

            if ( isBadVersion(mid)):
                r = mid
                ans = mid
            else:
                l = mid

        return ans
        
