# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        flag = False
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                flag = True
            res = head
            head = head.next
        if flag:
            return res
        return head
       
