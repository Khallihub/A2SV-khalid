# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        cura = headA
        while cura:
            visited.add(cura)
            cura = cura.next
        curb = headB
        while curb:
            if curb in visited:
                return curb
            curb = curb.next
        return None