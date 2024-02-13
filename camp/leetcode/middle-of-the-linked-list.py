# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next
            fast = fast.next
            if fast and fast.next == None:
                return slow
        return slow
        