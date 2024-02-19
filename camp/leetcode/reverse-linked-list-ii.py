# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        beforeLeft = None
        
        for _ in range(left - 1):
            beforeLeft = cur
            cur = cur.next

        prev = None
        start = cur
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        if beforeLeft:
            beforeLeft.next = prev
        else:
            head = prev
        start.next = cur

        return head
