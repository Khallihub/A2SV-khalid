# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        middle = n//2
        second_half = head
        for i in range(middle):
            second_half = second_half.next
        if n%2 != 0:
            second_half = second_half.next
        prev, cur = None, second_half
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        first_half = head
        while first_half and prev:
            if first_half.val != prev.val:
                return False
            first_half = first_half.next
            prev = prev.next
        return True
