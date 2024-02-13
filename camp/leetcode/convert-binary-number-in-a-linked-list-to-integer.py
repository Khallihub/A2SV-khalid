# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = 0
        cur = head
        while cur:
            binary = binary * 2 + cur.val
            cur = cur.next
        return binary
