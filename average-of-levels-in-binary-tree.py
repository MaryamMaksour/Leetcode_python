''' 
Linke: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

Runtime 
3 ms, Beats 46.48%

Memory 
19.98 MB, Beats 41.82%

 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        ans = []
        if(root == None):
            return ans
        
        
        q = deque([root])

        while q:
            lev_sz = len(q)
            lev_sum = 0

            for i in range(lev_sz):
                node = q.popleft()
                lev_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right) 

            ans.append(lev_sum/lev_sz)
        
        return ans
        
