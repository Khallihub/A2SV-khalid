# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        cur = head
        cu = head
        kkk = head.next
        if head.next:
            print(head.next.val)
        while cur:
            cur = cur.next
            count +=1
        k = count - n
        print(count,n,k)
        if count == 1:
            head = ListNode()
            return head.next
        while k > 1:
            cu = cu.next
            k -= 1
        if count >1:
            cu.next = cu.next.next
        if k == 0:
            return kkk
        print(cu.val)
        return head
