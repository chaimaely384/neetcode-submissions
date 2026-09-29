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

        H = {None : None}
        L = head

        while L :
            copy = Node(L.val)
            H[L] = copy
            L = L.next

        curr = head
        while curr :
            copy = H[curr]
            copy.next = H[curr.next]
            copy.random = H[curr.random]
            curr = curr.next
        return H[head]
