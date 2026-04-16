# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Idea: 
        - p and q only know children not parents but we need to traverse up the tree
        - the root is an ancestor of both p and q no matter what p and q are
        - if p and q are children of the same ancestor brand there will be a LCA 
            - we know if p and q are both on the same branch or not (because it's a bin search tree)
                - if p < a and q < a they are on the left side => recursively find new ancestor with root = root.left
                - if p > a and q > a do the same but with right child
                - if p < a and q > a then root is the lca
                - if any of both is equal to a then a is the lca
        """

        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        elif (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val): 
            return root
        elif p.val == root.val or q.val == root.val: 
            return root
