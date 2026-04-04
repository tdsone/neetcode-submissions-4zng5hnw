# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursively swap children
        - base case left and right are None
        """
        if root is None:
            return
        
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root