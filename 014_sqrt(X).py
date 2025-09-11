'''

Linke:
https://leetcode.com/problems/search-insert-position/description/


Runtime 
5 ms, Beats 31.70%

Memory 
17.81 MB, Beats 32.86%

''' 
 class Solution:
    def mySqrt(self, x: int) -> int:

        l = 0
        r = int((x+1)/2) + 1

        while l + 1 < r:

            mid = l + int((r - l )/2)

            if(mid*mid <= x):
                l = mid
            else:
                r = mid

        return l
        
