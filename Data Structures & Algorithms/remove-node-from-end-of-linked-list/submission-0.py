# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> null
        #           l         r
        #           2    1     
        
        # if n is the head
        # 1 ->  2 -> null
        # p     c

        res = ListNode(0, head)
        r, l = head, res

        while n > 0:
            n -= 1 
            r = r.next
        
        while r:
            r = r.next
            l = l.next
        
        l.next = l.next.next

        return res.next

