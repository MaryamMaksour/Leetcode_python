''' 

Linke: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

Runtime 
0 ms, Beats 100%

Memory 
19.20 MB, Beats 6.41%

'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l = -1
        r = len(letters)

        while ( l  + 1 < r):
            mid = int(l + (r - l)/2)

            if(letters[mid] <= target):
                 
                l = mid
            else:
                r = mid

        if r == len(letters):
            r = 0

        return letters[r]
        
