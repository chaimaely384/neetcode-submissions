# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        lastn = head
        l = 0

        while lastn :
            lastn = lastn.next
            l += 1

        removeindx = l-n

        if removeindx == 0 :
            return head.next

        curr = head
        
        for i in range(l-1) :
            if i+1 == removeindx :
                curr.next = curr.next.next
                break
            curr = curr.next
        return head



       

        