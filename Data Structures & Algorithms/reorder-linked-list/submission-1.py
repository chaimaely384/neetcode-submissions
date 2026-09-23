# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #divide the listnode into 2 lists by half

        fastp, slowp = head.next, head

        while fastp and fastp.next :
            fastp = fastp.next.next
            slowp = slowp.next
        

        
        L1, L2 = head, slowp.next
        slowp.next = None

        #Reinverse the order of L2

        prev, curr = None, L2

        while curr :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        L2 = prev

        while L2 :
            temp1, temp2 = L1.next, L2.next
            L1.next = L2
            L2.next = temp1
            L1, L2 = temp1, temp2

        
        
        
        
        