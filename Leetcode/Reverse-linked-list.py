# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        cur, prev = head, None
    
        while cur:
            step = cur.next
            cur.next = prev
            prev = cur
            cur = step
        
        return prev
