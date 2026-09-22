# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fastp, slowp = head, head

        while fastp :
            fastp = fastp.next
            if fastp : fastp=fastp.next 
            else : return False
            slowp = slowp.next
            if fastp==slowp :
                return True
        return False

        