''' 
Linke: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

Runtime 
0 ms, Beats 100%

Memory 
17.86 MB, Beats 95.66%

 
ALGO: BFS
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []

        q = deque([root])
        ans = []
        t = 0

        while q:
            sz = len(q)
            res = []
            
            for i in range(sz):
                node = q.popleft()
                res.append(node.val)

                if(node.left):
                    q.append(node.left)

                if(node.right):
                    q.append(node.right)
            
            if(t):
                res.reverse()
          
            ans.append(res)
            t = 1-t

        return ans
        
