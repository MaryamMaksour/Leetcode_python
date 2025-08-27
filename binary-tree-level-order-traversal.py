''' 
Linke: https://leetcode.com/problems/binary-tree-level-order-traversal/

Runtime 
0 ms, Beats 100%

Memory 
18.32 MB, Beats 86.77%
 

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []

        ans = []

        q = deque([root])

        while q:

            sz = len(q)
            res = []
            for i in range(sz):
                node = q.popleft()
                res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            ans.append(res)

        return ans


        
