"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        - bfs approach

        - recursive
        """
    
        def _copyRandomList(head, visited):
            if head is None: 
                return None
                 
            new_node = Node(x=head.val, next=None, random=None)
            visited[head] = new_node

            if head.next is not None:
                if head.next not in visited:
                    new_node.next = _copyRandomList(head.next, visited)
                else: 
                    new_node.next = visited[head.next]
            if head.random is not None:
                if head.random not in visited:
                    new_node.random = _copyRandomList(head.random, visited)
                else: 
                    new_node.random = visited[head.random]
            
            return new_node
        
        visited = {}

        return _copyRandomList(head, visited)
                