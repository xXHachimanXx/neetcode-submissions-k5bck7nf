# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # a = 123 b = 456
        # 
        # l1 = 3 -> 2 -> 1 -> None
        # l2 = 6 -> 5 -> 4 -> None
        # rs = 9 -> 7 -> 5 -> None

        # l1 = 3 -> None "0"
        # l2 = 7 -> None "0"
        # rs = 0 -> 1 -> None
        # carry = 1

    	# carry = 1
        # l1 = 4 -> 1    -> None
        # l2 = 7 -> None  
        # rs = 1 -> 2 -> None
        # if sm > 9: rs = sm%10 and carry = sm//10
        #

        # while l1 or l2

        if not l1 and not l2:
            return None
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1

        carry = 0
        root = ListNode()
        res = root

        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            sm = d1 + d2 + carry
            res_digit = sm%10
            carry = sm//10

            res.next = ListNode(res_digit)

            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return root.next


            
        