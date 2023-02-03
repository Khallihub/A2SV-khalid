# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def length1(l):
            count = 0
            while l:
                l = l.next
                count +=1
            return count
        len1 = length1(l1)
        len2 = length1(l2)
    
        head1 = l1
        head2 = l2
        flag = False
        if len1 > len2:
            flag = True
        if not flag:
            head1, head2 = head2, head1
        res = head1
        rr = res
        carry = 0
        while head1:
            if head2:
                sum = head1.val + head2.val + carry
            elif head1 and carry:
                sum = head1.val + carry
            elif head1 and not carry:
                sum = head1.val
            else:
                sum = carry
            print(sum)
            carry = 0
            if sum <= 9:
                print(sum)

                res.val = sum
                res = res.next
                sum = 0
            else:
                print(sum)

                a = int(str(sum)[1])
                res.val = a
                if not res.next:
                    res.next = ListNode("1")
                    break
                res = res.next
                sum = 0
                carry = 1
                

            head1 = head1.next
            if head2:
                head2 = head2.next
        return rr
