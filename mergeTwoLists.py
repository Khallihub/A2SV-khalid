# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        aa = res
        head1 = list1
        head2 = list2
        while head1 or head2:
            if head1 and head2 and head1.val < head2.val:
                res.next = ListNode(head1.val)
                head1 = head1.next
                res = res.next
            elif head1 and head2 and head2.val <= head1.val:
                res.next = ListNode(head2.val)
                head2 = head2.next
                res = res.next

            elif not head1 and list2:
                res.next = ListNode(head2.val)
                head2 = head2.next
                res = res.next

            elif not head2 and head1:
                res.next = ListNode(head1.val)
                head1 = head1.next
                res = res.next

            else: 
                print("jj")
        return aa.next
        
