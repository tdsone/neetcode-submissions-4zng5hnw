# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        BST: 
        1) all nodes on right are larger than current node
        2) all nodes on left are smaller than current node
        3) 1 and 2 hold for all nodes

        We can recursively check whether all nodes fall into correct range to avoid double checking nodes
        range is [min, max] where both are excl. -> curr val needs to be larger than min and smaller than max 
        -> range get's updated with every recursive call

        Issue: if we first check if all nodes on left are smaller and then check if left subtree is a bst, we check all nodes twice for every node
        """

        def _is_valid(node, range) -> bool:
            if range[0] is not None and not range[0] < node.val:
                return False
            if range[1] is not None and not range[1] > node.val:
                return False

            left_valid, right_valid = True, True
            if node.left: 
                left_valid = _is_valid(node.left, [range[0], node.val])
                
            if left_valid and node.right:
                right_valid = _is_valid(node.right, [node.val, range[1]])

            return left_valid and right_valid

        return _is_valid(root, [None, None])
        