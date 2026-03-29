# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = set()
        curr = head

        if not curr:
            return False
        
        while curr:
            if curr in count:
                return True

            count.add(curr)
            curr = curr.next

        return False
            
        