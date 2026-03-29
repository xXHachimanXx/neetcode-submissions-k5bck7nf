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

        mp = {}

        # 1 ->       2 ->       3 -> None
        #   -> None    -> 3       -> 3

        def copyRandomListAux(head):
            if not head:
                return None
            if head in mp:
                return mp[head]
            
            new_node = Node(head.val)
            mp[head] = new_node
            new_node.next = copyRandomListAux(head.next)
            new_node.random = mp.get(head.random)

            return new_node
            

        return copyRandomListAux(head)