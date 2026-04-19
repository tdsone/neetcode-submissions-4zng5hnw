# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Adjusted level order traversal

        level order traversal
        - queue to process nodes by level
        - each level has one array per level

        - here, the rightmost node is in view but we need 
          to process the other nodes because they might have 
          in-view children
        """
        view = []
        if root is None: 
            return view

        q = deque([(root, 0)])
        level = 0

        last = None
        while q:
            curr_node, curr_level = q.popleft()
            
            if curr_node.left: 
                q.append((curr_node.left, curr_level + 1))
            if curr_node.right: 
                q.append((curr_node.right, curr_level + 1))

            if curr_level > level:
                level += 1
                view.append(last.val)

            if not q: 
                view.append(curr_node.val)

            last = curr_node

        return view