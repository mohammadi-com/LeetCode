# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        l3 = output = ListNode()

        while l1 or l2:
            if l1 and l2:
                d_sum = l1.val + l2.val + l3.val
                l3.val = d_sum % 10
                print(f"l3 is {l3}")
                carry = d_sum // 10
                print(f"carry is {carry}")
                if l1.next or l2.next or carry:
                    l3.next = ListNode(val=carry)
                    print(f"l3 iss {l3}")
                    l3 = l3.next
                    print(f"l3 isss {l3}")
                l1 = l1.next
                l2 = l2.next
            elif l1:
                d_sum = l1.val + l3.val
                l3.val = d_sum % 10
                carry = d_sum // 10
                if l1.next or carry:
                    l3.next = ListNode(val=carry)
                    l3 = l3.next
                l1 = l1.next
            else:
                d_sum = l2.val + l3.val
                l3.val = d_sum % 10
                carry = d_sum // 10
                if l2.next or carry:
                    l3.next = ListNode(val=carry)
                    l3 = l3.next
                l2 = l2.next

        return output
