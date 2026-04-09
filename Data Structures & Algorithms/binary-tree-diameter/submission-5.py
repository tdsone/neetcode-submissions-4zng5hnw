# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        through = max_depth_left + max_depth_right
        left_max_diam 
        right_max_diam
        diameter(root) = max(through, left_max_diam, right_max_diam)
        """

        def dfs(root):
            left_max_diam, max_depth_left = dfs(root.left) if root.left else (0, 0)
            right_max_diam, max_depth_right = dfs(root.right) if root.right else (0, 0)

            through = max_depth_left + max_depth_right
            max_diam = max(through, left_max_diam, right_max_diam)
            max_depth = 1 + max(max_depth_left, max_depth_right)

            print(f"{max_diam=}, {max_depth=}")

            return max_diam, max_depth 

        return dfs(root)[0]
