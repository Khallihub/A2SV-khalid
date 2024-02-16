# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None for i in range(k)]
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        if n <= k:
            cur = head
            i = 0
            while cur:
                res[i] = cur
                tmp = cur.next
                cur.next = None
                cur = tmp
                i += 1
        else:
            parts = [n//k for i in range(k)]
            rem = n % k
            i = 0
            while rem > 0:
                parts[i] += 1
                i += 1
                rem -= 1
            cur = head
            for i in range(k):
                partsLen = parts[i]-1
                res[i] = cur
                while cur and partsLen > 0:
                    cur = cur.next
                    partsLen -= 1
                if cur == None:
                    break
                tmp = cur.next
                cur.next = None
                cur = tmp
            tmp = res[-1]
            while tmp.next:
                tmp = tmp.next
            tmp.next = cur
        return res
        
