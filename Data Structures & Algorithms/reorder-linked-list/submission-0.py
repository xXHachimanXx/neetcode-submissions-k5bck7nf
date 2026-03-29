# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 6, 1, 3, 4, 5, 6]
        #        h        t
        
        #  h.next -> t
        #  t.next -> h.next.next
        #  
        #  0
        # [0 -> 1 -> 2 -> 3 -> null 4 <- 5 <- 6]
        #  h                        sd        f

        # find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next

        # reverse second part
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge then
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


        