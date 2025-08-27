''' 
Linke:
https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Runtime 
3 ms, Beats  3.37%

Memory 
12.40 MB, Beats 93.86%

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    ans = list()
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None:
            return []
        

        ans = []
        ans.append(root.val)  
        print(ans)

        if(root.left != None):
            ans += (self.preorderTraversal(root.left))

        if(root.right != None):
            ans += (self.preorderTraversal(root.right))

        

        return ans

         
