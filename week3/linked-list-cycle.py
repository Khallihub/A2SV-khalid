# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using visited 
        # visited = set()
        # cur = head
        # while cur:
        #     if cur in visited:
        #         return True
        #     visited.add(cur)
        #     cur = cur.next
        # return False
        # using floyds
        slow, fast = head,head
        if fast:
            fast = fast.next
        if fast == None:
            return False
        fast = fast.next
        if fast == None:
            return False

        while slow != fast and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False
        if fast == None:
            return False
        return True