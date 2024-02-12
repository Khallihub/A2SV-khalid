# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cura, curb = headA, headB
        while cura and curb:
            cura = cura.next
            curb = curb.next
        cur = cura if cura else curb
        longer = "cura" if cura else "curb"
        difference = 0
        while cur:
            difference += 1
            cur = cur.next
        cura, curb = headA, headB
        if longer == "cura":
            for i in range(difference):
                cura = cura.next
        else:
            for i in range(difference):
                curb = curb.next
        while cura and curb and cura != curb:
            cura = cura.next
            curb = curb.next

        if cura == None or curb == None:
            return None
        return cura
        