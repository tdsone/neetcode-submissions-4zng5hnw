# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        DFS: 

        go from root to node and keep track of path
        - we only need to keep track of max value in path not full path values
        """

        good_nodes = 0 

        def dfs(node, max_val):
            nonlocal good_nodes

            # do something
            if node.val >= max_val: 
                good_nodes += 1
                max_val = node.val
            
            if node.right:
                dfs(node.right, max_val)
            if node.left:
                dfs(node.left, max_val)

        dfs(root, root.val)

        return good_nodes