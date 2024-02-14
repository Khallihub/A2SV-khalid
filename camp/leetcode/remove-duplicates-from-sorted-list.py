# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            tmp = cur
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            tmp.next = cur.next if cur != None else cur
            cur = cur.next
        return head