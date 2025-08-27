''' 
Linke: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

Runtime 
48 ms, Beats 75.52%

Memory 
19.17 MB, Beats 52.61%

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root == None:
            return root
        
        q = deque([root])

        root.next = None

        while q:
            sz = len(q) - 1
            node = q.popleft()

            if node.left:
                q.append(node.left)
                q.append(node.right)

            for _ in range(sz):
                rg = q.popleft()
                node.next = rg
                node = rg

                if node.left:
                    q.append(node.left)
                    q.append(node.right)

           
                

        return root
